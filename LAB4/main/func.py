import time


class command:  
    def __init__(self) -> None:
        self.filename = None
        self.data = None
        self.B = 0
        self.P = 0
        self.T = 0

        self.stack = []
        self.stack_pos = 0

        rows = 4
        columns = 6
        self.instructionmem = [[(0, 0, 0) for _ in range(columns)] for _ in range(rows)]

        rows = 10
        columns = 10
        value = "0000"
        self.datamem = [[value for _ in range(columns)] for _ in range(rows)]

        self.stop = 1

    def hex_to_binary(self, hex_string):
        decimal_value = int(hex_string, 16)
        self.binary_ = bin(decimal_value)[2:].zfill(16)
        return self.binary_

    def convert_to_tuple(self, binary_string):

        a_bits = binary_string[:3]
        b_bits = binary_string[3:5]
        c_bits = binary_string[5:]

        decimal_a = int(a_bits, 2)
        decimal_b = int(b_bits, 2)
        decimal_c = int(c_bits, 2)

        return decimal_a, decimal_b, decimal_c
    
    def load(self, filename):
        filename = filename
        binary_list = []
        self.binaryL = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    hex_value = line.strip()
                    self.binary_value = self.hex_to_binary(hex_value)
                    self.modified_binary = self.binary_value[:3] + '00' + self.binary_value[5:]
                    self.binaryL.append(self.modified_binary)
                    result_tuple = self.convert_to_tuple(self.modified_binary)

                    binary_list.append(result_tuple)
        except FileNotFoundError:
            print(f"File not found: {filename}")

        self.blist = binary_list.copy()
        # print(self.binaryL)
        for i in range(len(self.instructionmem)):
            for j in range(len(self.instructionmem[i])):
                if binary_list:
                    self.instructionmem[i][j] = binary_list.pop(0)
        # print(self.instructionmem[0])
        return self.instructionmem
    
    def set_values(self, b, p, t):
        self.Br = f"{b:04d}"
        self.Pr = f"{p:04d}"
        self.Tr = f"{t:04d}"

    def dump(self):
        self.set_values(self.B, self.P, self.T)
        reg = f'\n\nREGISTERS:\nB (Base):\t\t\t{self.Br}\nP (Program Counter):\t\t{self.Pr}\nT (Top of stack):\t\t{self.Tr}'
        print(reg)
        ins = '\nINSTRUCCTION MEMORY:\n\t0\t\t1\t\t2\t\t3\t\t4\n'
        for i in range(len(self.instructionmem)):
            a = self.instructionmem
            ins += f'{i*5}\t{a[i][i]}\t{a[i][1]}\t{a[i][2]}\t{a[i][3]}\t{a[i][4]}\n'
        print(ins)

        datamems = 'DATA MEMORY:\n\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n'
        for i in range(len(self.datamem)):
            d = self.datamem
            datamems += f'{i * 10}\t{d[i][0]}\t{d[i][1]}\t{d[i][2]}\t{d[i][3]}\t{d[i][4]}\t{d[i][5]}\t{d[i][6]}\t{d[i][7]}\t{d[i][8]}\t{d[i][9]}\n'
        print(datamems)

    # def set_stk(self):
    #         if self.B == 0 and self.T == 0:
    #             self.B = 1
    #             self.T = 1
    #         if self.B != 0 and self.T != 0:
    #             self.T = self.T + 1

    def _2_complement(self, val):
        xnary = ''
        for char in val:
            if char == '0':
                xnary += '1'
            else:
                xnary += '0'
        # print(val)
        # print(xnary)
        hex_value = format(int(xnary, 2), '04X')
        return hex_value


    def step(self):
        (func, leve, val) = self.blist[self.stack_pos]
        self.stack_pos += 1
        # print(func == 0)
        # print(self.B)
        # print(self.T)
        self.T = 1
        if func == 0:
            hfunc = hex(func)[2:].upper()
            hleve = hex(leve)[2:].upper()
            hvalu = hex(val)[2:].upper()
            hexa = format(int(hfunc + hleve + hvalu, 16), '04X')
            self.datamem[self.P//10][self.P] = hexa
            # print(self.datamem)
            self.P += 1

        if func == 7:
            if val == 0:
                self.stop = 0
            elif val == 1:
                self.stop = 1
            elif val == 2:
                data = self.binaryL[self.P//10 + self.P - 1]
                hexformat = self._2_complement(data)
                # print('HHHHHHHHH', hexformat)
                self.datamem[self.P//10][self.P-1] = hexformat
                self.P += 1
                


    def run(self):
        for i in range(len(self.binaryL)):
            self.step()
            if self.stop == 0:
                break
            self.dump()
            time.sleep(2)
    



# cm = command()
# cm.load('sample.mc')
# cm.run()
# cm.dump()
