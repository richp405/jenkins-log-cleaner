# jenkins-log-cleaner

Tkinter-based tool to clean up Pretty Print output, which gets mangled in pytest logs.  Partly, this is for me to play with tkinter.

The problem:
------------
When running a jenkins build, especially with projects using pytest or ansible test, you get unreadable output.  You can even use 'pretty print' and it looks bad in the log output.  I got tired of "copy-paste, straighten out linefeeds, work on indents in data".

So, I made a little cleaner-upper with a tkinter front-end... paste a 'paragraph' from a log view in, hit 'process', and if it was pretty-printed, it will clean up cr/lf, make indents, and all in a little dialog.

It's crude and simplistic, but useful.  Since I'm doing a bit of ci/cd work and analysis, I figure I will probably crank out a few of these.



