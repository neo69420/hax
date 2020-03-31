from pathlib import Path
import sys
import subprocess
from subprocess import run
import time
import requests


def post_text(title, author, author_url, text, save_hash, cookie_uuid, page_id):
    # title > 2
    # text encoded < 65536
    # save hash or empty
    api_url = 'https://edit.graph.org/save'
    long_name = '---------------------------TelegraPhBoundary21'

    headers = {
        'Content-Type': f'multipart/form-data; boundary={long_name}',
        'Host': 'edit.graph.org',
        'Origin': 'https://graph.org',
        'Cookie': f'tph_uuid={cookie_uuid}',
    }

    data = f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="Data";filename="content.html"\r\n' + \
           'Content-type: plain/text\r\n' + \
           '\r\n' + \
           '[{"tag":"p","children":["' + text + '"]}]\r\n' + \
           f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="title"\r\n' + \
           '\r\n' + \
           f'{title}\r\n' + \
           f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="author"\r\n' + \
           '\r\n' + \
           f'{author}\r\n' + \
           f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="author_url"\r\n' + \
           '\r\n' + \
           f'{author_url}\r\n' + \
           f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="save_hash"\r\n' + \
           '\r\n' + \
           f'{save_hash}\r\n' + \
           f'--{long_name}\r\n' + \
           'Content-Disposition: form-data;name="page_id"\r\n' + \
           '\r\n' + \
           f'{page_id}\r\n' + \
           f'--{long_name}--'

    suffix = requests.post(url=api_url, headers=headers, data=data).json()['path']
    return f'https://graph.org/{suffix}'


def upload(title, text):
    return post_text(title, '', '', text,
                    '1c9a345cad33bfc193f6ccd03901e8dc2ad7',
                    'goLcm0a8QsjqAusEjcvMdvVoGArO54nls9vO7DVX6e', 0)


def run_cmd(*args):
    ret = run(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = ret.stdout.decode('utf-8')
    err = ret.stderr.decode('utf-8')

    return f'out:\n{out}\nerr:\n{err}\n'


with open(sys.argv[1], 'w') as f:
    sec = 0

    while True:
        time.sleep(1)
        print(upload('ajkfljsafjiwslfjsiwx', str(sec)), file=f)
        sec += 1

    # print(ip, file=f)
    # print(run_cmd('ls /tmp'), file=f)
    # print(run_cmd('touch /tmp/lololol'), file=f)
    # print(run_cmd('apt-get install -y curl'), file=f)
    # print(run_cmd('curl http://httpbin.org/ip'), file=f)
    # print(run_cmd('uname -a'), file=f)
    # print(run_cmd('ifconfig -a'), file=f)
    # print(run_cmd('apt-get install libcap2-bin'), file=f)
    # print(run_cmd('grep Cap /proc/$BASHPID/status'), file=f)

