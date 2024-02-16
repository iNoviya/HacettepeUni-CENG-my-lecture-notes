`timescale 1us / 1ps
module ARTAU(
    input radar_echo,
    input scan_for_target,
    input [31:0] jet_speed,
    input [31:0] max_safe_distance,
    input RST,
    input CLK,
    output reg radar_pulse_trigger,
    output reg [31:0] distance_to_target,
    output reg threat_detected,
    output reg [1:0] ARTAU_state
);

    reg [1:0] next_ARTAU_state;
    parameter s0 = 2'b00, s1 = 2'b01, s2 = 2'b10, s3 = 2'b11;

    always @(posedge CLK, negedge RST) begin
        if (RST == 0) begin
            ARTAU_state <= s0;
        end else begin
            ARTAU_state <= next_ARTAU_state;
        end
    end

    always @* begin
        case (ARTAU_state)
            s0: begin
                if (scan_for_target == 1) begin
                    next_ARTAU_state = s1;
                end else begin
                    next_ARTAU_state = s0;
                end
            end
            s1: begin
                if () begin
                    next_ARTAU_state = s2;
                end else begin
                    next_ARTAU_state = s1;
                end 
            end
            s2: begin
                if () begin
                    next_ARTAU_state = s1;
                end else if begin
                    next_ARTAU_state = s0;
                end else if begin
                    next_ARTAU_state = s3;
                end
            end
            s3: begin
                if () begin
                    next_ARTAU_state = s0;
                end else if begin
                    next_ARTAU_state = s1;
                end
            end
            default: begin
                next_ARTAU_state = s0;
            end
        endcase
    end

// Your code goes here.


endmodule