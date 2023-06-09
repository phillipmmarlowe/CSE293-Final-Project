#################################################
#
# Konami module
#
# Create a Konami StateMachine module
#
# Code: U U D D L R L R B A S
#################################################

from pymtl3 import *

# Module definition 
class Konami(Component):
  def construct( s ):
    s.reset_i = InPort()
    s.up_i = InPort()
    s.down_i = InPort()
    s.left_i = InPort()
    s.right_i = InPort()
    s.a_i = InPort()
    s.b_i = InPort()
    s.start_i = InPort()
    s.code_o = OutPort()
    
    @update
    # YOUR CODE HERE
    
    @update_ff
      
        
        
        
        
        
        
        
        
        
        
        
        
        
