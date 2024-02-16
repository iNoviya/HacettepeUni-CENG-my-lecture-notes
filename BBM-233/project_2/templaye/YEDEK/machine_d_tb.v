module machine_d_tb;

    reg CLK;
    reg RESET;
    reg x;

    wire F;
    wire [2:0] S;

    machine_d UUT (
        .CLK(CLK),
        .RESET(RESET),
        .x(x),
        .F(F),
        .S(S)
    );

    initial begin
        $dumpfile("counter_d_result.vcd");
        $dumpvars;
        RESET = 1;
        x = 0;
        #3;

        RESET = 0;
        x = 0;
        #6;

        x = 1;
        #20;

        x = 0;
        #10;

        x = 1;
        #20;

        x = 0;
        #10;

        x = 1;
        #20;

        x = 0;
        #20;

        x = 1;
        #10;

        x = 0;
        #10;

        x =1;
        #10;

        RESET = 1;
        #5;

        RESET = 0;
        #10;

        x = 0;
        #40;

        x = 1;
        #10;

        RESET = 1;
        #10;


        $finish;
    end

    initial begin
        CLK = 0;
        forever begin
            #5;
            CLK = ~CLK;
        end
    end

endmodule
