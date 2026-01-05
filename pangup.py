import argparse

import pangu


def cli():
    parser = argparse.ArgumentParser(
        description='Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).'
    )
    parser.add_argument('files', nargs='+', help='Files to be processed')
    args = parser.parse_args()

    for filepath in args.files:
        content = pangu.spacing_file(filepath)
        with open(filepath, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    cli()
