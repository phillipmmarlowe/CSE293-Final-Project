#################################################
#
# Counter module
#
# Create a counter module
#
#################################################

from pymtl3 import *

# Module definition 
class Counter(Component):
# YOUR CODE HERE
  def construct( s, nbits = 1 ):
    s.up_i = InPort()
    s.down_i = InPort()
    s.count_o = OutPort(nbits)
    s.next_w = Wire(nbits)

    @update_ff
    # YOUR CODE HERE
    # Use <<= for sequential assignment
    def countblk():
        
    @update
    # YOUR CODE HERE
    def updateblk():
