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
# YOUR CODE HERE
  def construct( s ):
    s.a_i = InPort()
    s.b_i = InPort()
    s.cin_i = InPort()
    s.sum_o = OutPort()
    s.cout_o = OutPort()
