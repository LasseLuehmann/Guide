import os
from pathlib import Path
import re
import csv
from datetime import datetime

database = Path.joinpath(Path.home(), '.Guide_LaLu_database')
file = Path.joinpath(database, 'journey.csv')

def create_database(database=database, file=file):
    """This function runs automaticaly when guide starts. It makes sure that the datafile exists
    and if it doesn't it creates it. 
    """
    if not Path.exists(file):
        os.system(f'mkdir {database} && cd {database} && touch journey.csv')
        with open(file, mode='w') as new_db:
            csv.writer(new_db).writerow(['Date    ', 'Time    ', 'Command','Path'])

def delete_data(db=database, file=file):
    """ This function is used to delete the datafile in order to delete the preexisting content.
    Related to '-x'
    """
    os.system(f'cd {Path.home()} && rm -r {db}')
        
def pre_content(db=file):
    """ This function read the hole datafile and return the whole content in a List of List.
    Related to '-j'
    """
    content = []
    with open(db) as precon:
        while line := precon.readline():
            if len(line) == 0:
                continue
            else:
                sepline = line.split(',')
                content.append([sepline[0], sepline[1], sepline[2], sepline[3].strip('\n')])
    return content

def for_database(path: str,com, db=file):
    """ In this function we collect the chosen path and the given command 
    and together with the current time and date it save this information in the datafile.
    Runs automaticaly by '-p', '-l', '-la', '-c', '-m' and '--mt'
    """
    if com == '':
        return
    else:
        now = datetime.now()
        con = [[now.strftime('%d/%m/%Y'), now.strftime('%H:%M:%S'), com, str(path)]]
        with open(db, mode= 'a') as destin:
            save = csv.writer(destin)
            save.writerows(con)

def path_finder(object: str, com: str, here=Path.home()):
    """ This function takes the requested object and tries to find it
    in your data. It takes also the command wich should be excecuted to provid it 
    to the next function. The search starts from the home directory. 
    Runs automaticaly by '-p', '-l', '-la', '-c', '-m' and '--mt'
    """
    cache = []
    sear = here.rglob('*')
    for found in sear:
        if re.search('dist', str(found)) or found.name.startswith('.') or found.name.endswith('.egg-info'):
            continue
        elif re.search(object, str(found.name)):
            cache.append(found)
    return folder_search(cache, com)
        
def folder_search(cache: list, com: str):
    """ This function takes all pathes wich contain the requested object and the command 
    wich should be excecuted. The user will be asked to deside wich path should be used.
    Runs automaticaly by '-p', '-l', '-la', '-c', '-m' and '--mt'
    """
    if len(cache) >= 1:
        count = 1
        for opt in cache:
            print(count, opt)
            count += 1
        ask = input('choose your desired path with entering the related number: ')
        for_database(cache[int(ask)-1], com)
        print('\n','-'*70)
        return cache[int(ask)-1], com
    else:
        print('No match for your choice')

def path_changer(path: Path, com: str):
    """ This function anilyse wich command is requested. Depending on that it will excecute
    the related excecuting function. If pwd was choosen it will directly return the path.
    Runs automaticaly by '-p', '-l', '-la', '-c', '-m' and '--mt'
    """
    if path.name.startswith('__'):
        upath = path.parent
    else:
        upath = path
    if com == 'pwd':
        return upath
    elif com == 'code':
        return execute_code(upath, com)
    elif com == 'ls' or com == 'ls -a':
        return execute_ls(upath, com)
    elif com == 'mv':
        return execute_mv(upath, com)
    elif com == 'mv -t':
        return execute_mvto(upath, com)

def execute_code(upath: Path, com: str):
    """ This function is the excecuting function for the code command.
    Related to '-c'
    """
    if upath.is_file():
        order = com + ' ' + str(upath)
    else:
        order = 'cd ' + str(upath) + ' && ' + com + ' .'
    return os.system(order)

def execute_ls(upath: Path, com: str):
    """ This function is the excecuting function for the ls command.
    Related to '-l' and '-la'
    """
    if upath.is_file():
        print('Your path leads to a file, no ls available! \nls will be excecuted from the parent\n')
        order = com + ' ' + str(upath.parent)
    else: 
        order = com + ' ' + str(upath)
    return os.system(order)

def execute_mv(upath: Path, com: str):
    """ This function is the executing funtion for the mv command.
    Related to '-m'
    """
    new_name = input('how would you like to call your destiny: ')
    order = com + ' ' + str(upath.name) + ' ' + new_name
    return os.system(order)

def execute_mvto(upath: Path, com: str):
    """ This function is the esecutin function for the mv -t command.
    Related to '-mt'
    """
    new_directory = input('Wich folder should be the destiny: ')
    dest = path_finder(object=new_directory, com='')
    order = com + ' ' + str(dest[0]) + ' ' + str(upath)
    os.system(order)
    return f'({upath.name}) was moved successfully to ({dest[0]})'

