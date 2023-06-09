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
    
    s.table = [
      0b0111111,
      0b0000110,
      0b1011011,
      0b1001111,
      0b1100110,
      0b1101101,
      0b1111101,
      0b0000111,
      0b1111111,
      0b1101111,
      0b1110111,
      0b1111100,
      0b0111001,
      0b1011110,
      0b1111001,
      0b1110001
    ]
    
    @update
    # YOUR CODE HERE
    def updateblk():
        s.out_o @= ~s.table[s.in_i]
