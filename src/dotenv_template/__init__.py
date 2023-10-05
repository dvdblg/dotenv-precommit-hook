import argparse
from .create_template import create_template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--env-file',
        default='.env',
        help='The .env file to read from',
    )
    parser.add_argument(
        '--env-template-file',
        default='.env.template',
        help='The template file to write to',
    )
    parser.add_argument(
        '--also-comment',
        action='store_true',
        help='Also comment out the variable names',
    )
    args = parser.parse_args()

    create_template(
        env_file=args.env_file,
        env_template_file=args.env_template_file,
        also_comment=args.also_comment,
    )

if __name__ == '__main__':
    main()