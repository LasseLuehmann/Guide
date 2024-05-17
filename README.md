# Guide

This programm is ment to guide you through your terminal with just a few arguments

## Options

The programm itself takes two arguments 
   1. the command you would like to use.
      - pwd: `-p | --pwd`
      - code: `-c | --code`
      - ls: `-l | --ls`
      - version: `-v | --version`
   2. the package/module wich you are searching for 

## How to achieve 
The programm starts from home directory using Path from pathlib and will use rglob with unpack from pathlib to search for the package/module.
If multiple packages/modules exists it will list the pathes to all of them.
It will search for names wich contain the name wich was given via regex.
When the pachkage/module was found then it will use os.system to print path leading to the found package/module
If a command was given it will be executed instead of pwd.

## Imports used

> 1. pathlib
> 2. os
> 3. re

### how to use 

1. open your terminal and type `guide` followed by the option
2. type a part of the name of the package/module you would like to find, for example `Gui`
3. now the program starts with the search and provide you with a `numbered collection` of all the pathes wich contain the provided sample of the name
4. you make your choice by giving the related number and the program will execute the `command` in the choosen `path`

```bash
>> guide -p
>> Where do you want to go: 16\W05
>> 1 /home/dci-student/DCI/Python/15_Database/16.05
>> choose your desired path with entering the related number: 1
>> /home/dci-student/DCI/Python/15_Database/16.05
```

Because this module uses regex to find the object we are able to use regex syntax within the name.
regex syntax are for example 
- `\w`: any alphanumeric charecters
- `\W`: any charecter that is not represented with `\w`
- `\d`: any digit
If you are uncertain how the name is spelled or seperated you can concider these options.
