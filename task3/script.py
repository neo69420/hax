from pathlib import Path
import sys
import subprocess
from subprocess import run


def run_cmd(*args):
    ret = run(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = ret.stdout.decode('utf-8')
    err = ret.stderr.decode('utf-8')

    return f'out:\n{out}\nerr:\n{err}\n'


with open(sys.argv[1], 'w') as f:
    print(run_cmd('uname -a'), file=f)
    print(run_cmd('ip addr show'), file=f)
    print(run_cmd('echo $USER'), file=f)

