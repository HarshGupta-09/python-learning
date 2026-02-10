from pathlib import Path

p = Path('inbuild')

print(p.exists())
print(p.is_file())

pp = Path("./in-build-Modules").mkdir()
