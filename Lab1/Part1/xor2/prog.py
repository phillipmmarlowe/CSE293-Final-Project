#################################################
#
# Xor2 prog
#
#################################################
from pymtl3 import *
from pymtl3.passes.backends.verilog import *
import xor2

a = xor2.Xor2()
a.set_metadata(VerilogTranslationPass.enable, True)
a.apply(VerilogTranslationPass())












