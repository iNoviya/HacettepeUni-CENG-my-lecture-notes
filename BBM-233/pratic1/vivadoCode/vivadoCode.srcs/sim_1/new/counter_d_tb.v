module counter_d_tb;

    // Parametreler
    reg reset, clk, mode;
    wire [2:0] count;

    // D���m�z� �a��rma
    counter_d dut (
        .reset(reset),
        .clk(clk),
        .mode(mode),
        .count(count)
    );

    // Clock sinyali olu�turma
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

        // S�f�rlama yap
        reset = 1'b0;
        #5; // 5 birim zaman bekleme

        // Art�� modunda sayma
        mode = 1'b1;
        #20; // 20 birim zaman bekleme

        // Azal�� modunda sayma
        mode = 1'b0;
        #20; // 20 birim zaman bekleme

        // Daha fazla test senaryolar� eklenebilir

        $stop; // Testi sonland�r
    end

endmodule
