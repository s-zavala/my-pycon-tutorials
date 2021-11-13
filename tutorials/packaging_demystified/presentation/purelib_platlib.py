# purelib and platlib are two folders used as python library locations. They are often the same directory.
import sys, sysconfig

print(sysconfig.get_path('purelib'))
print(sysconfig.get_path('platlib'))

