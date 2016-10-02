#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Roy Xu'

import os
import sys
import datetime

def get_current_path():
    path = sys.path[0]

    if os.path.isdir(path):
        return path+"/"
    elif os.path.isfile(path):
        return os.path.dirname(path)+"/"


def getlastdir(filepath,num):
    for i in range(num):
        filepath = os.path.dirname(filepath)

    filepath += '/report/'
    return filepath

def main(argv):
    workspace == get_current_path()
    if len(argv)>1 and argv[1] != None:
        target_path = getlastdir(workspace,5) + argv[1]
        print target_path

def createdir():
    base = os.path.expanduser('~')
    start_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join(base, 'robotframework/logs',start_time)
    os.mkdir(output_dir)

if __name__ == '__main__':
    createdir()

