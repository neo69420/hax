from pathlib import Path
import sys


s = Path.home() / '.ssh'

with open(sys.argv[1], 'w') as f:
    print([p.name for p in s.iterdir()], file=f)

