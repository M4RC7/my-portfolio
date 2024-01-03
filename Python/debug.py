DEBUG = True
# def debug(str):
#   if DEBUG: print(str)

x = 5
if DEBUG: print(x)

### You'll often need to print values in default output for debugging (or use a proper debugger -RECOMMENDED), but you'll always (trust me) forget to erase them once you're done debugging. Also, you may want to keep them for future debugging.
### So an alternative to not trash your programs with useless debugging \"print()\" functions is to hold them behind a debug boolean, like the suggested methods above: Once you're done debugging, simply \"turn off\" the \"debug\" variable.