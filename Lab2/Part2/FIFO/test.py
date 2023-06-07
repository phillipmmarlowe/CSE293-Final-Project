#################################################
#
# Fifo test module
#
#################################################
from pymtl3 import *
import fifo
#import random

# Simulation DONT TOUCH
a = fifo.Fifo(8)
#b = correctParamAdder(8)
a.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
#b.apply(DefaultPassGroup(textwave=True,vcdwave='testsim'))
a.sim_reset()
#b.sim_reset()

for n in range(1,10):
  a.in_i @= n
  a.sim_tick()
  if((0 != 0)):
    print("FAIL")
    print("expected out_o: "+ str(n-1) +" but got: "+ str(a.out_o))
    assert (n-1 == a.out_o)

a.sim_tick()
a.sim_tick()
a.sim_tick()
a.sim_tick()

a.print_textwave()
print("-----------------------------------------------------------")
print("PASS")
print("-----------------------------------------------------------")












