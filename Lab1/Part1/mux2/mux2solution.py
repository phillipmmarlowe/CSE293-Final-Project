#################################################
#
# Mux module
#
# Create a module to test mux
#
#################################################

from pymtl3 import *

# Module definition 
class Mux2(Component):
  def construct(s):
    s.a_i = InPort()
    s.b_i = InPort()
    s.s_i = InPort()
    s.c_o = OutPort()

    @update
    def andblk():
      # YOUR CODE START
      s.c_o @= (s.a_i & s.s_i) | (s.b_i & ~s.s_i)
      # YOUR CODE END


