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
# YOUR CODE HERE
  def construct( s, nbits = 1 ):
    s.a_i = InPort(nbits)
    s.b_i = InPort(nbits)
    s.sum_o = OutPort(nbits)
