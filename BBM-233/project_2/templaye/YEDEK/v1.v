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
    reg A, B;

    dff dff1 ((present_state[1] & x) | (present_state[0] & x), CLK, RESET, A);
    dff dff2 ((present_state[1] & x) | (~present_state[0] & x), CLK, RESET, B);

    always @(*) begin
        if (RESET) begin
            present_state <= 2'b00;
        end else begin
            present_state <= next_state;
        end
    end

    always @(*) begin
        next_state[0] = A;
        next_state[1] = B;
    end

    assign F = A & B;
    assign S = {A, B, ~B};
endmodule