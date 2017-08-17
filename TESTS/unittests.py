#!/usr/bin/python
# coding=utf-8
# Desenvolvimento Aberto
# TestParticipante.py


import sys
sys.path.append("../")

from unittest import TestCase
import unittest
from lib import Text
from lib import PlainText
from lib import CypherText
from lib import Crypto

__author__='pmdragon'


class TestText(unittest.TestCase):

    def test_addBlocks(self):
        text=Text()
        text.addBlock('PEDRO')
        text.addBlock('TESTE')
        self.assertEquals(text.getBlocks(), ['PEDRO', 'TESTE'])
        self.assertEquals(str(text), 'PEDROTESTE|')
        
    
class TestPlainText(unittest.TestCase):
    
    def test_addBlocks(self):
        text=PlainText()
        text.addBlock('PEDRO')
        text.addBlock('TESTE')
        self.assertEquals(text.getBlocks(), ['PEDRO', 'TESTE'])
        self.assertEquals(str(text), 'PEDROTESTE|')

    def test_newPlaintText(self):
        text=PlainText()
        self.assertEquals(text.getBlocks(), [])
        self.assertEquals(str(text), '|')

    def test_newPlaintText2(self):
        text=PlainText("TESTE", 16)
        self.assertEquals(text.getBlocks(), ['TESTE           '])
        self.assertEquals(str(text), 'TESTE           |')

    def test_newPlaintText3(self):
        text=PlainText("TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST", 16)
        self.assertEquals(text.getBlocks(), ['TESTTESTTESTTEST', 'TESTTESTTESTTEST', 'TESTTESTTESTTEST','TESTTESTTESTTEST', 'TEST            '])
        self.assertEquals(str(text), 'TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST            |')

class TestCrypherText(unittest.TestCase):
    def test_addBlocks(self):
        text=CypherText()
        text.addBlock('PEDRO')
        text.addBlock('TESTE')
        self.assertEquals(text.getBlocks(), ['PEDRO', 'TESTE'])
        self.assertEquals(str(text), 'PEDROTESTE|')
        
class TestCrypto(unittest.TestCase):
    
    def test_newCrypto(self):
        crypto=Crypto('TESTE', 'TEST')
        self.assertEquals(str(crypto),
         'PlainText:  TESTE           |\nCypherText: \xad\xe3\x8a\xc0o\t\xa0\xb4-\xe1\x08\xe4\x9d\xb8C\xb6|\nDecrytText: TESTE           |')

    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
