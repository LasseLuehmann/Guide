import os
from pathlib import Path
import re
import csv
from datetime import datetime

db = Path.joinpath(Path.cwd(), 'src', 'Guide_LaLu', 'journey.csv')

def create_new_database(db=db):
    with open(db, mode='w') as new_db:
        csv.writer(new_db).writerow(['Date    ', 'Time', 'Command    ','Path'])
        
def pre_content(db=db):
    content = []
    with open(db) as precon:
        while line := precon.readline():
            if len(line) == 0:
                continue
            else:
                sepline = line.split(',')
                content.append([sepline[0], sepline[1], sepline[2], sepline[3].strip('\n')])
    return content

def for_database(com: str,pat, db=db):
    content = []
    now = datetime.now()
    dat= now.strftime('%-d/%-m/%Y')
    tim = now.strftime('%-H:%-M')
    precon = pre_content(db)
    for list in precon:
        content.append(list)
    strpat = str(pat)
    content.append([dat, tim, strpat, com])
    with open(db, mode= 'w') as destin:
        save = csv.writer(destin)
        save.writerows(content)

def path_finder(object: str, com: str, here=Path('/home')):
    """ This function takes the requested object and tries to find it
    in your data. It takes also the command wich should be excecuted to provid it 
    to the next function. The search starts from the home directory. 
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
    """
    if len(cache) >= 1:
        count = 1
        for opt in cache:
            print(count, opt)
            count += 1
        ask = input('choose your desired path with entering the related number: ')
        for_database(cache[int(ask)-1], com)
        print('\n','-'*70)
        return path_changer(cache[int(ask)-1], com)
    else:
        print('No match for your choice')

def path_changer(path: Path, com: str):
    """ This function anilyse wich command is requested. Depending on that it will excecute
    the related excecuting function. If pwd was choosen it will directly return the path.
    """
    if path.name.startswith('__'):
        upath = path.parent
    else:
        upath = path
    if com == 'pwd':
        return upath
    elif com == 'code':
        return excecut_code(upath, com)
    elif com == 'ls' or com == 'ls -a':
        return excecut_ls(upath, com)

def excecut_code(upath: Path, com: str):
    """ This function is the excecuting function for the code command."""
    if upath.is_file():
        order = com + ' ' + str(upath)
    else:
        order = 'cd ' + str(upath) + ' && ' + com + ' .'
    return os.system(order)

def excecut_ls(upath: Path, com: str):
    """ This function is the excecuting function for the ls command."""
    if upath.is_file():
        print('Your path leads to a file, no ls available! \nls will be excecuted from the parent\n')
        order = com + ' ' + str(upath.parent)
    else: 
        order = com + ' ' + str(upath)
    return os.system(order)


