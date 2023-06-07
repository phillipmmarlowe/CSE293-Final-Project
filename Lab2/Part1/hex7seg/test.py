#################################################
#
# Adder gate test module
#
#################################################
from pymtl3 import *
import hex7seg


class goodHex7seg(Component):
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



# Simulation DONT TOUCH
a = hex7seg.Hex7seg()
b = goodHex7seg()
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
b.sim_reset()
for num in range(16):
  a.in_i @= num
  b.in_i @= num
  a.sim_tick()
  b.sim_tick()
  assert b.out_o == a.out_o
  #print("Out: "+str(a.out_o))
'''
if((a.out_o != 0)):
    print("FAIL")
    print("expected count_o: "+ str(0) +" but got: "+ str(a.count_o))#+ " at cycle: " + str(0)
    assert (a.count_o == 0)
'''



#a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












