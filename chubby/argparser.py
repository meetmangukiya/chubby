"""
ArgumentParser of chubby.
"""

import argparse

parser = argparse.ArgumentParser(description="GitHub in your terminal",
                                 prog="chubby")

# Important:
# Won't work if used like `chubby create -L ...`
# Should be used as `chubby -L debug ...`
parser.add_argument('--log', '-L',
                    help='Set log level')

parser.add_argument('--version', '-v',
                    help='Show chubby version',
                    action='store_true')


subparsers = parser.add_subparsers(dest='command')

# Config subparser
# ----------------
config_parser = subparsers.add_parser('config',
                                      help='configure chubby')

config_parser.add_argument('-t', '--token',
                    help='github account token')


# Issue subparser
# ---------------

issue_subparser = subparsers.add_parser('issue',
                                        help='GitHub issue utilities')

issue_subparser.add_argument('-t', '--title',
                             dest='issue_title',
                             help='Title of the issue')

issue_subparser.add_argument('-d', '--description',
                             dest='issue_description',
                             help='Description of the issue',
                             default='')

issue_subparser.add_argument('-e', '--edit',
                             help='Edit issue',
                             action='store_true',
                             default=False)

issue_subparser.add_argument('-r', '--repository',
                             help='Repository for the issue')

issue_subparser.add_argument('-n', '--number',
                             dest='issue_number',
                             help='Issue number')

issue_subparser.add_argument('-g', '--get',
                             action='store_true',
                             help='Get a given issue')
