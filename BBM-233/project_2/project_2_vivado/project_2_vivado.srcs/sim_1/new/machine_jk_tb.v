module machine_jk_tb;
    // Your code goes here.  DO NOT change anything that is already given! Otherwise, you will not be able to pass the tests!
    reg CLK;
    reg RESET;
    reg x;

    wire F;
    wire [2:0] S;

    machine_jk UUT (
        .CLK(CLK),
        .RESET(RESET),
        .x(x),
        .F(F),
        .S(S)
    );

    initial begin
        $dumpfile("machine_d_tb.vcd");
        $dumpvars;
        RESET = 1;
        x = 0;
        #20;

        RESET = 0;
        x = 0;
        #30;

        RESET = 1;
        x =1;
        #10;

        RESET = 0;
        #30;

        RESET = 1;
        x =0;
        #10;

        RESET = 0;
        x = 1;
        #10;

        x = 0;
        #40;

        x = 1;
        #10;





        $finish;
    end

    initial begin
        CLK = 1;
        forever begin
            #5;
            CLK = ~CLK;
        end
    end

endmodule