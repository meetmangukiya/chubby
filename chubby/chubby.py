import sys
import logging

from chubby.argparser import parser
import chubby.chulib as chulib

args = parser.parse_args()

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('[%(levelname)s]\t[%(name)s]\t%(message)s'.format('')))
logger.addHandler(ch)
#logger.setFormatter(logging.Formatter('%(levelname)s:%(module)s:%(message)s'))

def main():
    if args.log:
        logger.setLevel(getattr(logging, args.log.upper()))
    logger.debug('args parsed: {}'.format(args))

    # Config command
    if args.command == 'config':
        logger.debug('Command config invoked...')
        gh = chulib.save_to_config(args.user)

    # Create command
    elif args.command == 'create':
        logger.debug('`create` subparser triggered...')
        if not args.create:
            print("chubby: error: provide subcommand for create eg. `chubby create issue`")
            logger.debug('exiting: No subcommand for create provided...')
            sys.exit()

        # Create issue command
        if args.create == 'issue':
            # check required args
            logger.debug('subcommand `create issue` triggered...')
            if not args.issue_title or not args.issue_repo or not args.user:
                print("chubby: Insufficient args provided. Ensure that you've provided `--title`, `--repo`, and `--user`")
                logger.debug('exiting: Insufficient args provided for `issue`...')
                sys.exit()

            gh = chulib.get_login(args.user)

            title = args.issue_title
            description = args.issue_description
            owner = args.issue_repo.split('/')[0]
            repo = args.issue_repo.split('/')[1]
            # create issue
            issue = gh.create_issue(owner=owner, repository=repo, title=title, body=description)
            print("Issue created successfully:", '#' + str(issue.number), issue.html_url)

        # Create repo command
        if args.create == 'repo':
            # check required args
            logger.debug('subcommand `create repo` triggered...')
            if not args.user or not args.repo_name:
                print("chubby: Insufficient args provided. Ensure that you've provided `--user`, `--name` arguments")
                logger.debug("exiting: Insufficient args provided for `repo`...")
                sys.exit()

            gh = chulib.get_login(args.user)

            description = args.repo_description

            repo = gh.create_repo(args.repo_name, description=description)
            print("Repository created successfully:", repo.html_url)

if __name__ == '__main__':
    main()
