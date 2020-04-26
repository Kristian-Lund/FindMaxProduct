
from Functions import cleanString
from ListClass import ListClass



WindowDim = 4
f = open('./input.txt','r')
DirtyString = f.read()
CleanString = cleanString(DirtyString)
List = ListClass(CleanString, WindowDim)


print(List)
print(List.getWindowCalcultions())









