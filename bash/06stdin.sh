#! /bin/bash

# stdin will be print into file1.txt
# since ls -al is correct command, not stderr, so file2.txt will be created but empty
ls -al 1>06_output_files/06_file1.txt 2>06_output_files/06_file2.txt

ls +al 1>06_output_files/06_file3.txt 2>06_output_files/06_file4.txt

# with wrong command, if no stderr specify, it will print to terminal
ls +al 1>06_output_files/06_file5.txt

# combine both stdin and stderr to same place
ls +al 1>06_output_files/06_file6.txt 2>&1

# or same effect as above as shortcut
ls -al >& 06_output_files/06_file7.txt