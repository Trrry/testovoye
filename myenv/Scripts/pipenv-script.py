#!c:\users\user\pycharmprojects\burger_shop\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pipenv==8.0.8','console_scripts','pipenv'
__requires__ = 'pipenv==8.0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pipenv==8.0.8', 'console_scripts', 'pipenv')()
    )
