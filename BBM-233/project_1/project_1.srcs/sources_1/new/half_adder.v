`timescale 1ns/10ps

module half_adder(
    input A, B,
    output S, C
);
	// Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!
    // find sum
    // xor G1 (S,A,B);
    assign S = A ^ B;
    // find carry
    assign C = A & B;
    // and G2 (C,A,B);

endmodule