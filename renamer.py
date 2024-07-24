# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

# Just modify the code if you need it

import subprocess
import pathlib

# Run every element <<file>> of one directory and renames it
# 000 + number:
# 0005.png for example or 0040.jpg
for index, element in enumerate(pathlib.PosixPath("./Art digital").iterdir(), 1):
    
    # Ignores every file with extension .py and directories
    if element.suffix == ".py":
        continue
    
    # Renames file using UNIX command
    subprocess.check_call(["mv", f"{ element }", f"{ '0' * (4 - len(str(index)) ) + f'{ index }'  }{ element.suffix }" ])
