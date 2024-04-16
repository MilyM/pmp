# author: Milosz Cygan

# functions
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def get_unique(data):
    return set(data)

def first_last(txt):
    return txt[0], txt[-1]

def main():
    a = 10
    b = 2
    txt = 'random_txt'

    d_list = [1, 4, 4]
    d_tuple = ('a', 'd', 'g', 'a')

    print(f'{a} + {b} = {sum(a,b)}')
    print(f'{a} - {b} = {sub(a,b)}')
    print(f'Unique from: {d_list} are: {get_unique(d_list)}')
    print(f'First and last letter from {txt}, are: {first_last(txt)}')



if __name__ == '__main__':
    main()