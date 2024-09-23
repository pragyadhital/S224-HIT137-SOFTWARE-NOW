def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    return decrypted_text

# Example encrypted text (from the image):
encrypted_text = """
tybony_inenvoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebrff_ahzoref():
    tybony tybony_inenvoyr
    ybpny_inenvoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenvoyr > 0:
        vs ybpny_inenvoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenvoyr)
        ybpny_inenvoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inenvoyr = 10
    zl_qvpg['xrl4'] = ybpny_inenvoyr

zbqvsl_qvpg(5)

qrs hcangr_tybony():
    tybony tybony_inenvoyr
    tybony_inenvoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
    cevag("5 abg sbeq va gur qvpgvbanel!")
cevag(tybony_inenvoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

key = 13
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
