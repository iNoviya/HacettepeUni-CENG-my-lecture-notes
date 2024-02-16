module full_adder(
    input A,
    input B,
    input Cin,
    wire t1,t2,t3;
    output S,
    output Cout
);
    xor g1 (t1,A,be);
    xor g2 (S,Cin,t1);
    and g3 (t2,A,B);
    and g4 (t3,t1,Cin);
    or g5  (Cout,t3,t2)

    // Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!

endmodule