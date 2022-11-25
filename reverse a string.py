def reverse(stg):

    rstg = ''
    index = len(stg)
    while index > 0:
        rstg += stg[ index - 1 ]
        index = index - 1
    return rstg
print(reverse('1234abcd'))
