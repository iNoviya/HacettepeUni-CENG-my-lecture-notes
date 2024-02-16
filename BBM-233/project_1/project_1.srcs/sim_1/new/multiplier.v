`timescale 1ns/10ps

module multiplier_tb;
    reg [2:0] A;
    reg [2:0] B;
    wire [5:0] P;
    multiplier UUT(A,B,P);
    initial begin
        $dumpfile ("multiplier.vcd");
        $dumpvars;
        A = 3'b000;
        B = 3'b000;
        #10;
        A = 3'b111;
        B = 3'b010;
        #10;
        A = 3'b101;
        B = 3'b001;
        #10;
        A = 3'b010;
        B = 3'b011;
        #10;
        A = 3'b100;
        B = 3'b100;
        #10;
        A = 3'b010;
        B = 3'b101;
        #10;
        A = 3'b011;
        B = 3'b100;
        #10;
        A = 3'b100;
        B = 3'b100;
        #10;
        A = 3'b001;
        B = 3'b001;
        #10;
        A = 3'b011;
        B = 3'b110;
        #10;
        A = 3'b111;
        B = 3'b111;
        #10 $finish;
        
    end
endmodule
