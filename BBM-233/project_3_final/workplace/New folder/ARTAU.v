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
    parameter time = 0;
    parameter Relative_Target_Velocity = ((distance_to_target + jet_speed * time ) - max_safe_distance) / 2;

    // reg [1:0] next_ARTAU_state;
    // parameter s0 = 2'b00, s1 = 2'b01, s2 = 2'b10, s3 = 2'b11;

    // always @(posedge CLK, negedge RST) begin
    //     if (RST == 0) begin
    //         ARTAU_state <= s0;
    //     end else begin
    //         ARTAU_state <= next_ARTAU_state;
    //     end
    // end

    // always @* begin
    //     case (ARTAU_state)
    //         s0: begin
    //             if (scan_for_target == 1) begin
    //                 next_ARTAU_state = s1;
    //             end else begin
    //                 next_ARTAU_state = s0;
    //                 radar_pulse_trigger = 0;
    //                 distance_to_target = 0;
    //                 threat_detected = 0;
    //             end
    //         end
    //         s1: begin
    //             if () begin
    //                 next_ARTAU_state = s2;
    //             end else begin
    //                 next_ARTAU_state = s1;
    //             end 
    //         end
    //         s2: begin
    //             if () begin
    //                 next_ARTAU_state = s1;
    //             end else if begin
    //                 next_ARTAU_state = s0;
    //             end else if begin
    //                 next_ARTAU_state = s3;
    //             end
    //         end
    //         s3: begin
    //             if () begin
    //                 next_ARTAU_state = s0;
    //             end else if begin
    //                 next_ARTAU_state = s1;
    //             end
    //         end
    //         default: begin
    //             next_ARTAU_state = s0;
    //         end
    //     endcase
    // end

    // Your code goes here.
    // Define states

    parameter IDLE = 2'b00;
    parameter EMIT = 2'b01;
    parameter LISTEN = 2'b10;
    parameter ASSESS = 2'b11;

    parameter Relative_Target_Velocity = dis

    // // Internal registers
    // reg [1:0] state_reg;
    // reg emit_timer;
    // reg listen_timer;
    // reg [31:0] prev_distance;
    // reg target_detected;
    // reg [31:0] distance_calc;

    // // State transition and outputs logic
    // always @(posedge CLK or posedge RST) begin
    //     if (RST) begin
    //         state_reg <= IDLE;
    //         radar_pulse_trigger <= 0;
    //         distance_to_target <= 0;
    //         threat_detected <= 0;
    //         ARTAU_state <= IDLE;
    //         emit_timer <= 0;
    //         listen_timer <= 0;
    //         prev_distance <= 0;
    //         target_detected <= 0;
    //         distance_calc <= 0;
    //     end else begin
    //         case(state_reg)
    //             IDLE: begin
    //                 if (scan_for_target) begin
    //                     radar_pulse_trigger = 1;
    //                     emit_timer = 3; // 300μs (assuming 100μs per clock cycle)
    //                     state_reg = EMIT;
    //                 end
    //             end
    //             EMIT: begin
    //                 if (emit_timer > 0) begin
    //                     emit_timer = emit_timer - 1;
    //                 end else begin
    //                     radar_pulse_trigger = 0;
    //                     listen_timer = 20; // 2000μs (assuming 100μs per clock cycle)
    //                     state_reg = LISTEN;
    //                 end
    //             end
    //             LISTEN: begin
    //                 if (listen_timer > 0 && radar_echo) begin
    //                     distance_calc = (radar_echo * 300000000) / 2; // Calculate distance
    //                     distance_to_target = distance_calc;
    //                     if (target_detected == 0) begin
    //                         prev_distance = distance_calc;
    //                         target_detected = 1;
    //                         state_reg = EMIT;
    //                     end else begin
    //                         // Assess threat
    //                         if ((jet_speed - ((prev_distance - distance_to_target) / 3)) < 0 && distance_to_target < max_safe_distance) begin
    //                             threat_detected = 1;
    //                         end
    //                         state_reg <= ASSESS;
    //                     end
    //                 end else if (listen_timer == 0) begin
    //                     state_reg <= IDLE;
    //                 end
    //             end
    //             ASSESS: begin
    //                 if (scan_for_target) begin
    //                     radar_pulse_trigger = 1;
    //                     emit_timer = 3; // 300μs (assuming 100μs per clock cycle)
    //                     state_reg = EMIT;
    //                 end else if (listen_timer == 0) begin
    //                     state_reg = IDLE;
    //                 end
    //             end
    //         endcase
    //     end
    // end

    // // Output assignment
    // always @(*) begin
    //     case(state_reg)
    //         IDLE: ARTAU_state = IDLE;
    //         EMIT: ARTAU_state = EMIT;
    //         LISTEN: ARTAU_state = LISTEN;
    //         ASSESS: ARTAU_state = ASSESS;
    //     endcase
    // end

endmodule