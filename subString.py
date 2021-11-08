s = "abddherfsstemxwz"

def subString(string):
    firstString = string[0]
    copyFirstString = ""
    x = 1
    for item in string[x:len(string)]:
        if firstString[-1] != item:
            firstString += item
        else:
            copyFirstString = firstString
            if len(firstString) > len(copyFirstString):
                pass
            else:
                firstString = string[x]
        x += 1
    if len(firstString) > len(copyFirstString):
        return firstString
    else:
        return copyFirstString

print(subString(s))