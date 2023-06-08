#################################################
#
# Xor2 prog
#
#################################################
from pymtl3 import *
from pymtl3.passes.backends.verilog import *
import os
import counter

a = counter.Counter(3)
a.set_metadata(VerilogTranslationPass.enable, True)
a.apply(VerilogTranslationPass())

b = counter.Counter(22)
b.set_metadata(VerilogTranslationPass.enable, True)
b.apply(VerilogTranslationPass())

os.system("mv Counter__nbits_3__pickled.v counter.sv")
os.system("mv Counter__nbits_22__pickled.v counter22.sv")
os.system("make prog")











