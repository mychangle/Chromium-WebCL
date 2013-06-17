#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys


def main():
  print 'symlink: touches link_outside_build_root/'
  assert len(sys.argv) == 1

  if 'asdf\n' != open(
      os.path.join('link_outside_build_root', 'test_file3.txt'), 'rb').read():
    print 'Failed'
    return 1
  return 0


if __name__ == '__main__':
  sys.exit(main())
