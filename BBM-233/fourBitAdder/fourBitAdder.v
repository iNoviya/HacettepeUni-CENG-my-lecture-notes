module fourBitAdder (
    input A[3,0];
    input B[3,0];
    input Cin;

    wire t1,t2,t3;

    output S[3,0];
    output Cout;
)
    full_adder fa1 (S[0],t1,A[0],B[0],Cin);
    full_adder fa2 (S[1],t2,A[1],B[1],t1);
    full_adder fa3 (S[2],t3,A[2],B[2],t2);
    full_adder fa4 (S[3],Cout,A[3],B[3],t3);

endmodule