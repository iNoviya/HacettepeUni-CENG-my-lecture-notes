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
    reg [1:0] pulse_count;
    reg [1:0] next_ARTAU_state;
    reg [31:0] listen_to_echo_timer;
    reg [31:0] pulse_emiter_timer;
    reg [31:0] status_update_timer;
    reg [31:0] d1;
    reg [31:0] d2;
    reg [7:0] count;
    reg count_emit_repait = 0;
    reg target_is_approaching = 0;
    reg [31:0] t1,t2,t3,t4,t5,t6,tstart,d1t,d2t;
    reg [31:0] asd = 1'b0;
    reg [31:0] Relative_Target_Velocity;


    
    always @ (posedge CLK , posedge RST , posedge scan_for_target, posedge radar_echo ) begin
        if (RST == 1) begin
            radar_pulse_trigger <= 0;
            distance_to_target <= 0;
            threat_detected <= 0;
            listen_to_echo_timer <= 0;
            pulse_emiter_timer <= 0;
            status_update_timer <= 0;
            count <= 0;
            pulse_count <= 0;
            count_emit_repait <= 0;
            d1 <= 0;
            d2 <= 0;
            t1 <= 0;
            t2 <= 0;
            t3 <= 0;
            t4 <= 0;
            t5 <= 0;
            t6 <= 0;
            tstart <= 0;
            d1t <= 0;
            d2t <= 0;
            asd <= 0;
            Relative_Target_Velocity <= 0;
            ARTAU_state <= IDLE;
            

        end else begin  
            case(ARTAU_state)
                IDLE: begin
                    if(scan_for_target == 1) begin
                        radar_pulse_trigger = 1;
                        t1 = $realtime;
                        tstart = $realtime;
                        #5;
                        while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                            #1;
                            asd = asd + 1;
                        end 
                        ARTAU_state = EMIT;
                    end else begin
                        ARTAU_state = IDLE;
                    end
                end

                EMIT: begin
                    t2 = $realtime;
                    pulse_count = pulse_count + 1;
                    pulse_emiter_timer = 300-(t2-t1);
                    #pulse_emiter_timer;
                    radar_pulse_trigger = 0;
                    #1;
                    while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                        #1;
                    end
                    t3 = $realtime;
                    ARTAU_state = LISTEN;
                end

                LISTEN: begin
                    t4 = $realtime;
                    listen_to_echo_timer = (t4 - t3);
                    if (listen_to_echo_timer > 1900) begin
                        radar_pulse_trigger = 0;
                        distance_to_target = 0;
                        threat_detected = 0;
                        pulse_count = 0;
                        t1 = 0;
                        t2 = 0;
                        t3 = 0;
                        t4 = 0;
                        t5 = 0;
                        t6 = 0;
                        // #1;
                        asd = 1;
                        while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                            #1;
                            asd = asd + 1;
                        end 
                        ARTAU_state = IDLE;
                        #(100-asd);
                    end else begin 
                        if (radar_echo == 1) begin
                            if (pulse_count == 1) begin
                                radar_pulse_trigger = 1;
                                t1 = $realtime;
                                distance_to_target = ((LIGHT_SPEED * (t1-tstart)) / 200000);
                                d1 = distance_to_target;
                                d1t = (t1-tstart);
                                #1;
                                while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                                    #1;
                                end
                                ARTAU_state = EMIT;

                            end else if (pulse_count == 2) begin
                                t5 = $realtime;
                                distance_to_target = ((LIGHT_SPEED * ( t5 - t1 )))/200000;
                                d2 = distance_to_target;
                                if ((d2 < d1) && (d2 < max_safe_distance)) threat_detected = 1;
                                d2t = (t5 - t1);
                                #1;
                                while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                                    #1;
                                end 
                                ARTAU_state = ASSESS;
                                

                            end 
                        end else begin
                            // #1;
                            // while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                            //     #1;
                            // end 
                            ARTAU_state = LISTEN;
                        end
                    end 
                end
                
                ASSESS: begin
                    t6 = $realtime;
                    pulse_count = 0;
                    Relative_Target_Velocity = (d2 + jet_speed*((d2t)-(d1t)) - d1)/((d1t)+(d2t));
                    
                    if ((d2 - d1) < 0) begin
                        // + jet_speed * (((d2t)-(d1t))/100000) 
                        target_is_approaching = 1;
                        if (d2 < max_safe_distance) threat_detected = 1;
                    end else begin
                        target_is_approaching = 0;
                    end

                    // if (( target_is_approaching == 1) && (d2 < max_safe_distance)) begin
                    //     threat_detected = 1;
                    // end 
                    status_update_timer = t6 -t5;
                    if (scan_for_target == 1) begin
                        t1 = $realtime;
                        radar_pulse_trigger = 1;
                        #1;
                        while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                            #1;
                        end 
                        ARTAU_state = EMIT;
                    end else if ((scan_for_target == 0 ) && (status_update_timer > 2900)) begin 
                        radar_pulse_trigger = 0;
                        distance_to_target = 0;
                        pulse_count = 0;
                        threat_detected = 0;
                        t1 = 0;
                        t2 = 0;
                        t3 = 0;
                        t4 = 0;
                        t5 = 0;
                        t6 = 0;
                        #1;
                        while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                            #1;
                        end 
                        ARTAU_state = IDLE;
                    end else begin
                        // #1;
                        // while ((($realtime % 50) !=0) || (($realtime % 100) ==0)) begin
                        //     #1;
                        // end 
                        ARTAU_state = ASSESS;
                    end
                end
                default: begin
                    ARTAU_state = IDLE;
                end
            endcase
        end 
    end

endmodule