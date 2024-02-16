CC = iverilog 
FLAGS = -Wall 
library_input: *.v

counter_jk:
	$(CC) $(FLAGS) -o counter_jk_t counter_jk.v jk_sync_res.v counter_jk_tb.v
	vvp counter_jk_t
	gtkwave counter_jk_result.vcd
counter_d:
	$(CC) $(FLAGS) -o counter_d_t counter_d.v dff_sync_res.v counter_d_tb.v
	vvp counter_d_t
	gtkwave counter_d_result.vcd
clean:
	rm *.vcd
	rm counter_d_t
	rm counter_jk_t