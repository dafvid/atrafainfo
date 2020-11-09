import sys

__version__ = '201109.1'


def eprint(s):
    print(s, file=sys.stderr)

eprint('atrafadata v.{}'.format(__version__))
