# Command Reference
`put` - puts a binary value in the address space - args: `0/1, index`  
`vput` - puts a binary value in the v-address space - args: `0/1, index`  
`prnt` - reads the v-address space, and prints out the respective ascii character  
`equl` - compares the values of the two `compare_index`s in address space, and writes the comparison result (1 for equivalent, 0 for different) to the `write_index` - args: `compare_index, compare_index_2, write_index`  
`vequl` - compares the values of the two `compare_index`s in v-address space, and writes the comparison result (1 for equivalent, 0 for different) to the `write_index` - args: `compare_index, compare_index_2, write_index`  
`mov` - moves a value from the addr range at index `i1` to the v-addr range at index `i2` - args: `i1, i2`   
`cpy` - copies a value from the addr range at index `i1` to the v-addr range at index `i2` - args: `i1, i2`  
`flsh` - resets all values in the addr range  
`vflsh` - resets all values in the v-addr range  
`jmp` - changes the current line number that the interpreter is interpreting to number (int) `n1` (0-based) - args: `n1`

## Debug
`dump` - prints out the contents of the address space to console  
`vdump` - prints outs the contents of the v-address
