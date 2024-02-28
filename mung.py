import argparse
import os
import re


def normalize(s):
    return re.sub(r"[^_\-.\w]", "_", s)


def mung(key, ref):
    key = normalize(key)
    ref = normalize(ref)
    return f"{key}-{ref}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="stash_name")
    parser.add_argument("-k", "--key", default="stash_key")
    parser.add_argument("-r", "--ref", default="ref_name")
    args = parser.parse_args()

    ref = os.environ[args.ref]
    key = os.environ[args.key]
    name = mung(key, ref)

    print(f"::debug::Creating output {args.output}={name} ")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f'{args.output}={name}' + '\n')
