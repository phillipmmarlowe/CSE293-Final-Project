#################################################
#
# Counter test module
#
#################################################
from pymtl3 import *
import counter
#import random
'''
class correctParamAdder(Component):
  def construct( s, nbits = 1 ):
    s.a_i = InPort(nbits)
    s.b_i = InPort(nbits)
    s.sum_o = OutPort(nbits)

    @update
    def upblk():
      s.sum_o  @= s.a_i + s.b_i
'''
# Simulation DONT TOUCH
a = counter.Counter(8)
#b = correctParamAdder(8)
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
#b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
#b.sim_reset()

a.up_i @= 0
a.down_i @= 0
a.sim_tick()
if((a.count_o != 0)):
    print("FAIL")
    print("expected count_o: "+ str(0) +" but got: "+ str(a.count_o))#+ " at cycle: " + str(0)
    assert (a.count_o == 0)
a.sim_tick()
if((a.count_o != 0)):
    print("FAIL")
    print("expected count_o: "+ str(0) +" but got: "+ str(a.count_o))#+ " at cycle: " + str(1)
    assert (a.count_o == 0)


a.up_i @= 1
a.down_i @= 0
for i in range(1,4):
  a.sim_tick()
  if((a.count_o.int() != i)):
    print("FAIL")
    print("expected count_o: "+ str(i) +" but got: "+ str(a.count_o.int()))#+ " at cycle: " + str(i)
    assert (a.count_o.int() == i)
a.up_i @= 0
a.down_i @= 1
for i in range(1,7):
  a.sim_tick()
  print("expected count_o: "+ str(3-i) +" but got: "+ str(a.count_o.int()))#+ " at cycle: " + str(i)
  if((a.count_o.int() != 3-i)):
    print("FAIL")
    print("expected count_o: "+ str(3-i) +" but got: "+ str(a.count_o.int()))#+ " at cycle: " + str(i)
    assert (a.count_o.int() == 3-i)



#a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












