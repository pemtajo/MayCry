#!/usr/bin/python
# coding=utf-8
# Desenvolvimento Aberto
# TestParticipante.py


import sys
sys.path.append("../..")

import unittest
from classes import Text

__author__='pmdragon'

class Tests(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestText(unittest.TestCase):

    def test_addBlocks(self):
        text=Text()
        text.addBlock('PEDRO')
        text.addBlock('TESTE')
        self.assertEquals(text.blocks, ['PEDRO', 'TESTE'])
        self.assertEquals(str(text), 'PEDROTESTE|')
        




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
