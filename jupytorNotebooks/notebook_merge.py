import io
import os
import sys

from IPython import nbformat

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    print(nbformat.writes(merged))

if __name__ == '__main__':
    notebooks = ['00.TableOfContets.ipynb', '01.print and help.ipynb',
                 '02.arithmetic calculation.ipynb', '03.data-types.ipynb']
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
        
    merge_notebooks(notebooks)
