# View importers that python uses when you run an import statement.
import os
import sys
for importer in sys.meta_path:
    print(repr(importer))

