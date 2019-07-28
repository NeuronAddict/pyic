from pyic.blind_tester import BlindTester
from pyic.tools import SqliEncoder
from pyic.body_conditions import *
from pyic.blind_string_finder import BlindStringFinder
from pyic.union_string_finder import UnionStringFinder
from pyic.star_extract import StarExtract
from pyic.db_dumper import DbDumper
from pyic.manual_loop import *
from pyic.payloads import *
from pyic.loggers import *
from pyic.html2text_filter import *
from pyic.time_blind_tester import *

# noinspection PyUnresolvedReferences
import requests

if __name__ == '__main__':
    print("#" * 25 + "\n#\n# pyic lib loaded!\n#\n" + "#" * 25)
    print('\nTo get help, type help(object) with object the following : '
          'Tester, BlindStringFinder, UnionStringFinder, BlindTester, '
          'SqliEncoder, DbDumper, HasText, Not, loop, StarExtract\n')
    print('Type dir() to see all availables types and try help(<type>) to search other help\n')
    print('You can also read the source code!\n')
    print('https://github.com/NeuronAddict/pyic\n')
