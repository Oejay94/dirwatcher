# dirwatcher

## Summary of the project.
The goal for this project is to scan a directory for a sepcific, or magic, word. The terminal will continue logging, letting the user know on which line the word can be found. If the user were to create a '.txt' file, within a folder, and add their choice of word to the CMD line, the program will then search for that word exclusively. Of course, in order to do this, the user would have to restart the terminal and tell it, that is the CMD Line, which word to search for and which folder it is within. Also, the terminal will let the user if they delete a file or the folder entirely if the CMD Line is told to be watching that directory.

## Example CMD Line for watching a directory 
python3 dirwatcher.py watchdir Joey

## Example Output on Terminal for searching of the magic word
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


## Example Output on Terminal if file or directory is removed
2020-01-16 12:35:27.928 dirwatcher.py INFO    [MainThread  ] 
----------------------------------------------------
   Running dirwatcher.py
   Started on 2020-01-16T12:35:27.928042
----------------------------------------------------

2020-01-16 12:35:27.929 dirwatcher.py INFO    [MainThread  ] Watch Dir: watchdir, File Ext: .txt, Polling Int: 1.0, Magic Txt: Joey
2020-01-16 12:35:27.929 dirwatcher.py INFO    [MainThread  ] Watching new file: watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 1 in watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 5 in watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 14 in watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 20 in watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 21 in watchdir/sample.txt
2020-01-16 12:35:27.931 dirwatcher.py INFO    [MainThread  ] Found the Joey on 22 in watchdir/sample.txt
2020-01-16 12:35:35.945 dirwatcher.py INFO    [MainThread  ] Removed deleted file: watchdir/sample.txt
2020-01-16 12:35:43.962 dirwatcher.py ERROR   [MainThread  ] [Errno 2] No such file or directory: 'watchdir'
2020-01-16 12:35:44.963 dirwatcher.py ERROR   [MainThread  ] [Errno 2] No such file or directory: 'watchdir'
^C2020-01-16 12:35:45.490 dirwatcher.py WARNING [MainThread  ] Received SIGINT
2020-01-16 12:35:45.971 dirwatcher.py INFO    [MainThread  ] 
----------------------------------------------------
   Stopped dirwatcher.py
   Uptime was 0:00:00.001647
----------------------------------------------------