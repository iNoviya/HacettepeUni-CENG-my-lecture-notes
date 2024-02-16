module counter_d_tb;

    // Parametreler
    reg reset, clk, mode;
    wire [2:0] count;

    // Düðümüzü çaðýrma
    counter_d dut (
        .reset(reset),
        .clk(clk),
        .mode(mode),
        .count(count)
    );

    // Clock sinyali oluþturma
    always begin
        clk = 1'b0;
        #5; // 5 birim zaman bekleme
        clk = 1'b1;
        #5; // 5 birim zaman bekleme
    end

    // Test senaryosu
    initial begin
        reset = 1'b1;
        mode = 1'b0;
        #10; // 10 birim zaman bekleme

        // Sýfýrlama yap
        reset = 1'b0;
        #5; // 5 birim zaman bekleme

        // Artýþ modunda sayma
        mode = 1'b1;
        #20; // 20 birim zaman bekleme

        // Azalýþ modunda sayma
        mode = 1'b0;
        #20; // 20 birim zaman bekleme

        // Daha fazla test senaryolarý eklenebilir

        $stop; // Testi sonlandýr
    end

endmodule
