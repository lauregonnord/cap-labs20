##Automatically generated RISCV code, MIF08 & CAP 2019
##non executable 3-Address instructions version


##prelude

        .text
        .globl f
f:
        addi sp, sp, -160
        sd ra, 0(sp)
        sd fp, 8(sp)
        addi fp, sp, 160
        

##Generated Code
        sd s1, 16(sp)
        sd s2, 24(sp)
        sd s3, 32(sp)
        sd s4, 40(sp)
        sd s5, 48(sp)
        sd s6, 56(sp)
        sd s7, 64(sp)
        sd s8, 72(sp)
        sd s9, 80(sp)
        sd s10, 88(sp)
        sd s11, 96(sp)
        # Return at end of function:
        li temp_0, 1
        sub temp_1, zero, temp_0
        mv a0, temp_1
        ld s1, 16(sp)
        ld s2, 24(sp)
        ld s3, 32(sp)
        ld s4, 40(sp)
        ld s5, 48(sp)
        ld s6, 56(sp)
        ld s7, 64(sp)
        ld s8, 72(sp)
        ld s9, 80(sp)
        ld s10, 88(sp)
        ld s11, 96(sp)


##postlude

        ld ra, 0(sp)
        ld fp, 8(sp)
        addi sp, sp, 160
        ret
##Automatically generated RISCV code, MIF08 & CAP 2019
##non executable 3-Address instructions version


##prelude

        .text
        .globl main
main:
        addi sp, sp, -160
        sd ra, 0(sp)
        sd fp, 8(sp)
        addi fp, sp, 160
        

##Generated Code
        sd s1, 16(sp)
        sd s2, 24(sp)
        sd s3, 32(sp)
        sd s4, 40(sp)
        sd s5, 48(sp)
        sd s6, 56(sp)
        sd s7, 64(sp)
        sd s8, 72(sp)
        sd s9, 80(sp)
        sd s10, 88(sp)
        sd s11, 96(sp)
        # Return at end of function:
        sd t0, 104(sp)
        sd t1, 112(sp)
        sd t2, 120(sp)
        sd t3, 128(sp)
        sd t4, 136(sp)
        sd t5, 144(sp)
        sd t6, 152(sp)
        call f
        ld t0, 104(sp)
        ld t1, 112(sp)
        ld t2, 120(sp)
        ld t3, 128(sp)
        ld t4, 136(sp)
        ld t5, 144(sp)
        ld t6, 152(sp)
        mv temp_0, a0
        mv a0, temp_0
        ld s1, 16(sp)
        ld s2, 24(sp)
        ld s3, 32(sp)
        ld s4, 40(sp)
        ld s5, 48(sp)
        ld s6, 56(sp)
        ld s7, 64(sp)
        ld s8, 72(sp)
        ld s9, 80(sp)
        ld s10, 88(sp)
        ld s11, 96(sp)


##postlude

        ld ra, 0(sp)
        ld fp, 8(sp)
        addi sp, sp, 160
        ret
