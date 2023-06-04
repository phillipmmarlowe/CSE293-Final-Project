#################################################
#
# Adder gate test module
#
#################################################
from pymtl3 import *
import adder

class correctAdder(Component):
  def construct( s ):
    s.a_i = InPort()
    s.b_i = InPort()
    s.cin_i = InPort()
    s.sum_o = OutPort()
    s.cout_o = OutPort()

    @update
    def upblk():
      s.sum_o  @= s.cin_i ^ s.a_i ^ s.b_i
      s.cout_o @= ( ( s.a_i ^ s.b_i ) & s.cin_i ) | ( s.a_i & s.b_i )


# Simulation DONT TOUCH
a = adder.Adder()
b = correctAdder()
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
b.sim_reset()

a.a_i @= 0
a.b_i @= 0
a.cin_i @= 0


b.a_i @= 0
b.b_i @= 0
b.cin_i @= 0

a.sim_tick()
b.sim_tick()

if((a.sum_o != b.sum_o) | (a.cout_o != b.cout_o)):
  print("FAIL")
  print("expected sum_o, cout_o: "+ str(b.sum_o)+ ", "+ str(b.cout_o) +" but got: "+ str(a.sum_o)+ ", "+ str(a.cout_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert (a.sum_o == b.sum_o) & (a.cout_o == b.cout_o)



a.a_i @= 0
a.b_i @= 1
a.cin_i @= 0


b.a_i @= 0
b.b_i @= 1
b.cin_i @= 0

a.sim_tick()
b.sim_tick()

if((a.sum_o != b.sum_o) | (a.cout_o != b.cout_o)):
  print("FAIL")
  print("expected sum_o, cout_o: "+ str(b.sum_o)+ ", "+ str(b.cout_o) +" but got: "+ str(a.sum_o)+ ", "+ str(a.cout_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert (a.sum_o == b.sum_o) & (a.cout_o == b.cout_o)


a.a_i @= 0
a.b_i @= 1
a.cin_i @= 1


b.a_i @= 0
b.b_i @= 1
b.cin_i @= 1

a.sim_tick()
b.sim_tick()

if((a.sum_o != b.sum_o) | (a.cout_o != b.cout_o)):
  print("FAIL")
  print("expected sum_o, cout_o: "+ str(b.sum_o)+ ", "+ str(b.cout_o) +" but got: "+ str(a.sum_o)+ ", "+ str(a.cout_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert (a.sum_o == b.sum_o) & (a.cout_o == b.cout_o)
  
  
a.a_i @= 1
a.b_i @= 1
a.cin_i @= 0


b.a_i @= 1
b.b_i @= 1
b.cin_i @= 0

a.sim_tick()
b.sim_tick()

if((a.sum_o != b.sum_o) | (a.cout_o != b.cout_o)):
  print("FAIL")
  print("expected sum_o, cout_o: "+ str(b.sum_o)+ ", "+ str(b.cout_o) +" but got: "+ str(a.sum_o)+ ", "+ str(a.cout_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert (a.sum_o == b.sum_o) & (a.cout_o == b.cout_o)


a.a_i @= 1
a.b_i @= 1
a.cin_i @= 1


b.a_i @= 1
b.b_i @= 1
b.cin_i @= 1

a.sim_tick()
b.sim_tick()

if((a.sum_o != b.sum_o) | (a.cout_o != b.cout_o)):
  print("FAIL")
  print("expected sum_o, cout_o: "+ str(b.sum_o)+ ", "+ str(b.cout_o) +" but got: "+ str(a.sum_o)+ ", "+ str(a.cout_o) +" a_i: "+ str(a.a_i) +" b_i: "+ str(a.b_i))
  assert (a.sum_o == b.sum_o) & (a.cout_o == b.cout_o)

#a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












