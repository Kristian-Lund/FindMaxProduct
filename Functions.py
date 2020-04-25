def cleanString(StringToClean):
    ItemsToRemove = ['"','\\n', ';','+']
    for Item in ItemsToRemove:
        StringToClean = StringToClean.replace(Item, '')
    CleanString = StringToClean
    return CleanString

#Obsolete if using colorama....
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
