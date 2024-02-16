module jk_sync_res(J, K, clk, sync_reset, Q);
    input J;
    input K;
    input clk; // clock input 
    input sync_reset; // synchronous reset 
    output reg Q; // output Q 
    
    always @(posedge clk) 
    begin
        if(sync_reset==1'b1)
            Q <= 1'b0; 
        else begin
            case ({J,K})  
                2'b00 :  Q <= Q;  
                2'b01 :  Q <= 0;  
                2'b10 :  Q <= 1;  
                2'b11 :  Q <= ~Q;  
            endcase  
        end
    end 
endmodule