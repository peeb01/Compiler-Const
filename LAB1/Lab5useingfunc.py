import LAB5 as l5
import os

cwd = os.getcwd()

#1 convert to binary and write mct to mc
### convert to binary
path = cwd + '\lab5src.mct'
binary = l5.newformat(path)
bin = binary._binary()
binary._2_newfile('outputsq')

#2
### Check
binary._2_newfile_with_check('outsq')

#3
### mc to mct
l503path = cwd + '\outputsq.mc'
mcf = l5.conv_2_mct(l503path)
mcf.write_2_newfile('hhhhhhhhh')


# 4
### write mc to asm
l504path = cwd + '\outputsq.mc'
asm = l5.mc_2_asm(l504path)
asm.write_2_asm('assssm')


# 5
### binary machine code
l505path = cwd + '\lab5Hexfiledata.txt'
readhex = l5.readHex(l505path)
readhex.return_data_errors()