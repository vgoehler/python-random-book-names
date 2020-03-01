"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mrandom_book_names` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``random_book_names.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``random_book_names.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse


class CLI:
    def __init__(self):
        self.args = None

        self.parser = argparse.ArgumentParser(description='Command description.')
        self.parser.add_argument('--number', type=int,
                                 help="The amount of runs.")

    def parse(self, args):
        self.args = self.parser.parse_args(args)
        return self.args


def main(args=None):
    cli = CLI()
    args = cli.parse(args=args)
    print(args.names)
