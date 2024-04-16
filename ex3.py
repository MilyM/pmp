# author: Milosz Cygan

def do_some(*args, **kwargs):

    print('keywords arguments')

    for key, value in kwargs.items():
        print(key, value)
    
    sum = 0
    print('positional arguments')

    for arg in args:
        arg_type = type(arg)

        if arg_type is int or arg_type is float:
            sum += arg

        elif arg_type is str:
            if arg.isdigit():
                sum += float(arg)
        print(args)
        
    print(f'Sum of numeric args is: {sum}')

    





if __name__ == '__main__':
    do_some(1, 1.1, 'a', '3', i=1, b=2, c='a')