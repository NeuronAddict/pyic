from setuptools import setup

setup(name='pyic',
      version='0.1',
      description='Python injection console lib',
      url='http://github.com/neuronaddict/pyic',
      author='neuronaddict',
      author_email='',
      license='GNUv3',
      packages=['pyic'],
      zip_safe=False, install_requires=['requests', 'html2text', 'termcolor', 'prettytable'])
