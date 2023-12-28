filepath = 'D:\Book\Computer Eng\Compiler\LAB\ex.txt'

def readFile(filename : str):
    """
    Args : file name : str
    Returns : data from file
    """
    with open(filename, 'r') as file:
        filedata = file.read()
        return int(filedata)

def check_num(number):
    return 0 <= number <= 2**31 - 1



def write2Cpp(filename : str, data : int):
    """
    Args 1 : file name : will convert to Cpp , Example input filename = "Holla"
    Args 2 : data to write in file : integer
    Returns: New file .cpp for urn print(data)
    """
    filename = filename + '.cpp'
    text = f"""#include <iostream>

using namespace std;
int main(){{
    int data = {data};
    cout << "the number is : " << data << endl;
    return 0;
}}
"""
    if check_num(data) == True:
        with open(filename, 'w') as file:
            file.write(text)
            print(f"Write file {filename} sucessful.")      
    else : 
        print("The size of the numbers is not in the range 0 to 2,147,483,647.")

number = readFile(filepath)
write2Cpp("TestLab2", number)