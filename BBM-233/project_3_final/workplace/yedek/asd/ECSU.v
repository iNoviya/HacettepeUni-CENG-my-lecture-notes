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
    // initial begin 
    //     CLK = 0;
    // end

    // always #5 begin
    //     CLK = -CLK;
    // end

    reg [1:0] next_ECSU_state;
    parameter s0 = 2'b00, s1 = 2'b01, s2 = 2'b10, s3 = 2'b11;

    always @(posedge CLK, negedge RST) begin
        if (RST == 0) begin
            ECSU_state <= s0;
        end else begin
            ECSU_state <= next_ECSU_state;
        end
    end

    always @(ECSU_state,thunderstorm,temperature,wind,visibility) begin
        case (ECSU_state)
            s0: begin
                if (wind <= 15 && wind > 10 && visibility == 2'b01) begin
                    next_ECSU_state = s1;
                end else if (wind > 15 || visibility == 2'b11 || (temperature > 35 || temperature < -35) || thunderstorm == 1) begin
                    next_ECSU_state = s2;
                    severe_weather = 1;
                end else begin
                    next_ECSU_state = s0;
                    emergency_landing_alert <= 0;
                    severe_weather = 0;
                end
            end
            s1: begin
                if (wind <= 10 && visibility == 2'b00) begin
                    next_ECSU_state = s0;
                    severe_weather = 0;
                    emergency_landing_alert = 0;
                end else if (wind > 15 || (temperature > 35 || temperature < -35) || visibility == 2'b11 || thunderstorm == 1) begin
                    next_ECSU_state = s2;
                    severe_weather = 1;
                end 
            end
            s2: begin
                if (wind > 20 || (temperature > 40 || temperature < -40)) begin
                    next_ECSU_state = s3;
                    emergency_landing_alert = 1;
                end else if (thunderstorm == 0 && wind <= 10 && (temperature <= 35 && temperature >= -35) && visibility == 2'b01) begin
                    next_ECSU_state = s1;
                    severe_weather = 0;
                end 
            end
            s3: begin
                next_ECSU_state = s3;
                emergency_landing_alert = 1;

                // end else begin 
                //     next_ECSU_state = s1;
                //     emergency_landing_alert = 0;
                //     severe_weather = 0;
                // end
            end
            default: begin
                next_ECSU_state = s0;
            end
        endcase
    end

endmodule
