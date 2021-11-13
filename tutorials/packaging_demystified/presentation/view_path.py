# View PYTHON PATH.
import os
import sys
for path in sys.path:
    print(repr(path))

# When using virtualenv you get built-ins and the standard library in the PYTHON PATH.
# The global site-packages are replaced by the virtualenv's own site-packages.
