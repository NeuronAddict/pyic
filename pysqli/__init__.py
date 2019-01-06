from pysqli.blind_tester import BlindTester
from pysqli.tools import SqliEncoder
from pysqli.body_conditions import *
from pysqli.blind_string_finder import BlindStringFinder
from pysqli.union_string_finder import UnionStringFinder
from pysqli.star_extract import StarExtract
from pysqli.db_dumper import DbDumper
from pysqli.manual_loop import *
from pysqli.payloads import *

# noinspection PyUnresolvedReferences
import requests

if __name__ == '__main__':
    print("#" * 25 + "\n#\n# python sqli lib loaded!\n#\n" + "#" * 25)
    print('\nTo get help, type help(object) with object the following : '
          'Tester, BlindStringFinder, UnionStringFinder, BlindTester, '
          'SqliEncoder, DbDumper, HasText, Not, loop, StarExtract\n')
    print('Type dir() to see all availables types and try help(<type>) to search other help\n')
    print('You can also read the source code!\n')
