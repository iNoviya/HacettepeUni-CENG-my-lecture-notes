`timescale 1ns/1ps


module counter_d_tb;
    reg reset, clk, mode; 
    wire [2:0] count;
    integer i;
    counter_d c1(reset, clk, mode, count);
    
    initial begin
        $dumpfile("counter_d_result.vcd");
        $dumpvars;
        reset = 1;
        mode = 0;
        #21;
        reset = 0; 
        #101;
        mode = 1;
        #101;
        reset=1;
        #20;
        $finish;
    end

    initial begin
        clk = 0;
        forever begin
            #5;
            clk = ~clk;
        end
    end

endmodule