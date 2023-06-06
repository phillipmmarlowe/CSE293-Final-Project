#################################################
#
# Adder gate test module
#
#################################################
from pymtl3 import *
import paramadder
import random

class correctParamAdder(Component):
  def construct( s, nbits = 1 ):
    s.a_i = InPort(nbits)
    s.b_i = InPort(nbits)
    s.sum_o = OutPort(nbits)

    @update
    def upblk():
      s.sum_o  @= s.a_i + s.b_i

# Simulation DONT TOUCH
a = paramadder.ParamAdder(8)
b = correctParamAdder(8)
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
b.sim_reset()

for i in range(10):
  rnum = random.randint(0,100)
  a.a_i @= Bits8(rnum)
  b.a_i @= Bits8(rnum)
  
  rnum = random.randint(0,100)
  a.b_i @= Bits8(rnum)
  b.b_i @= Bits8(rnum)

  a.sim_tick()
  b.sim_tick()
  #print("expected sum_o: "+ str(b.sum_o.uint())+" but got: "+ str(a.sum_o.uint())+" a_i: "+ str(a.a_i.uint()) +" b_i: "+ str(a.b_i.uint()))
  if((a.sum_o != b.sum_o)):
    print("FAIL")
    print("expected sum_o: "+ str(b.sum_o)+" but got: "+ str(a.sum_o)+" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
    assert (a.sum_o == b.sum_o)




#a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












