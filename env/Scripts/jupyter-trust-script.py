
# -*- coding: utf-8 -*-
import re
import sys

from nbformat.sign import TrustNotebookApp

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(TrustNotebookApp.launch_instance())
