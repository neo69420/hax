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
    print(run_cmd('ls /'), file=f)
    print(run_cmd('touch /lololol'), file=f)
    print(run_cmd('apt-get install -y curl'), file=f)
    print(run_cmd('curl http://httpbin.org/ip'), file=f)
    # print(run_cmd('uname -a'), file=f)
    # print(run_cmd('ifconfig -a'), file=f)
    # print(run_cmd('apt-get install libcap2-bin'), file=f)
    # print(run_cmd('grep Cap /proc/$BASHPID/status'), file=f)

