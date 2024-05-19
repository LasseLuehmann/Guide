import argparse
from .__init__ import __version__
from .operation import path_finder, pre_content, create_new_database, create_database

def main() -> None:

    parser = argparse.ArgumentParser(description= ' provides a search engine for your terminal')

    parser.add_argument('-v', '--version', action='store_true', help='version of Guide LaLu')
    parser.add_argument('-c', '--code', action='store_true', help='start your editor in the provided direction')
    parser.add_argument('-l', '--ls', action='store_true', help='display all non hidden content of the provided direction')
    parser.add_argument('-la', '--lsall', action='store_true', help='display all content of the provided direction including hidden')
    parser.add_argument('-p', '--pwd', action='store_true', help='display the Path of the provided direction')
    parser.add_argument('-j', '--journey', action='store_true', help='prints your searching history')
    parser.add_argument('-x', '--exterminate', action='store_true', help='used delete your history')

    args = parser.parse_args()

    create_database()

    if args.version:
        print(__version__)
    elif args.journey:
        data = pre_content()
        for row in data:
            print(f'| {row[0]}\t| {row[1]}\t\t| {row[2]}\t\t| {row[3]}\n','-'*100)
    elif args.exterminate:
        create_new_database()
        print('Your histoy was successfully deleted!')
    else:
        object = input('Where do you want to go: ')
        if args.code:
            com = 'code'
            path_finder(object, com)
        elif args.ls:
            com = 'ls'
            path_finder(object, com)
            print('','-'*70,'\n')
        elif args.lsall:
            com = 'ls -a'
            path_finder(object, com)
            print('','-'*70,'\n')
        elif args.pwd:
            com = 'pwd'
            print(f'{path_finder(object, com)}','\n','-'*70,'\n')
    

if __name__ == '__main__':
    main()