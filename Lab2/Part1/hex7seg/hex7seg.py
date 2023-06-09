#################################################
#
# Hex7Seg module
#
# Create a hex7seg module
# You can leave the dp off
#################################################

from pymtl3 import *

# Module definition 
class Hex7seg(Component):
# YOUR CODE HERE
  def construct( s ):
    s.in_i = InPort(4)
    s.out_o = OutPort(8)

        
        
