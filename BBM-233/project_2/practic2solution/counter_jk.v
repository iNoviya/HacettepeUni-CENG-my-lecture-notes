module counter_jk(input reset, input clk, input mode, output [2:0] count);
    wire q0, q1, q2;

    jk_sync_res jk0(
        .J((~mode) | (~q2 & ~q1) | (q2 & q1)),
        .K((~mode) | (~q2 & q1) | (q2 & ~q1)),
        .clk(clk), 
        .sync_reset(reset), 
        .Q(q0)
    );

    jk_sync_res jk1(
        .J((~mode & q0) | (~q2 & q0)), 
        .K((~mode & q0) | (q2 & q0)), 
        .clk(clk), 
        .sync_reset(reset), 
        .Q(q1)
    );

    jk_sync_res jk2(
        .J((~mode & q1 & q0) | (mode & q1 & ~q0)), 
        .K((~mode & q1 & q0) | (mode & ~q1 & ~q0)), 
        .clk(clk), 
        .sync_reset(reset), 
        .Q(q2)
    );


    assign count = {q2, q1, q0};
endmodule