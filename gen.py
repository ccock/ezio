#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os
import shlex
import subprocess

from distutils.util import strtobool
from os import path

PROJECT_ROOT = path.dirname(path.abspath(__file__))
CMAKE_ROOT = path.dirname(path.abspath(__file__))

def run(cmd):
    subprocess.call(shlex.split(cmd))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-type', dest='build_type', type=str, default='Debug')
    parser.add_argument('--build-test', dest='build_test',
                        type=lambda opt: bool(strtobool(opt)), default=True)
    args = parser.parse_args()

    build_type = args.build_type.capitalize()

    out_dir = path.join(PROJECT_ROOT, 'build', build_type)
    if not path.exists(out_dir):
        os.makedirs(out_dir)

    os.chdir(out_dir)

    no_build_unittest = not args.build_test

    run('cmake'
        ' -DCMAKE_BUILD_TYPE={}'
        ' -DCMAKE_BUILD_NO_UNITTEST={}'
        ' -G "Ninja" {}'
        .format(build_type, no_build_unittest, CMAKE_ROOT))

    run('cmake'
        ' --build {}'
        ' -- -j 4'
        .format(out_dir))


if __name__ == '__main__':
    main()
