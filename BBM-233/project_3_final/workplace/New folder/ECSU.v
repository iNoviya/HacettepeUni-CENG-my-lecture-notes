// M MUSTAFA KARATAŞ
// 2230356164
// BBM_233 Verilog (final) assigment III
`timescale 1us / 1ns

module ECSU(
    input CLK,
    input RST,
    input thunderstorm,
    input [5:0] wind,
    input [1:0] visibility,
    input signed [7:0] temperature,
    output reg severe_weather,
    output reg emergency_landing_alert,
    output reg [1:0] ECSU_state
);

    wire [1:0] next_ECSU_state;
    parameter ALL_CLEAR = 2'b00, CAUTION = 2'b01, HIGH_ALERT = 2'b10, EMERGENCY = 2'b11;

    always @(posedge CLK or posedge RST) begin
        if (RST == 1) begin
            ECSU_state <= ALL_CLEAR;
            severe_weather <= 0;
            emergency_landing_alert <= 0;
        end else 
            ECSU_state <= next_ECSU_state;
    end


    always @(ECSU_state,thunderstorm,temperature,wind,visibility,RST,next_ECSU_state,severe_weather,severe_weather) begin
        case (ECSU_state)
            ALL_CLEAR: begin
                if (wind <= 15 && wind > 10 && visibility == 2'b01) begin
                    next_ECSU_state = CAUTION;
                end else if (wind > 15 || visibility == 2'b11 || (temperature > 35 || temperature < -35) || thunderstorm == 1) begin
                    next_ECSU_state = HIGH_ALERT;
                    severe_weather = 1;
                end else begin
                    next_ECSU_state = ALL_CLEAR;
                    emergency_landing_alert <= 0;
                    severe_weather = 0;
                end
            end
            CAUTION: begin
                if (wind <= 10 && visibility == 2'b00) begin
                    next_ECSU_state = ALL_CLEAR;
                    // severe_weather = 0;
                    // emergency_landing_alert = 0;
                end else if (wind > 15 || (temperature > 35 || temperature < -35) || visibility == 2'b11 || thunderstorm == 1) begin
                    next_ECSU_state = HIGH_ALERT;
                    severe_weather = 1;
                end else 
                    next_ECSU_state = CAUTION;
                
            end
            HIGH_ALERT: begin
                if (wind > 20 || (temperature > 40 || temperature < -40)) begin
                    next_ECSU_state = EMERGENCY;
                    emergency_landing_alert = 1;
                end else if (thunderstorm == 0 && wind <= 10 && (temperature <= 35 && temperature >= -35) && visibility == 2'b01) begin
                    next_ECSU_state = CAUTION;
                    severe_weather = 0;
                end else begin
                    next_ECSU_state = HIGH_ALERT;
                end
            end
            EMERGENCY: begin
                if (RST == 1 ) begin
                    next_ECSU_state = ALL_CLEAR;
                    severe_weather = 0;
                    emergency_landing_alert = 0;
                end else begin
                    next_ECSU_state = EMERGENCY;
                    // emergency_landing_alert = 1;
                end
            end
            default: begin
                next_ECSU_state = ALL_CLEAR;
            end
        endcase
    end

endmodule
