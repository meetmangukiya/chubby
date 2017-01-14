import argparse

parser = argparse.ArgumentParser(description="GitHub in your terminal",
                                 prog="chubby")

subparsers = parser.add_subparsers(dest='command')

# Config subparser
# ----------------

parser_config = subparsers.add_parser('config',
                                      help='Obtain access token and save to config file')

parser_config.add_argument('user',
                           help="Obtain access token and save to config file")

# Create subparser
# ----------------

parser_create = subparsers.add_parser('create',
                                      help='Create repositories, issues, pull requests, etc.')


create_subparser = parser_create.add_subparsers(dest='create')

## Issue Sub-subparser
## -------------------

issue_parser = create_subparser.add_parser('issue',
                                            help='Fiddle with GitHub issues')

issue_parser.set_defaults(create='issue')

issue_parser.add_argument('-t', '--title',
                          help='Title of the issue',
                          dest='issue_title')

issue_parser.add_argument('-d', '--description',
                          dest='issue_description',
                          help='Description of the issue')

issue_parser.add_argument('-r', '--repo', '--repository',
                          dest='issue_repo',
                          help='Repository to create issue on')

issue_parser.add_argument('-u', '--user',
                          dest='user',
                          help='Username of the account to carry out actions on')
