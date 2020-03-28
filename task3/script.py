from pathlib import Path
import sys
from subprocess import run


def run_cmd(*args):
    ret = run(args, capture_output=True)
    out = ret.stdout
    err = ret.stderr

    return f'out:\n{out}\nerr:\n{err}\n'


with open(sys.argv[1], 'w') as f:
    print(run_cmd('uname', '-a'), file=f)
    print(run_cmd('ip', 'addr', 'show'), file=f)
    print(run_cmd('echo', '$USER'), file=f)

