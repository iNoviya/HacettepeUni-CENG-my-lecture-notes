module machine_d(
    input wire CLK,     // 
    input wire RESET,   // 
    input wire x,       // x 
    output wire F,       // F 
    output wire [2:0] S  // S 
);

    wire d1_in, d2_in, d3_in;   // D flip-flop inputs
    wire A, B, C;           // flipflopt output wire

    dff DFF1(.CLK(CLK), .RESET(RESET), .D(d1_in), .Q(A));
    dff DFF2(.CLK(CLK), .RESET(RESET), .D(d2_in), .Q(B));
    dff DFF3(.CLK(CLK), .RESET(RESET), .D(d3_in), .Q(C));

  
    assign d1_in = A | (B & ~x);     
    assign d2_in = (B & x) | (~B & ~x) | (A & ~x);      
    assign d3_in = (~C & x) | (C & ~x);

    // F 
        // assign F = (x & ~B & ~C) | (x & A & B & C);
    assign F = (A & B & ~C);
    // S[0], S[1], S[2] 
    assign S[0] = C;
    assign S[1] = B;
    assign S[2] = A;

endmodule