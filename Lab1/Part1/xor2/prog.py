#################################################
#
# Xor2 prog
#
#################################################
from pymtl3 import *
from pymtl3.passes.backends.verilog import *
import os
import xor2

a = xor2.Xor2()
a.set_metadata(VerilogTranslationPass.enable, True)
a.apply(VerilogTranslationPass())

os.system("mv Xor2_noparam__pickled.v xor2.sv")
os.system("make prog")











