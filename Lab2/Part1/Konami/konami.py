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
# YOUR CODE HERE
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
    s.cstate = 0
    s.nstate = 0
    '''
    states = [
      0b00000000000,
      0b00000000001,
      0b00000000010,
      0b00000000100,
      0b00000001000,
      0b00000001000
      
    ]
    '''
    @update
    # YOUR CODE HERE
    def updateblk():
      if (s.reset_i):
        s.code_o @= 0
        s.cstate = 0
        s.nstate = 0
      s.cstate = s.nstate
      if ((s.cstate == 0) & s.up_i):
        #print("Entered")
        s.nstate = s.cstate + 1
      elif ((s.cstate == 1) & s.up_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 2) & s.down_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 3) & s.down_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 4) & s.left_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 5) & s.right_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 6) & s.left_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 7) & s.right_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 8) & s.b_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 9) & s.a_i): 
        s.nstate = s.cstate + 1
      elif ((s.cstate == 10) & s.start_i): 
        s.code_o @= 1
        s.nstate = s.cstate + 1
      #else:
        #s.code_o @= 1
        #s.nstate = 0
    '''    
    @update_ff
    def updateff():
      s.cstate <<= s.nstate
      print(s.nstate)
    '''
      
        
        
        
        
        
        
        
        
        
        
        
        
        
