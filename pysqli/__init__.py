from pysqli.blindtester import BlindTester
from pysqli.tools import SqliEncoder
from pysqli.body_conditions import *
from pysqli.string_finder import StringFinder
from pysqli.db_dumper import DbDumper
from pysqli.manual_loop import *

# noinspection PyUnresolvedReferences
import requests

if __name__ == '__main__':
    print("#" * 25 + "\n#\n# python sqli lib loaded!\n#\n" + "#" * 25)
    print('\nTo get help, type help(object) with object the following : '
          'Tester, StringFinder, SqliEncoder, DbDumper, HasText, Not, loop, ManualLoop\n')

