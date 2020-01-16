# dirwatcher

## Summary of the project.
The goal for this project is to scan a directory for a sepcific, or magic, word. The terminal will continue logging, letting the user know on which line the word can be found. If the user were to create a '.txt' file, within a folder, and add their choice of word to the CMD line, the program will then search for that word exclusively. Of course, in order to do this, the user would have to restart the terminal and tell it, that is the CMD Line, which word to search for and which folder it is within. 

## Example CMD Line 
python3 dirwatcher.py watchdir Joey

## Example Output on Terminal
2020-01-16 12:20:08.947 dirwatcher.py INFO    [MainThread  ] 
----------------------------------------------------
   Running dirwatcher.py
   Started on 2020-01-16T12:20:08.947341
----------------------------------------------------

2020-01-16 12:20:08.949 dirwatcher.py INFO    [MainThread  ] Watch Dir: watchdir, File Ext: .txt, Polling Int: 1.0, Magic Txt: Joey
2020-01-16 12:20:08.949 dirwatcher.py INFO    [MainThread  ] Watching new file: watchdir/sample.txt
2020-01-16 12:20:08.950 dirwatcher.py INFO    [MainThread  ] Found the Joey on 1 in watchdir/sample.txt
2020-01-16 12:20:08.950 dirwatcher.py INFO    [MainThread  ] Found the Joey on 5 in watchdir/sample.txt
2020-01-16 12:20:08.950 dirwatcher.py INFO    [MainThread  ] Found the Joey on 14 in watchdir/sample.txt
^C2020-01-16 12:25:05.240 dirwatcher.py WARNING [MainThread  ] Received SIGINT
2020-01-16 12:25:05.802 dirwatcher.py INFO    [MainThread  ] 
----------------------------------------------------
   Stopped dirwatcher.py
   Uptime was 0:00:00.001702