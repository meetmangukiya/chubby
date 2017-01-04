import argparse

parser = argparse.ArgumentParser(description="GitHub in your terminal",
                                 prog="chubby")

parser.add_argument('config',
                    required=False,
                    help="Obtain access token and save to config file")
