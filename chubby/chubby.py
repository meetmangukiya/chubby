from chubby.argparser import parser
import chubby.chulib as chulib

args = parser.parse_args()

def main():
    try:
        if args.config:
            chulib.save_to_config(args.config)
    except:
        pass
