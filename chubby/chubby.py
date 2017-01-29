import sys
import logging

from chubby.argparser import parser
import chubby.chulib as chulib
import chubby.config as config

args = parser.parse_args()

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('[%(levelname)s]\t[%(name)s]\t%(message)s'.format('')))
logger.addHandler(ch)
#logger.setFormatter(logging.Formatter('%(levelname)s:%(module)s:%(message)s'))

is_default = "DEF" in config.read_config().sections()

def main():
    if args.log:
        logger.setLevel(getattr(logging, args.log.upper()))
    logger.debug("is_default: " + "True" if is_default else "False")
    logger.debug('args parsed: {}'.format(args))

    if not args.command or args.command == 'help':
        logger.debug("No commands given, printing help and exiting...")
        parser.print_help()
        sys.exit()

    # Config command
    if args.command == 'config':
        logger.debug('Command config invoked...')
        if args.default_user:
            logger.debug('Setting ' + args.user + ' as default user')
            state = chulib.set_default(args.user)
            if state:
                logger.debug("Setting default succeeded")
                print("Username " + args.user + " set as default user")
        else:
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
            if not args.issue_title or not args.issue_repo or not args.user and not is_default:
                print("chubby: Insufficient args provided. Ensure that you've provided `--title`, `--repo`" + ", and `--user`" if not is_default else "")
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
            if not args.user or not args.repo_name and not is_default:
                print("chubby: Insufficient args provided. Ensure that you've provided arguments: `--name`" + " `--user`" if not is_default else "")
                logger.debug("exiting: Insufficient args provided for `repo`...")
                sys.exit()

            gh = chulib.get_login(args.user)

            description = args.repo_description

            repo = gh.create_repo(args.repo_name, description=description)
            print("Repository created successfully:", repo.html_url)

if __name__ == '__main__':
    main()
