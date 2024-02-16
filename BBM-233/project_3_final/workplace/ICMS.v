`timescale 1us / 1ps

module ICMS(
    input CLK,
    input RST,

    input radar_echo,
    input scan_for_target,
    input [31:0] jet_speed,
    input [31:0] max_safe_distance,
    input [5:0] wind,
    input thunderstorm,
    input [1:0] visibility,
    input signed [7:0] temperature,

    output radar_pulse_trigger,
    output [31:0] distance_to_target,
    output safe_to_engage,
    output threat_detected,
    output emergency_landing_alert,
    output [1:0] ECSU_state,  
    output [1:0] ARTAU_state
);

   // Your code goes here.

    // always @(posedge CLK or posedge RST) begin
    //     if (RST == 1) begin
    //         radar_pulse_trigger <= 0;
    //         distance_to_target <= 0;
    //         safe_to_engage <= 0;
    //         threat_detected <= 0;
    //         emergency_landing_alert <= 0;
    //         ECSU_state <= 0;  
    //         ARTAU_state <= 0;
    //     end 
    // end

    wire m1_out_threat_detected,m2_out_severe_weather;


    ARTAU M1(
        .radar_echo(radar_echo),
        .scan_for_target(scan_for_target),
        .jet_speed(jet_speed),
        .max_safe_distance(max_safe_distance),
        .RST(RST),
        .CLK(CLK),
        .radar_pulse_trigger(radar_pulse_trigger),
        .distance_to_target(distance_to_target),
        .threat_detected(m1_out_threat_detected),
        .ARTAU_state(ARTAU_state)
    );
    ECSU M2 (
        .CLK(CLK),
        .RST(RST),
        .thunderstorm(thunderstorm),
        .wind(wind),
        .visibility(visibility),
        .temperature(temp),
        .severe_weather(m2_out_severe_weather),
        .emergency_landing_alert(emergency_landing_alert),
        .ECSU_state(ECSU_state)
    );

    assign threat_detected = m1_out_threat_detected;
    assign safe_to_engage = m2_out_severe_weather & m1_out_threat_detected;
    


endmodule