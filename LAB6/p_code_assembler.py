import numpy as np

class pcode_assembler:
    """ P Code Assembler """

    def __init__(self) -> None:
        pass
    
    def read_asm_re(self, filename):
        """Fuction return to Hexadecimal data
        \n\n\n\n\n
        Args : filename is file name or file path
        \n\n\n
        Return : Hexadecimal number(P Code) from .asm
        """
        with open(filename, 'r') as file:
            filedata = file.read()
            filedata = np.array([list(map(str, line.split())) for line in filedata.split('\n')])
            for j in range(len(filedata)):
                for i in range(len(filedata[0])):
                    if filedata[j][i] == 'LIT':
                        filedata[j][i] = '0'
                    elif filedata[j][i] == 'OPR':
                        filedata[j][i] = '7'
                    elif filedata[j][i] == 'LOD':
                        filedata[j][i] = '2'
                    elif filedata[j][i] == 'STO':
                        filedata[j][i] = '3'
                    elif filedata[j][i] == 'JMP':
                        filedata[j][i] = '5'
                        
            self.binary_data = [[format(int(num[0]), '03b'), format(int(num[1]), '02b'), format(int(num[2]), '011b')] for num in filedata]
            self.ls = []
            for i in range(len(self.binary_data)):
                st = ''
                for j in range(len(self.binary_data[0])):
                    st = st + self.binary_data[i][j]
                self.ls.append([st])  
            formatted_data = [
            " ".join(row) for row in self.ls
                    ]
            binary_string = "\n".join([j[:4] + ' ' + j[4:8] + ' ' + j[8:12] + ' ' + j[12:] for j in formatted_data])
            binary_data = np.array([list(map(str, line.split())) for line in binary_string.split('\n')])
            hexadecimal_data = [[hex(int(''.join(sublist), 2))[2:] for sublist in row] for row in binary_data]  
            el = []
            for i in range(len(hexadecimal_data)):
                sk = ''
                for j in range(len(hexadecimal_data[0])):
                    sk = sk + hexadecimal_data[i][j]
                el.append(sk)
            return el


    def check_asm(self, data):
        """ Check Macro and Maive accept asm """
        row = []
        macro_as1 = ['STOP', 'RET', 'NEG', 'ADD', 'SUB', 'MUL', 'DIV', 'ISODD', 'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE']
        naive_asm = ['LIT', 'INT', 'JMP', 'JPC','LOD', 'STO','CAL']
        
        for i in range(len(data)):

            if len(data[i]) == 3:
                if data[i][0] == 'OPR' and int(data[i][1]) != 0:
                    pass
                elif (data[i][0] not in naive_asm) and (data[i][0] != 'OPR'):
                    text = f'line : {i+1} not accept.'
                    row.append(text)  
                elif (data[i][0] in naive_asm) and (data[i][2] != 'V'):
                    text = f'line : {i+1} not accept.'
                    row.append(text)

            elif len(data[i]) != 3:
                if len(data[i]) == 2:
                    if (data[i][0] == 'ASSIGN' or data[i][0] == 'ALLOC' or data[i][0] == 'JUMP' or data[i][0] == 'JZ')  and data[i][1] == 'V' :
                        pass
                    else :
                        text = f'line : {i+1} not accept.'
                        row.append(text)
                elif len(data[i]) == 1:
                    if data[i][0] not in macro_as1:
                        text = f'line : {i+1} not accept.'
                        row.append(text)
                elif len(data[i]) > 3:
                    text = f'Line : {i+1} not accept.'
                    row.append(text)

        return row
    
    def macro_asm_naive(self, filename):
        with open(filename, 'r') as file:
            filedata = file.read()
            self.data = ([list(map(str, line.split())) for line in filedata.split('\n')])
            self.ch = self.check_asm(self.data)
            if len(self.ch) != 0:
                for i in self.ch:
                    print(i)
                    
            if len(self.ch) == 0:
                return self.data
        

ax = pcode_assembler()
data = ax.read_asm_re('test.asm')
result = ax.macro_asm_naive('test.asm')
print(data)