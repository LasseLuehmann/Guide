# 0.0.8 New Features
> fixed the database issue: a folder and a csv file will be created in the home diectory to contain the database

# Guide

This programm is ment to guide you through your terminal with just a few arguments.
The programm starts from home directory using Path from pathlib and will use rglob with unpack from pathlib to search for the package/module.
If multiple packages/modules exists it will list the pathes to all of them.
It will search for names wich contain the name wich was given with regex.
When the pachkage/module was found then it will use os to execute your given command in the found package/module

## Options

The programm itself takes a option and then ask for the name wich your are sarcing for: 
   1. the command you could use.
      - pwd: `-p | --pwd`
      - code: `-c | --code`
      - ls: `-l | --ls` -> ls -a: `-la | --lsall`
      - version: `-v | --version`
      - history: `-j | --journey`
      - delete: `-x | exterminate`
   2. the package/module wich you are searching for 

### how to use 

1. open your terminal and type `guide` followed by the option
2. type a part of the name of the package/module you would like to find, for example `Gui`
3. now the program starts with the search and provide you with a `numbered collection` of all the pathes wich contain the provided sample of the name
4. you make your choice by giving the related number and the program will execute the `command` in the choosen `path`

```bash
>> guide -p
>> Where do you want to go: Guide
>> 1 /home/dci-student/DCI/Python/Projects/Guide
>> choose your desired path with entering the related number: 1
>> /home/dci-student/DCI/Python/Projects/Guide
```

Because this module uses regex to find the object we are able to use regex syntax within the name.
regex syntax are for example 
- `\w`: any alphanumeric charecters
- `\W`: any charecter that is not represented with `\w`
- `\d`: any digit
- `^`: startswith
- `$`: endswith
- `*`: 0 to infinite
- `+`: 1 to infinite

If you are uncertain how the name is spelled or seperated you can concider these options.
> Remember: in order to use a backslash `\` you have double it like `\\W`

### Imports used

> 1. pathlib
> 2. os
> 3. re
> 4. csv
> 5. datetime
