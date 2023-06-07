#################################################
#
# Counter test module
#
#################################################
from pymtl3 import *
import konami
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
a = konami.Konami()
#b = correctParamAdder(8)
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
#b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
#b.sim_reset()

a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)
    
a.up_i @= 1
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)
    
a.up_i @= 1
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 1
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 1
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 0
a.left_i @= 1
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 1
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 0
a.left_i @= 1
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 1
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 1
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)


a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 1
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)


a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 1

a.sim_tick()
if((a.code_o != 1)):
    print("FAIL")
    print("expected code_o: "+ str(1) +" but got: "+ str(a.code_o))
    assert (a.code_o == 1)
'''
a.up_i @= 0
a.down_i @= 0
a.left_i @= 0
a.right_i @= 0
a.a_i @= 0
a.b_i @= 0
a.start_i @= 0

a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)
'''
a.start_i @= 0
a.reset_i @= 1
a.sim_tick()
if((a.code_o != 0)):
    print("FAIL")
    print("expected code_o: "+ str(0) +" but got: "+ str(a.code_o))
    assert (a.code_o == 0)

#a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












