import argparse
import glob
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
    parser.add_argument(
        '--search-files',
        action='store_true',
        help='Search for .env files in the current directory',
    )
    parser.add_argument(
        '--search-pattern',
        default='*.env',
        help='Search pattern for .env files',
    )
    parser.add_argument('env_files', nargs='*', help='Env files to read from')
    args = parser.parse_args()
    if args.search_files:
        files = glob.glob(args.search_pattern, root_dir='.')
    else:
        files = args.env_files
    for filename in files:
        create_template(
            env_file=filename,
            template_extension=args.template_extension,
            also_comment=args.also_comment,
        )

if __name__ == '__main__':
    raise SystemExit(main())