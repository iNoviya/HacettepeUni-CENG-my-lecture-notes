`timescale 1ns / 1ps

module multiplier(
    input [2:0] A, B,
    output [5:0] P
    );
//    wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15;
//    and G1_A0andB0  (P[0],A[0],B[0]);
//    and G2_A1andB0  (w1,A[1],B[0]);
//    and G3_A2andB0  (w2,A[2],B[0]);
//    and G4_A0andB1  (w3,A[0],B[1]);
//    and G5_A1andB1  (w4,A[1],B[1]);
//    and G6_A2andB1  (w5,A[2],B[1]);
//    and G7_A0andB2  (w9,A[0],B[1]);
//    and G8_A1andB2  (w10,A[1],B[1]);
//    and G9_A2andB2  (w11,A[2],B[1]);
    wire [2:0] w1,w2,w3;
    wire w6,w7,w8,w12,w13,w14,w15;
    genvar i;
    generate
        for (i = 0; i < 3; i = i + 1) begin : ANDs
            and G_A0andB (w1[i], A[0], B[i]);
            and G_A1andB (w2[i], A[1], B[i]);
            and G_A2andB (w3[i], A[2], B[i]);
        end
    endgenerate
    and g2 (P[0],w1[0],1);

    half_adder M1_haM (w2[0],w1[1],P[1],w6);
    half_adder M2_haM (w2[1],w1[2],w7,w8);

    full_adder M3_faM (w3[0],w7,w6,P[2],w12);
    full_adder M4_faM (w3[1],w2[2],w8,w13,w14);
    
    half_adder M5_haM (w13,w12,P[3],w15);
    full_adder M6_faM (w3[2],w14,w15,P[4],P[5]);
endmodule