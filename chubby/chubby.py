from .argparser import parser
import .chulib

args = parser.parse_args()

if args.config:
    chulib.save_to_config(args.config)
