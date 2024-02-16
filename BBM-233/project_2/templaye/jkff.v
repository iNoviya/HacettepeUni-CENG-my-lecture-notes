// M MUSTAFA KARATAŞ
// 2230356164
// BBM_233 Verilog assigment II
module jkff (
    input J,      // Data input
    input K,      // Data input
    input CLK,    // Clock input
    input RESET,  // Asynchronous reset, active high
    output reg Q  // Output
);
    // Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!
    // JK flip-flop 
    always @(posedge CLK or posedge RESET) begin
        if (RESET) begin
            Q <= 1'b0; 
        end else begin
            case ({J, K})
                2'b00: Q <= Q; // J=0, K=0 
                2'b01: Q <= 1'b0; // J=0, K=1 
                2'b10: Q <= 1'b1; // J=1, K=0 
                2'b11: Q <= ~Q; // J=1, K=1 
            endcase
        end
    end
endmodule