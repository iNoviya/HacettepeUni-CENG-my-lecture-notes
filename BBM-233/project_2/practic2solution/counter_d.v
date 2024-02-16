module counter_d(input reset, input clk, input mode, output [2:0] count);
    wire q0, q1, q2;

    dff_sync_res d0(.D((~mode & ~q0) | (mode & ~q2 & ~q1) | (mode & q2 & q1)), .clk(clk), .sync_reset(reset), .Q(q0));
    dff_sync_res d1(.D((q1 & ~q0) | (~mode & ~q1 & q0) | (mode & ~q2 & q0)), .clk(clk), .sync_reset(reset), .Q(q1));
    dff_sync_res d2(.D((~mode & ~q2 & q1 & q0) | (mode & q1 & ~q0) | (~mode & q2 & ~q1) | (~mode & q2 & ~q0) | (mode & q2 & q0)), .clk(clk), .sync_reset(reset), .Q(q2));
    assign count = {q2, q1, q0};
    
endmodule