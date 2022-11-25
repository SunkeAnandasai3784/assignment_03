def upper_lower(letter):
    ul={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in letter:
        if i.isupper():
           ul["UPPER_CASE"]+=1
        elif i.islower():
           ul["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", letter)
    print ("No. of Upper case characters : ", ul["UPPER_CASE"])
    print ("No. of Lower case Characters : ", ul["LOWER_CASE"])

upper_lower('The quick Brown Fox')
