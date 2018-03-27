def status(mood, days):
    if(mood==True):
        if(days>=3):
            return "Working"
        elif(days==2):
            return "Working"
        elif(days==1):
            return "Done"
        else:
            return "Error"
    else:
        if(days>=3):
            return "Nothing"
        elif(days==2):
            return "Nothing"
        elif(days==1):
            return "Overnight Working"
        else:
            return "Error"

print(status(True, 3))
print(status(True, 1))
print(status(False, 5))
print(status(False, 1))
