import argparse
from .__init__ import __version__
from .operation import path_finder

def main() -> None:

    parser = argparse.ArgumentParser(description= ' provides a search engine for your terminal')

    parser.add_argument('-v', '--version', action='store_true', help='version of progcount')
    parser.add_argument('-c', '--code', action='store_true', help='start your editor in the provided direction')
    parser.add_argument('-l', '--ls', action='store_true', help='display all non hidden content of the provided direction')
    parser.add_argument('-p', '--pwd', action='store_true', help='display the Path of the provided direction')

    args = parser.parse_args()

    if args.version:
        print(__version__)
    else:
        object = input('Where do you want to go: ')
        if args.code:
            com = 'code'
            path_finder(object, com)
        elif args.ls:
            com = 'ls'
            path_finder(object, com)
            print('\n')
        elif args.pwd:
            com = 'pwd'
            print(f'{path_finder(object, com)}\n')
    # else:
    #     com = input('What would you like to do(pwd/ls/code): ')
    
    # if com == '':
    #     com = 'pwd'
    # print(f'\n{path_finder(object, com)}\n')

if __name__ == '__main__':
    main()