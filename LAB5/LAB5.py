class newformat:
    """
    This class provides functionality for processing data from a text file and converting it to a binary format.

    The input file is expected to have lines with three integers separated by spaces.
    The format for each line is assumed to be: Function Level Value
    where Function, Level, and Value are integers.

    Example:\n
    1 0 1023\n
    2 3 512\n
    0 1 255\n

    Usage:
    - Initialize the class with the filename.
    - Use readFile method to read the content of the file.
    - Use _2_newfile_true_convert method to perform the conversion and save the binary data to a new file.

    Example Usage:
    filename = 'your_file_path.txt'  # Replace with your actual file path
    converter = newformat(filename)

    ### Read data from the file
    data = converter.readFile()

    ### Check and convert data, then save to a new file
    converter._2_newfile_true_convert('output_file')
    """

    def __init__(self, filename) -> None:
        self.filename = filename
        self.filedata = None
        self.bin = None
    
    def readFile(self):
        """
        Reads the content of the specified file.

        Returns:
        str: The content of the file.
        """
        with open(self.filename, 'r') as file:
            self.filedata = file.read()
            return self.filedata

    def _binary(self):
        """
        Converts the data to binary format.

        Returns:
        str: The binary data.
        """
        if self.filedata == None:
            self.filedata = self.readFile()
        data = self.filedata
        data = [list(map(int, line.split())) for line in data.split('\n')]
        column_bit_lengths = [3, 2, 11]

        binary_data = [
            [bin(num)[2:].zfill(bit_length) for num, bit_length in zip(row, column_bit_lengths)]
            for row in data
        ]

        formatted_data = [
            " ".join(row) for row in binary_data
        ]

        binary_string = "\n".join([j[:10] + ' ' + j[10:14] + ' ' + j[14:] for j in formatted_data])
        self.bin = binary_string
        return self.bin

    def _2_newfile(self, newfilename='output'):
        """
        Writes the binary data to a new file.

        Args:
        newfilename (str): The name of the new file (without extension).
        """
        if self.bin == None:
            self.bin = self._binary()

        newfile = newfilename + '.mc'
        with open(newfile, 'w') as file:
            file.write(self.bin)

    def _check(self):
        """
        Validates the input data.

        Returns:
        bool: True if the data is valid, False otherwise.
        """
        if self.filedata == None:
            self.filedata = self.readFile()
        data = self.filedata
        data = [list(map(int, line.split())) for line in data.split('\n')]

        all_errors = []

        for i in range(len(data)):
            errors = []

            if not (0 <= data[i][0] < 8):
                text = f'Line {i+1} : Invalid function [{data[i][0]}]'
                errors.append(text)

            if not (0 <= data[i][1] < 4):
                text = f'Line {i+1} : Invalid level [{data[i][1]}]'
                errors.append(text)
            if (data[i][1] == 1):
                text = f'Line {i+1} : The function does not support level [{data[i][1]}]'
                errors.append(text)

            if not (0 <= data[i][2] < 2048):
                text = f'Line {i+1} : Invalid value [{data[i][2]}]'
                errors.append(text)
            if (data[i][2] == 13):
                text = f'Line {i+1} Invalid operation [{data[i][2]}]'
                errors.append(text)         
            if errors:
                all_errors.extend(errors)

        if all_errors:
            print('\n'.join(all_errors))
            return False

        return True

    def _2_newfile_with_check(self, newfilename='outlab5'):
        """
        Checks the data, converts it to binary, and writes it to a new file if the data is valid.

        Args:
        newfilename (str): The name of the new file (without extension).
        """
        filename = newfilename
        bools = self._check()
        if bools:
            self._binary()
            self._2_newfile(filename)
        else:
            pass

class conv_2_mct():
    """
    This class provides functionality for converting binary data to a specific MCT file format.

    The expected file format for reading is assumed to have lines with binary values.
    Each line is expected to have the format: 
    \n
    AAA\n 
    BB\n 
    CCCDDDD\n 
    EEEE\n
    where AAA, BB, CCC, DDDD, and EEEE represent binary values.

    Example:
    \n
    000 00 000 0000 0000\n
    111 00 000 0000 0001\n
    010 01 111 1111 1111\n

    The converted MCT format will have lines with decimal values.
    Each line will have the format: A B C
    where A, B, and C represent decimal values.

    Example:\n
    0 0 0\n
    7 0 1\n
    2 31 255\n

    Usage:
    - Initialize the class with the filename.
    - Use readFile method to read and convert binary data.
    - Use convert_str method to get a formatted string of the converted data.
    - Use write_2_newfile method to write the converted data to a new file.

    Example Usage:
    filename = 'your_file_path.txt'  # Replace with your actual file path
    conv = conv_2_mct(filename)

    ### Read and convert binary data
    converted_data = conv.readFile()
    print(converted_data)

    ### Get formatted string of the converted data
    formatted_str = conv.convert_str()
    print(formatted_str)

    ### Write the converted data to a new file
    conv.write_2_newfile('output_file')
    """

    def __init__(self, filename) -> None:
        self.filename = filename
        self.data = None

    def binary_2_decimal(self, binary):
        """
        Converts a binary string to a decimal integer.

        Args:
        binary (str): The binary string to be converted.

        Returns:
        int: The decimal integer representation of the binary string.
        """
        return int(''.join(map(str, binary)), 2)

    def readFile(self):
        """
        Reads and converts binary data from the specified file.

        Returns:
        list: A list of lists containing converted decimal values.
        """
        with open(self.filename, 'r') as file:
            filedata = file.read()
            self.data = []

            for line in filedata.split('\n'):
                line = line.replace(' ', '')
                if line:
                    converted_line = [
                        self.binary_2_decimal(line[0:3]),
                        self.binary_2_decimal(line[3:5]),
                        self.binary_2_decimal(line[5:])
                    ]
                    self.data.append(converted_line)

            return self.data

    def convert_str(self):
        """
        Converts the internal data to a formatted string.

        Returns:
        str: A formatted string of the converted data.
        """
        if self.data == None:
            self.data = self.readFile()
                    
        return "\n".join([" ".join(map(str, i)) for i in self.data])

    def write_2_newfile(self, filename='phaseout'):
        """
        Writes the converted data to a new file.

        Args:
        filename (str): The name of the new file (without extension).
        """
        filename = filename + '.mct'
        with open(filename, 'w') as file:
            file.write(self.convert_str())

class mc_2_asm():
    """
    This class provides functionality for reading and writing data in a specific file format.

    The expected file format for reading is as follows:
    Line format: 
    \n
    AAA\n 
    BB\n 
    CCC\n 
    DDDD\n 
    EEEE\n
    where AAA, BB, CCC, DDDD, and EEEE represent binary values.

    Example:
    \n
    000 00 000 0000 0000\n
    111 00 000 0000 0001\n
    010 01 111 1111 1111\n
    011 10 000 0100 1111\n
    101 00 000 0111 1011\n

    Usage:
    - Initialize the class with the filename.
    - Use readFile method to read the existing file content.
    - Use writeToFile method to add a new line to the file.

    Example Usage:
    filename = 'your_file_path.txt'  # Replace with your actual file path
    mc = mc_2_asm(filename)

    ### Read existing data
    existing_data = mc.readFile()
    print(existing_data)

    ### Add a new line
    new_line = '110 11 010 1010 1101'
    mc.writeToFile(new_line)

    ### Read data after adding a new line
    updated_data = mc.readFile()
    print(updated_data)
    """
    def __init__(self, filename) -> None:
        self.filename = filename
        self.filedata = None
        self.text = None
        self.hexfiledata = None
        self.decimal_data = None

    def readFile(self):
        """
        Reads the content of the specified file.

        Returns:
        str: The content of the file.
        """
        with open(self.filename, 'r') as file:
            self.filedata = file.read()
        return self.filedata
    
    def readFile_Base16(self, filename):
        """
        function for read file base 16 
        Returns:
            values from file 
        """
        with open(filename, 'r') as file:
            self.b16file = file.read()
        return self.b16file
    
    def binary_2_decimal(self, binary):
        """
        Converts a binary string to a decimal integer.

        Args:
        binary (str): The binary string to be converted.

        Returns:
        int: The decimal integer representation of the binary string.
        """
        return int(''.join(map(str, binary)), 2)  

    def funct_(self, number):
        """
        Converts a function number to its corresponding assembly language text.

        Args:
        number (int): The function number

        Returns:
        str: The corresponding assembly language text.
        """
        if number == 0:
            self.text = 'LIT'
            return self.text
        elif number == 1:
            self.text = 'INT'
            return self.text
        elif number == 2:
            self.text = 'LOD'
            return self.text
        elif number == 3:
            self.text = 'STO'
            return self.text
        elif number == 4:
            self.text = 'CAL'
            return self.text
        elif number == 5:
            self.text = 'JMP'
            return self.text
        elif number == 6:
            self.text = 'JPC'
            return self.text
        elif number == 7:
            self.text  = 'OPR'
            return self.text

    def set_func(self):
        """
        Converts binary data to assembly language format.

        Returns:
        list: A list of lists containing converted assembly language data.
        """
        if self.filedata is None:
            self.readFile()

        data = self.filedata
        data = [list(map(str, line.split())) for line in data.split('\n')]

        self.fnl = []
        for i in range(len(data)):
            self.fnl.append([self.funct_(self.binary_2_decimal(data[i][0])),
            (self.binary_2_decimal(data[i][1])),
            self.binary_2_decimal(data[i][2] + data[i][3] + data[i][4])])
        return self.fnl

    def convert_str(self):
        """
        Converts the internal data to a formatted string.

        Returns:
        str: A formatted string of the converted data.
        """
        return "\n".join([" ".join(map(str, i)) for i in self.set_func()])

    def write_2_asm(self, filename='phaseout'):
        """
        Writes the converted data to a new file in assembly language format.

        Args:
        filename (str): The name of the new file (without extension).
        """
        filename = filename + '.asm'
        with open(filename, 'w') as file:
            file.write(self.convert_str())


class readHex():

    def __init__(self, filename) -> None:
        self.filename = filename
        self.filedata = None
        self.text = None
        self.hexfiledata = None
        self.decimal_data = None

        
    def readHexbase(self):
        """
        read file data for Heximal data\n 
        Returns:\n
            data from file heximal base
        """
        with open(self.filename, 'r') as file:
            self.hexfiledata = file.read()
        return self.hexfiledata
    
    def hex_2_bin_16bit(self, hex_str):
        binary_str = bin(int(hex_str, 16))[2:]
        padded_binary_str = binary_str.zfill(16)
        return padded_binary_str
    
    def hex_format(self):
        """
        before use this function please use function :\n
        #### readHexbase(filename)
        """
        if self.hexfiledata == None:
            self.hexfiledata = self.readHexbase()
        data = self.hexfiledata
        data = [list(map(str, line.split())) for line in data.split('\n')]
        data = [pair[0] + pair[1] for pair in zip(data[::2], data[1::2])]
        data = [hex_pair[0] + hex_pair[1] for hex_pair in data]

        edata = [format(int(hex_str, 16), '04X') for hex_str in data]
        es = [self.hex_2_bin_16bit(de) for de in edata]

        self.final_format = [[es[i][:3], es[i][3:5] ,es[i][5:]] for i in range(len(es))]

        self.decimal_data = []
        for binary_ in self.final_format:
            decimal_ = [int(binary_str, 2) for binary_str in binary_]
            self.decimal_data.append(decimal_)

        return self.decimal_data
    
    def _check(self):
        """
        Validates the input data.

        Returns:
        list: A list of error messages. An empty list indicates no errors.
        """
        if self.decimal_data is None:
            self.decimal_data = self.hex_format()

        data = self.decimal_data
        all_errors = []

        for i in range(len(data)):
            errors = []

            if not (0 <= data[i][0] < 8):
                text = f'Bytes {2*i},{2*i+1} : Invalid function [{data[i][0]}]'
                errors.append(text)

            if not (0 <= data[i][1] < 4):
                text = f'Bytes {2*i},{2*i+1} : Invalid level [{data[i][1]}]'
                errors.append(text)
            if (data[i][1] == 1):
                text = f'Bytes {2*i},{2*i+1} : The function does not support level [{data[i][1]}]'
                errors.append(text)

            if not (0 <= data[i][2] < 2048):
                text = f'Bytes {2*i},{2*i+1} : Invalid value [{data[i][2]}]'
                errors.append(text)
            if (data[i][2] == 13):
                text = f'Bytes {2*i},{2*i+1} Invalid operation [{data[i][2]}]'
                errors.append(text)

            if errors:
                all_errors.extend(errors)

        return all_errors

    def return_data_errors(self):
        errors = self._check()
        if errors:
            print('\n'.join(errors))

