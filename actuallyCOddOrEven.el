(defun odd-or-even (x)
	(find-file "oddOrEven.c") ;Create buffer
	(insert "#include <stdio.h>\n\n") ;Insert C function
	(insert "int main(){\n\n")
	(insert (format "\tint x = %d;\n\n" x))
	(insert "\tif(x % 2 == 0)\n")
	(insert "\t\tprintf(\"%d is even.\", x);\n")
	(insert "\telse\n")
	(insert "\t\tprintf(\"%d is odd.\", x);\n\n")	
	(insert "\treturn 0;\n")
	(insert "}")
	(save-buffer)(kill-buffer) 
	(shell-command "gcc oddOrEven.c -o oddOrEven") ;make C program
	(setq output (shell-command-to-string "./oddOrEven")) ;save the output
	(shell-command "rm oddOrEven.c oddOrEven") ;remove C program
	(message output))

(odd-or-even 10)
(odd-or-even 11)

