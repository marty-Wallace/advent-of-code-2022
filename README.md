# advent-of-code-2018
Advent of Code 2018

A simple python framework for Advent Of Code 2018. 
Downloads input files and runs each day of code. 

To run create a virtual environment:
```commandline
$ python3 -m venv venv
```
For bash: 
```commandline
$ source venv/bin/activate
```
For windows:
```commandline
$ venv\Scripts\activate.ps1
$ #or
$ venv\Scripts\activate.bat
```
Then install the requirements: 
```commandline
$ pip install -r requirements.txt
```

If you want to be able to download input files automatically from https://adventofcode.com. First copy the `.secrets_template` file
then put your session token from your browser session into the file:
```commandline
$ cp .secrets_template .secrets
$ vim .secrets
```

Once your session token is stored in the .secrets file, when you run the code it will automatically download the input for that day if it hasn't already done so. 

Now you can run tests or run the actual Advent of Code input for each day. 


If I wanted to run against the actual input for day 1 part 1: 
```commandline
$ python main.py 1 1
```

If I wanted to run tests for day 1 part 2:
```commandline
$ python main.py --test 1 2
```

To auto-submit your answer for day 1 part 1:
```commandline
$  python main.py --submit 1 1
```

If you want to run more tests against a specific days problems, you can add input and output files to the `input/test/{day_number}/{part_number}/(input|output){test_number}`
If you add an input file without an output file, things may explode. 

