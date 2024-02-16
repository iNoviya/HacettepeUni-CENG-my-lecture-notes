`timescale 1ns/10ps

module full_adder(
    input A, B, Cin,
    output S, Cout
);
    wire w1,w2,w3;
    half_adder haM1 (A,B,w1,w2);
    half_adder haM2 (w1,Cin,S,w3);
    or G1 (Cout,w2,w3);

endmodule