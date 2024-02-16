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

    parameter IDLE = 2'b00, EMIT = 2'b01, LISTEN = 2'b10, ASSESS = 2'b11;
    parameter LIGHT_SPEED = 300000000;

    // Internal registers
    reg [7:0] pulse_count;
    reg [1:0] next_ARTAU_state;
    reg [7:0] listen_to_echo_timer;
    reg [7:0] pulse_emiter_timer;
    reg [7:0] status_update_timer;
    reg [31:0] d1;
    reg [31:0] d2;
    reg [7:0] count;
    reg count_emit_repait = 0;
    reg target_is_approaching = 0;

    always @(posedge CLK or posedge RST) begin
        if (RST == 1) count <=0;
        else count <= count + 1;
    end
    always @(posedge CLK or posedge RST or posedge radar_echo or posedge scan_for_target) begin
        if (RST) begin
            radar_pulse_trigger <= 0;
            distance_to_target <= 0;
            threat_detected <= 0;
            listen_to_echo_timer <= 0;
            pulse_emiter_timer <= 0;
            status_update_timer <= 0;
            ARTAU_state <= IDLE;

        end else begin
            ARTAU_state <= next_ARTAU_state;
             case(ARTAU_state)
                IDLE: begin
                    
                end

                EMIT: begin
                    
                end
                LISTEN: begin
                    
                end
                ASSESS: begin
                    
                end
                default: begin
                    next_ARTAU_state = IDLE;
                end
            endcase
        end
    end
endmodule
