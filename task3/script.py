from pathlib import Path
import sys


with open(sys.argv[1], 'w') as f:
    print([p.name for p in Path.home().iterdir()], file=f)

