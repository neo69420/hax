from pathlib import Path


print([p.name for p in Path.home().iterdir()])
