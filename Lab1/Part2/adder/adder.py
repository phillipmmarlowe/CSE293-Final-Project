#################################################
#
# Adder module
#
# Create an adder module
#
#################################################

from pymtl3 import *

# Module definition 
class Adder(Component):
  def construct( s ):
    s.a_i = InPort()
    s.b_i = InPort()
    s.cin_i = InPort()
    s.sum_o = OutPort()
    s.cout_o = OutPort()

    @update
    def upblk():
      s.sum_o  @= s.cin_i ^ s.a_i ^ s.b_i
      s.cout_o @= ( ( s.a_i ^ s.b_i ) & s.cin_i ) | ( s.a_i & s.b_i )
