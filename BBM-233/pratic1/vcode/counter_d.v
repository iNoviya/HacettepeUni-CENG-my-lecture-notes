module counter_d(
    input reset,
    input clk,
    input mode,
    output  [2:0] count
);

    [2:0] next_count;

    // D flip-flop'larını tanımla
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count <= 3'b000; // Sıfırlama durumu
        end else begin
            if (mode) begin // Artış modu
                next_count = count + 1;
            end else begin // Azalış modu
                next_count = count - 1;
            end
        end
    end

    // Flip-flop'lara atama
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count <= 3'b000; // Sıfırlama durumu
        end else begin
            count <= next_count;
        end
    end

endmodule
