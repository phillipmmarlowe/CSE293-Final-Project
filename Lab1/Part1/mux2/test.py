#################################################
#
# Mux gate test module
#
#################################################
from pymtl3 import *
import mux2

class correctMux2(Component):
  def construct(s):
    s.a_i = InPort()
    s.b_i = InPort()
    s.s_i = InPort()
    s.c_o = OutPort()

    @update
    def andblk():
      s.c_o @= (s.a_i & s.s_i) | (s.b_i & ~s.s_i)


# Simulation DONT TOUCH
a = mux2.Mux2()
b = correctMux2()
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
b.sim_reset()

a.a_i @= 0
a.b_i @= 0
a.s_i @= 0

b.a_i @= 0
b.b_i @= 0
b.s_i @= 0
a.sim_tick()
b.sim_tick()

if(a.c_o != b.c_o):
  print("FAIL")
  print("expected c_o: "+ str(b.c_o) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == b.c_o

a.a_i @= 0
a.b_i @= 1
a.s_i @= 0

b.a_i @= 0
b.b_i @= 1
b.s_i @= 0
a.sim_tick()
b.sim_tick()

if(a.c_o != b.c_o):
  print("FAIL")
  print("expected c_o: "+ str(b.c_o) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == b.c_o

a.a_i @= 0
a.b_i @= 1
a.s_i @= 1

b.a_i @= 0
b.b_i @= 1
b.s_i @= 1
a.sim_tick()
b.sim_tick()

if(a.c_o != b.c_o):
  print("FAIL")
  print("expected c_o: "+ str(b.c_o) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == b.c_o

a.a_i @= 1
a.b_i @= 1
a.s_i @= 1

b.a_i @= 1
b.b_i @= 1
b.s_i @= 1
a.sim_tick()
b.sim_tick()

if(a.c_o != b.c_o):
  print("FAIL")
  print("expected c_o: "+ str(b.c_o) +" but got: "+ str(a.c_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert a.c_o == b.c_o

a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












