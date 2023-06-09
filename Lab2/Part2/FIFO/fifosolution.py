#################################################
#
# Fifo module
#
# Create a Fifo module
#
#################################################

from pymtl3 import *

# Module definition 
class Fifo(Component):
# YOUR CODE HERE
  def construct( s, nbits ):
    s.in_i = InPort(nbits)
    s.out_o = OutPort(nbits)
    s.data = []
    '''
    for x in range(length):
      s.data.append(0)
    '''
    #s.countin = 0
    s.countout = 0

    @update_ff
    # YOUR CODE HERE
    # Use <<= for sequential assignment
    def ffblk():
      s.out_o <<= s.data[s.countout]
      s.countout <<= s.countout + 1
        
    @update
    # YOUR CODE HERE
    def updateblk():
      s.data.append(s.in_i)
      #s.countin = s.countin + 1
