	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
	## TODO Your assembly code there
	## step 1 : get the two ints from memory inside registers t0 and t1 ?
	# get 7 into tO : get the address into t2
	la t2,mydata
	ld t0, 0 (t2) #offset 0 from t2
	ld t1, 8 (t2) #offset is 8 size size of a dword is 64=8bytes
	## step 2 compare ! TODO for you !
	
## END TODO - end of user assembly code
	ld	ra,8(sp)
	addi	sp,sp,16
	jr	ra
	ret

# Data comes here
	.section	.data
mydata:
	.dword 7
	.dword 42
min:
	.dword 0


