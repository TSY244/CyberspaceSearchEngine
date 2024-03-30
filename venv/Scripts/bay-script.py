#!d:\code\vsc\django\cyberspacesearchengine\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bay==2.19.0','console_scripts','bay'
__requires__ = 'bay==2.19.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bay==2.19.0', 'console_scripts', 'bay')()
    )
