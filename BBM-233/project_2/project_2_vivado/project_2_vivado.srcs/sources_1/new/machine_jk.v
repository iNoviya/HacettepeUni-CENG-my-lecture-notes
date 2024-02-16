module machine_jk(
    input wire x,
    input wire CLK,
    input wire RESET,
    output wire F,
    output wire [2:0] S
);
    // Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!
    wire j1_in, j2_in, j3_in;
    wire k1_in, k2_in, k3_in;
    wire A,B,C;

    jkff JKFF1(.CLK(CLK), .RESET(RESET), .J(j1_in), .K(k1_in), .Q(A));
    jkff JKFF2(.CLK(CLK), .RESET(RESET), .J(j2_in), .K(k2_in), .Q(B));
    jkff JKFF3(.CLK(CLK), .RESET(RESET), .J(j3_in), .K(k3_in), .Q(C));

    assign j1_in = (B & ~x);
    assign k1_in = ~A;  

    assign j2_in = (~B & ~x);
    assign k2_in = (~A & ~x);

    assign j3_in = x;
    assign k3_in = x;

    assign F = (A & B & ~C);
    // S[0], S[1], S[2] 
    assign S[0] = C;
    assign S[1] = B;
    assign S[2] = A;

endmodule