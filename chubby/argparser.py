import argparse

parser = argparse.ArgumentParser(description="GitHub in your terminal",
                                 prog="chubby")

subparsers = parser.add_subparsers()


parser_config = subparsers.add_parser('config',
                                      help='Obtain access token and save to config file')

parser_config.add_argument('username',
                           default=None,
                           help="Obtain access token and save to config file")
