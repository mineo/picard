#!/usr/bin/env python3

import os.path
import sys


# On Windows try to attach to the console as early as possible in order
# to get stdout / stderr logged to console. This needs to happen before
# logging gets imported.
# See https://stackoverflow.com/questions/54536/win32-gui-app-that-writes-usage-text-to-stdout-when-invoked-as-app-exe-help
if sys.platform == "win32":
    from ctypes import windll
    if windll.kernel32.AttachConsole(-1):
        sys.stdout = open('CON', 'w')
        sys.stderr = open('CON', 'w')


from picard.tagger import main
from picard.util import (
    frozen_temp_path,
    is_frozen,
)

sys.path.insert(0, '.')

# This is needed to find resources when using pyinstaller
if is_frozen:
    basedir = frozen_temp_path
else:
    basedir = os.path.dirname(os.path.abspath(__file__))

main(os.path.join(basedir, 'locale'), True)
