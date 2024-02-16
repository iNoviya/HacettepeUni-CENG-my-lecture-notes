module machine_d(
    input wire x,
    input wire CLK,
    input wire RESET,
    output wire F,
    output wire [2:0] S
);
    wire w1d1, w2d1, w3d1;
    wire w1d2, w2d2;
    reg [1:0] present_state;
    reg [1:0] next_state;
    reg [1:0] Q;

    dff dff1 ((present_state[1] & x) | (present_state[0] & x), CLK, RESET, Q[0]);
    dff dff2 ((present_state[1] & x) | (~present_state[0] & x), CLK, RESET, Q[1]);

    always @(*) begin
        if (RESET) begin
            present_state <= 2'b00;
        end else begin
            present_state <= next_state;
        end
    end

    always @(*) begin
        next_state[0] = Q[0];
        next_state[1] = Q[1];
    end

    assign F = present_state[1] & present_state[0];
    assign S = {present_state[1], present_state[0], ~present_state[0]};
endmodule
