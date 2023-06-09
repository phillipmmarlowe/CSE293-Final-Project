#################################################
#
# And gate module
#
# Create a module to and the 
# two inputs a and b together
# to produce the output c
#
#################################################

from pymtl3 import *

# Module definition 
class And2(Component):
  def construct(s):
    s.a_i = InPort()
    s.b_i = InPort()
    s.c_o = OutPort()

    @update
    def andblk():
      # YOUR CODE START


