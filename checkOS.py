import os
print os.name

from sys import platform as _platform
print _platform

if _platform == "linux" or _platform == "linux2":
	  pass
elif _platform == "darwin":
  	pass
elif _platform == "win32":
  	pass
else :
	pass
