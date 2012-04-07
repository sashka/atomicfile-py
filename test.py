#!/usr/bin/env python
# encoding: utf-8
from __future__ import with_statement
import os
import unittest

from atomicfile import AtomicFile


def create_test_file(filename):
    f = open(filename, 'w')
    f.write('test\n')
    f.close()


class AtomicFileTest(unittest.TestCase):

    def setUp(self):
        self.filename = 'test-atomicfile.txt'

    def test_write(self):
        create_test_file(self.filename)
        af = AtomicFile(self.filename)
        expected = "this is written by AtomicFile.\n"
        af.write(expected)
        af.close()
        result = open(self.filename, 'r').read()
        try:
            self.assertEqual(result, expected)
        finally:
            os.remove(self.filename)

    def test_close(self):
        af = AtomicFile(self.filename)
        af.write('test\n')
        af.close()
        try:
            af.write('test again\n')
            self.fail('ValueError not raised')
        except ValueError:
            pass
        finally:
            os.remove(self.filename)

    def test_with(self):
        data = "this is written by AtomicFile.\n"

        with AtomicFile(self.filename) as f:
            f.write(data)

        try:
            f.write(data)
            self.fail("'ValueError: I/O operation on closed file' not raised")
        except ValueError:
            pass
        finally:
            os.remove(self.filename)


if __name__ == '__main__':
    unittest.main()
