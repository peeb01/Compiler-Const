filepath = 'D:\Book\Computer Eng\Compiler\LAB\ex.txt'

class Lab3:
    def __init__(self, filename) -> None:
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def check_data(self, data):
        try:
            data = int(data)
            if 0 <= data <= 2**31 - 1:
                return True
            else:
                print(f'{data} is not in the range [0, 2**31 - 1].')
        except ValueError:
            print(f'{data} is not an integer.')

    def analyzer2newfile(self, output_filename='output.txt'):
        data = self.read_file()
        if self.check_data(data):
            with open(output_filename, 'w') as file:
                file.write(data)


lab_instance = Lab3(filepath)
lab_instance.analyzer2newfile('hola.txt')
