import sys

from chubby.argparser import parser
import chubby.chulib as chulib

args = parser.parse_args()

def main():
    # Config command
    if args.command == 'config':
        print("config")
        gh = chulib.save_to_config(args.user)

    # Create command
    elif args.command == 'create':
        # Create issue command
        if not args.create:
            print("chubby: error: provide subcommand for create eg. `chubby create issue`")
            sys.exit()

        if args.create == 'issue':
            # check required args
            if not args.issue_title or not args.issue_repo or not args.user:
                print("chubby: Insufficient args provided. Ensure that you've provided `--title`, `--repo`, and `--user`")
                sys.exit()

            gh = chulib.get_login(args.user)

            title = args.issue_title
            description = args.issue_description
            owner = args.issue_repo.split('/')[0]
            repo = args.issue_repo.split('/')[1]
            # create issue
            issue = gh.create_issue(owner=owner, repository=repo, title=title, body=description)
            print("Issue created successfully:", '#' + str(issue.number), issue.html_url)

if __name__ == '__main__':
    main()
