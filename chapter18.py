# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:40:25 2020

@author: trimurti
"""

#<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>

import sys
import re

def extract_name(filename):
    names = []
    f = open(filename, 'r')
    text = f.read()
    groups = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for group in groups:
        print(group[0], group[1], group[2])

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print('file 명을 입력하시요')
        sys.exit(1)

    filename = './babynames/' + args[0]
    extract_name(filename)