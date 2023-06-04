#################################################
#
# Xor gate module
#
# Create a module to xor the 
# two inputs a and b together
# to produce the output c
#
#################################################

from pymtl3 import *

# Module definition 
class Xor2(Component):
  def construct(s):
    s.a_i = InPort()
    s.b_i = InPort()
    s.c_o = OutPort()

    @update
    def xorblk():
      # YOUR CODE START
      s.c_o @= s.a_i ^ s.b_i
      # YOUR CODE END


