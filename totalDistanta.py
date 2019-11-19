



>>> def distDisplay(s):
...     t = 1
...     d = s*t
...     h = 1
...     while d < 400:
...             print ("in", h, "hour(s), you traveled", d, "km")
...             t += 1
...             d = s*t
...     if d >= 400:
...             print ("you traveled 400 or more km, go to sleep")
...
