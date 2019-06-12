#!/usr/bin/env python
#
# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Builds GCC for Android."""
from __future__ import print_function

import os
import site

site.addsitedir(os.path.join(os.path.dirname(__file__), '../../ndk/build/lib'))
site.addsitedir(os.path.join(os.path.dirname(__file__), '../../ndk'))

# pylint: disable=import-error,wrong-import-position
import build_support
# pylint: enable=import-error,wrong-import-position


class ArgParser(build_support.ArgParser):
    def __init__(self):
        super(ArgParser, self).__init__()

        self.add_argument(
            '--toolchain', choices=build_support.ALL_TOOLCHAINS,
            help='Toolchain to build. Builds all if not present.')


def main(args):
    GCC_VERSION = '4.9'

    toolchains = build_support.ALL_TOOLCHAINS
    if args.toolchain is not None:
        toolchains = [args.toolchain]

    print(f'Building {args.host.value} toolchains: {" ".join(toolchains)}')
    for toolchain in toolchains:
        toolchain_name = '-'.join([toolchain, GCC_VERSION])
        sysroot_arg = '--sysroot={}'.format(
            build_support.sysroot_path(toolchain))
        build_cmd = [
            'bash',
            'build-gcc.sh',
            build_support.toolchain_path(),
            build_support.ndk_path(),
            toolchain_name,
            build_support.jobs_arg(),
            sysroot_arg,
            '--try-64',
        ]

        if args.host.is_windows:
            build_cmd.append('--mingw')

        build_support.build(build_cmd, args)

if __name__ == '__main__':
    build_support.run(main, ArgParser)
