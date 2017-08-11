#!/usr/bin/python

#using pycrypto
#script for encrypt

#

# ideua
# an mode ransom
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from optparse import OptionParser

import sys
sys.path.append("../..")


parser = OptionParser("usage: %prog [options] inputfile password")
parser.add_option("-i", "--input", dest="filename",
                       default="all", type="string",
                       help="specify filename to encrypt")
parser.add_option("-p", "--password", dest="password", help="password for lock the arquive")
parser.add_option("-d", "--decrypt",action="store_false", dest="encrypt", default=True, help="Option for encrypt the filename (is true for default)")
parser.add_option("-e", "--encrypt", action="store_true", dest="encrypt", help="Option for decrypt the filename")

(options, args) = parser.parse_args()
if len(args) != 2:
    parser.error("incorrect number of arguments")
    raise SystemExit

filename = args[0]
password = args[1]

print(options)
print(args)


charUseless=' ' #blank space

class Text(object):
    """docstring for Text."""
    _blocks=[]
    def __init__(self):
        super(Text, self).__init__()

    def addBlock(self,block):
        self.blocks.append(block)

    def refresh(self):
        self.blocks=[]

    def __str__(self):
        tmp=""
        for b in self.blocks:
            tmp+=b
        return tmp+"|"

    def __repr__(self):
        return super(self).__repr__

class PlainText(Text):
    """docstring for PlainText."""

    def __init__(self, arg=None, sizeBlock=None):
        super(PlainText, self).__init__()
        if (arg is not None) and (sizeBlock is not None):
            self.arg = arg
            self.sizeBlock=sizeBlock
            self._splitForSizeBlock()
        else:
            self.refresh()

    def _splitForSizeBlock(self):
        self.arg+=(self.sizeBlock-(len(self.arg)%self.sizeBlock))*charUseless
        self.blocks=[self.arg[i: i + self.sizeBlock] for i in range(0, len(self.arg), self.sizeBlock)]


class CypherText(Text):
    """docstring for CypherText."""
    def __init__(self):
        super(CypherText, self).__init__()


class Crypto(object):
    """docstring for Crypto."""
    SIZE_BLOCK=16

    def __init__(self, obj, password):
        super(Crypto, self).__init__()
        self.obj = obj
        self.encrypter= AES.new('This is a key123', AES.MODE_ECB)
        self.plain = PlainText(obj, self.SIZE_BLOCK)
        self.cypher =CypherText()
        self.textDecrypt = PlainText()
        self._encrypt()
        self._decrypt()

    def _encrypt(self):
        self.cypher.refresh()
        for block in self.plain.blocks:
            self.cypher.addBlock(self.encrypter.encrypt(block))

    def _decrypt(self):
        self.textDecrypt.refresh()
        for block in self.cypher.blocks:
            self.textDecrypt.addBlock(self.encrypter.decrypt(block))

    def __str__(self):
        view="PlainText:  "+ str(self.plain)+"\n"
        view+="CypherText: "+ str(self.cypher)+"\n"
        view+="DecrytText: "+ str(self.textDecrypt)

        return view




try:
   arquivo = open(filename,"r+b")
   tamanho = arquivo.tell()

   print(arquivo)
   crypto = Crypto(filename, password)
except IOError:
   crypto= Crypto(filename, password)




print(crypto)
