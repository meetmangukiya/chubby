"""
GitHub utilities in your terminal.
"""

import os

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()
