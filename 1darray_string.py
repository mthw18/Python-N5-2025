thisArray = ["kirsty","amelia","james","alie","euan","joshua"]
mostCharacters = len(thisArray[0])
pos = 0
for index in range(1,len(thisArray)):
    if len(thisArray[index]) > mostCharacters:
        mostCharacters = len(thisArray[index])
    pos = index
print(thisArray[pos],"has most number of characters", mostCharacters)