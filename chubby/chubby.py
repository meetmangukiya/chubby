import sys
import logging

from IGitt.GitHub import GitHubToken
from IGitt.GitHub.GitHubIssue import GitHubIssue
import requests

from chubby import VERSION
from chubby.argparser import parser
from chubby.config import read_config, write_config

args = parser.parse_args()

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('[%(levelname)s]\t[%(name)s]\t%(message)s'.format('')))
logger.addHandler(ch)

def requires(arguments, required):
    for arg in required:
        if not getattr(arguments, arg):
            print(arg + " is a required argument")
            return False
    return True

def take_action(args):
    if args.command == 'config':
        # configure, save token to .chubby file
        token = args.token or input('Enter github token: ')
        username = requests.get('https://api.github.com/user',
                                headers={
                                    'Authorization': 'token ' + token
                                }).json()['login']
        config = read_config()
        write_config('DEFAULT', {'token': token, 'username': username})
        print("chubby configured successfully!")
        return
    else:
        title = args.issue_title
        body = args.issue_description
        issue_number = args.issue_number
        repo = args.repository
        config = read_config()
        token = GitHubToken(config["DEFAULT"]["token"])
        username = config["DEFAULT"]["username"]

        if args.command == 'issue':
            if args.get:
                # get issue by number
                if requires(args, ["repository", "issue_number"]):
                    issue = GitHubIssue(token, repo, issue_number)
                    print(
                        "Title: {}\n"
                        "Description: {}\n"
                        "Labels: {}\n"
                        "Assignees: {}\n"
                        "URL: {}".format(issue.title, issue.description,
                                         ', '.join(issue.labels),
                                         ', '.join(issue.assignees),
                                         issue.url))
                return
            if not args.edit:
                # create a new issue
                if requires(args, ["issue_title", "repository"]):
                    if '/' not in repo:
                        repo = '/'.join([username, repo])
                    try:
                        issue = GitHubIssue.create(token, repo, title, body)
                    except RuntimeError:
                        logger.exception("An exception occured while creating an "
                                         "issue")
                        print("Something went wrong while creating issue. Please "
                              "ensure that you have rights to the repo provided.")
                    else:
                        print("Issue created successfully: {}".format(issue.url))
                return
            else:
                # edit an existing issue
                if requires(args, ["repository", "issue_number"]):
                    issue = GitHubIssue(token, repo, iss_number)
                    if title:
                        issue.title = title
                    if body:
                        print("Editing just the title, cannot edit the body :(")
                    print("Issue edited successfully: {}".format(issue.url))

def main():
    if args.command:
        take_action(args)
    else:
        if args.version:
            print("chubby {}".format(VERSION))

if __name__ == '__main__':
    main()
