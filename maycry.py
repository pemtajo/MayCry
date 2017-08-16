#!/usr/bin/python

#using pycrypto
#script for encrypt

#

# ideua
# an mode ransom
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from optparse import OptionParser
from classes import Crypto

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


try:
   arquivo = open(filename,"r+b")
   tamanho = arquivo.tell()

   print(arquivo)
   crypto = Crypto(filename, password)
except IOError:
   crypto= Crypto(filename, password)




print(crypto)
