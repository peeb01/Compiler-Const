class command:
    def __init__(self) -> None:
        self.filename = None

    def load(self, filename):
        with open(filename, 'r') as file:
            self.file_data = file.read()
        return self.file_data
    

ax = command()
data = ax.load('D:\Book\Computer Eng\Compiler\LAB4\sample.mc')
print(data)

