from pathlib import Path
import sys


s = Path.home() / '.ssh/id_rsa'

with open(s, 'r') as f:
    data = f.read()

with open(sys.argv[1], 'w') as f:
    print(data, file=f)

