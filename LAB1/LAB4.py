filepath = 'D:\Book\Computer Eng\Compiler\LAB\lab4src.txt'

def readFile(filename : str) -> str:
    with open(filename, 'r') as file:
        filedata = file.read()
        return filedata
    
def spl_data(values: str) -> list:
    arr = [subs for subs in values.split(' ') if subs]
    return arr

def check(data) -> tuple:
    try: 
        integer = int(data)
        return ('number' , integer)
    except ValueError:
        if data == '+' or data == '-' or data == '*' or data == '/' or data == '**' or data == '%' :
            return ('operator', f"{data}")
        elif data == '(':
            return ('left-parenthesis', f"{data}")
        elif data == ')':
            return ('right-parenthesis', f"{data}")
        else:
            return ('identifier', f"{data}") 

def name(values : str) -> list:
    ds = spl_data(str(values))
    result = []
    for data in ds:
        dt = check(data)
        result.append(dt)
    return result

def print_ls(value : list):
    for data in value:
        print(data)

values = readFile(filepath)
data = name(values)
# print(spl_data(values))
print_ls(data)
