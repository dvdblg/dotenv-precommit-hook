import argparse
from .create_template import create_template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--template-extension',
        default='.template',
        help='The template file extension',
    )
    parser.add_argument(
        '--also-comment',
        action='store_true',
        help='Also comment out the variable names',
    )
    parser.add_argument('env_files', nargs='*', help='Env files to read from')
    args = parser.parse_args()
    for filename in args.env_files:
        create_template(
            env_file=filename,
            template_extension=args.template_extension,
            also_comment=args.also_comment,
        )

if __name__ == '__main__':
    raise SystemExit(main())