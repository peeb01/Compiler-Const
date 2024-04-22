from func import command

cm = command()

print('\n\n*** Welcome to a PL/0 P-code machine shell! ***\n')

while(1):
    exited = ['quit', 'quit()', 'exit()', 'exit']
    commands = input('?>>>  ')
    if commands in exited:
        print('\n\nExit P-code machine shell...\n')
        break
    if commands == 'load' or commands == 'load()':
        filename = input('Enter the files name : ')
        data = cm.load(filename)
        # print(data)
    if commands == 'dump' or commands == 'dump()':
        # data = cm.load('sample.mc')
        cm.dump()
    if commands == 'step' or commands == 'step()':
        lis = ['quit', 'quit()', 'exit', 'exit()']
        cm.step()
            
    if commands == 'run' or commands == 'run()':
        cm.run()