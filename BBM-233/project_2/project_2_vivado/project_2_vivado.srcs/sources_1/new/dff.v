`timescale 1ns / 1ps
module dff (
    input D,      // Data input
    input CLK,    // Clock input
    input RESET,  // Asynchronous reset, active high
    output reg Q  // Output
);
    // Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!

    always @(posedge CLK or posedge RESET) begin
        if (RESET) begin
            Q <= 1'b0; // S�f�rlama durumunda
        end else begin
            Q <= D; // Giri� verisini ��k��a yans�t
        end
    end
endmodule