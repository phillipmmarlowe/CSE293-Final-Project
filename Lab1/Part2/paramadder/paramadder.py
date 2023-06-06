#################################################
#
# Parameterized Adder module
#
# Create an parameterized adder module
#
#################################################

from pymtl3 import *

# Module definition 
class ParamAdder(Component):
  def construct( s, nbits = 1 ):
    s.a_i = InPort(nbits)
    s.b_i = InPort(nbits)
    s.sum_o = OutPort(nbits)

    @update
    def upblk():
      s.sum_o  @= s.a_i + s.b_i
