// Top-level design file for the icebreaker FPGA board
//
// Wi23, Lab 1
module top
  (input [0:0] clk_12mhz_i
  ,input [0:0] reset_n_async_unsafe_i
   // n: Negative Polarity (0 when pressed, 1 otherwise)
   // async: Not synchronized to clock
   // unsafe: Not De-Bounced
  ,input [3:1] button_async_unsafe_i
   // async: Not synchronized to clock
   // unsafe: Not De-Bounced
  ,output [5:1] led_o);

  // For this lab, instantiate your xor2 gate. Using two wires from
  // btn_async_unsafe_i, drive an output wire in led_o.
  //
  // Your code goes here
  
  wire [21:0] newclk_w;
  
  Counter__nbits_22
  #()
  counter22_inst
  (.clk(clk_12mhz_i)
  ,.reset(reset_n_async_unsafe_i)
  ,.up_i(1'b1)
  ,.down_i(1'b0)
  ,.count_o(newclk_w)
  );
  
  
  
  Counter__nbits_3
  #()
  counter_inst
  (.clk(newclk_w[21])
  ,.reset(reset_n_async_unsafe_i)
  ,.up_i(button_async_unsafe_i[1])
  ,.down_i(button_async_unsafe_i[2])
  ,.count_o({led_o[2],led_o[1],led_o[3]})
  );
endmodule
