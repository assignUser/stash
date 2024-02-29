import os
import re


def normalize(s):
    return re.sub(r"[^_\-.\w]", "_", s)


def mung(key, ref):
    key = normalize(key)
    ref = normalize(ref)
    return f"{key}-{ref}"


def output_munged_name(ref = "ref_name", key = "stash_key", output = "stash_name"):
    ref = os.environ[ref]
    key = os.environ[key]
    name = mung(key, ref)

    print(f"::debug::Creating output {output}={name} ")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f'{output}={name}' + '\n')
