filepath = 'D:\Book\Computer Eng\Compiler\LAB\ex.txt'

def readFile(file_open : str):
    """
    Args : file name : str
    Returns : data from file
    """
    with open(file_open, 'r') as file:
        filedata = file.read()
        return filedata.split(' ')


#1.1
def writeFile(file_out : str, data : str):
    """
    Args 1 : Name output file .txt
    Args 2 : Data to write file  

    Got a new file's clone data from read file
    """
    with open(file_out, 'w') as file:
        file.write(data)

# writeFile('exce.txt', readFile('ex.txt'))

# for n in readFile('ex.txt').split(','):
#     print(int(n))

#1.2
def write_to_py(out_file_name : str, data):
    """
    Args 1 : name file Example "Name"
    Args 2 : data
    """
    _py = '.py'
    out_file = out_file_name + _py
    with open(out_file, 'w') as file:
        file.write(f'print({data})')

# write_to_py('/Program/testout', readFile('ex.txt'))


#1.3
def write_to_c(out_file_name : str, data):
    """
    Args 1 : name file Example "Name"
    Args 2 : data
    """
    _C = '.c'
    out_file = out_file_name + _C
    simple_text = f"""#include <stdio.h>

int main() {{
    char data[] = "{data}";
    printf("%s", data);
    return 0;
}}
"""
    with open(out_file, 'w') as file:
        file.write(simple_text)

# write_to_c('testC', readFile('ex.txt'))


#1.4
def write_to_cpp(out_file_name : str, data):
    """
    Args 1 : name file Example "Name"
    Args 2 : data
    """
    _cpp = '.cpp'
    out_file = out_file_name + _cpp
    simple_text = f"""#include <iostream>

using namespace std;
int main(){{
    char data[] = "{data}";
    cout << data << endl;
    return 0;
}}
"""
    with open(out_file, 'w') as file:
        file.write(simple_text)

# write_to_cpp('testcpp', readFile('ex.txt'))


def write_to_go(out_file_name : str, data):
    """
    Args 1 : name file Example "Name"
    Args 2 : data
    """
    _go = '.go'
    out_file = out_file_name + _go
    simple_text = f"""package main

import "fmt"
func main() {{
    fmt.Println("{data}")
}}
"""
    with open(out_file, 'w') as file:
        file.write(simple_text)

# write_to_go('testgo', readFile('ex.txt'))