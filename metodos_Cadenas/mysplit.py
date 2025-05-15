def mysplit(strng):
    #
    #def mysplit(strng):
    result = []
    word = ""
    
    for char in strng:
        if char != " ":
            word += char
        else:
            if word != "":
                result.append(word)
                word = ""
    
    if word != "":
        result.append(word)
        
    return result

    #


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))