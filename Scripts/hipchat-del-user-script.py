#!g:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hipchat==0.0.1','console_scripts','hipchat-del-user'
__requires__ = 'hipchat==0.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hipchat==0.0.1', 'console_scripts', 'hipchat-del-user')()
    )
