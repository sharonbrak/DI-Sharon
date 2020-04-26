
matrix = [
'7 3',
'Tsi',
'h%x',
'i #',
'sM ',
'$a ',
'#t%',
'ir!'
]

secretcode0 = ''
secretcode1 = ''
secretcode2 = ''

def decrypt(col, secretcode):
    for x in matrix:
        if x[col].isalpha():
            secretcode = secretcode + x[col]
        else:
            if len(secretcode)>0:
                if secretcode[-1] != ' ':
                    secretcode = secretcode + ' '
    return secretcode

secretcode0 = decrypt(0, secretcode0)
secretcode1 = decrypt(1, secretcode1)
secretcode2 = decrypt(2, secretcode2)

print(secretcode0+secretcode1+secretcode2)