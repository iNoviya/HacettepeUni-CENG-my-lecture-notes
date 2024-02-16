`timescale 1ns / 1ps

module counter_d(
    input reset,
    input clk,
    input mode,
    output reg [2:0] count
    );
    
    reg [2:0] next_count;

    // D flip-flop'lar�n� tan�mla
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count <= 3'b000; // S�f�rlama durumu
        end else begin
            if (mode) begin // Art�� modu
                next_count = count + 1;
            end else begin // Azal�� modu
                next_count = count - 1;
            end
        end
    end

    // Flip-flop'lara atama
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            count <= 3'b000; // S�f�rlama durumu
        end else begin
            count <= next_count;
        end
    end

    
endmodule
