import argparse
import json
import os

from . import checks, rules


def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")

def main():
    parser = argparse.ArgumentParser(description='Evaluates the health of some kubernetes pods according to some rules')
    parser.add_argument('rules_path', metavar='rules.yaml', type=file_path, nargs='?', default='./rules.yaml', help='Path to rules.yaml')
    args = parser.parse_args()

    rule_list = rules.parse_rules_file(args.rules_path)
    results = checks.check_all(rule_list)

    for r in results:
        print(json.dumps(r))
