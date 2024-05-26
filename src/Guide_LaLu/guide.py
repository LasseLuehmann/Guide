import argparse
from .__init__ import __version__
from .operation import path_finder, pre_content, delete_data, create_database, path_changer

def main() -> None:

    parser = argparse.ArgumentParser(description= 
         (' provides a search engine for your terminal'
         'Syntax: guide <your option> <the name wich you are searching for>'
         'guide -p Guide'))

    parser.add_argument('path', nargs='*')
    parser.add_argument('-v', '--version', action='store_true', help='version of Guide LaLu')
    parser.add_argument('-c', '--code', action='store_true', help='start your editor in the provided direction')
    parser.add_argument('-l', '--ls', action='store_true', help='display all non hidden content of the provided direction')
    parser.add_argument('-la', '--lsall', action='store_true', help='display all content of the provided direction including hidden')
    parser.add_argument('-p', '--pwd', action='store_true', help='display the Path of the provided direction')
    parser.add_argument('-m', '--mv', action='store_true', help='use the move option to rename your chosen destiny')
    parser.add_argument('-mt', '--mvto', action='store_true', help='use the move -t option to replace your chosen directory')
    parser.add_argument('-j', '--journey', action='store_true', help='prints your searching history')
    parser.add_argument('-x', '--exterminate', action='store_true', help='used delete your history')

    args = parser.parse_args()
    object = None

    create_database()

    if args.version:
        print('','-'*7,'\n|',__version__,'|','\n','-'*7)
    elif args.journey:
        data = pre_content()
        for row in data:
            print(f'| {row[0]}\t| {row[1]}\t| {row[2]}\t\t| {row[3]}\n','-'*100)
    elif args.exterminate:
        delete_data()
        create_database()
        print('','-'*38,'\n|','Your histoy was successfully deleted!|','\n','-'*38)
    else:
        for name in args.path:
            object = name
        if object:
            if args.code:
                com = 'code'
                data = path_finder(object, com)
                path_changer(path=data[0],com=data[1])
            elif args.ls:
                com = 'ls'
                data = path_finder(object, com)
                path_changer(path=data[0],com=data[1])
                print('','-'*70,'\n')
            elif args.lsall:
                com = 'ls -a'
                data = path_finder(object, com)
                path_changer(path=data[0],com=data[1])
                print('','-'*70,'\n')
            elif args.pwd:
                com = 'pwd'
                data = path_finder(object, com)
                print(f'{path_changer(path=data[0],com=data[1])}','\n','-'*70,'\n')
            elif args.mv:
                com = 'mv'
                data = path_finder(object, com)
                print(f'{path_changer(path=data[0],com=data[1])}','\n','-'*70,'\n')
            elif args.mvto:
                com = 'mv -t'
                data = path_finder(object, com)
                print(f'{path_changer(path=data[0],com=data[1])}','\n','-'*70,'\n')

    

if __name__ == '__main__':
    main()