`timescale 1ns/10ps

module half_adder_tb;

	// Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!
    reg A,B;
    wire S,C;
    half_adder UUT (A,B,S,C);
    initial begin
        $dumpfile("half_adder.vcd");
        $dumpvars;
        A=0;
        B=0;
        #10
        A=0;
        B=1;
        #10
        A=1;
        B=0;
        #10
        A=1;
        B=1;
        #10 $finish;
    end
endmodule