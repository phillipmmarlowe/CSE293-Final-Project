#################################################
#
# And gate test module
#
#################################################
from pymtl3 import *
import xor2

# Simulation DONT TOUCH
a = xor2.Xor2()
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
a.a_i @= 0
a.b_i @= 0
a.sim_tick()

if(a.c_o != 0):
  print("FAIL")
  print("expected c_o: "+ str(0) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == 0

a.a_i @= 0
a.b_i @= 1
a.sim_tick()

if(a.c_o != 1):
  print("FAIL")
  print("expected c_o: "+ str(1) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == 1

a.a_i @= 1
a.b_i @= 0
a.sim_tick()

if(a.c_o != 1):
  print("FAIL")
  print("expected c_o: "+ str(1) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == 1

a.a_i @= 1
a.b_i @= 1
a.sim_tick()

if(a.c_o != 0):
  print("FAIL")
  print("expected c_o: "+ str(0) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == 0

a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












