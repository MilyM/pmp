# author: Milosz Cygan

def write_menu():
    print('===Menu===')
    print('1. Write to file')
    print('2. Read the file')
    print('3. Close')


def write_to_file(text: str):
    file = input('Enter the filename with extension: ')
    with open(file, 'w') as f_open:
        f_open.write(text)
        print('File created')

def read_file():
    file = input('Enter the filename with extension: ')
    with open(file, 'r') as f_read:
        lines = f_read.readlines()
    return lines

def main():
    is_working = True
    write_menu()

    while is_working:
        operation = -1
        try:
            operation = int(input('Enter the operation number: '))
        except Exception as e:
            print(e)
        
        if operation == 1:
           to_write = input('Enter the text to write: ')
           write_to_file(to_write)

        elif operation == 2:
            lines = read_file()
            for line in lines:
                print(line.replace('\n', ''))
        elif operation == 3:
            exit()
        else:
            print('Bad operation number!')
        

if __name__ == '__main__':
    main()