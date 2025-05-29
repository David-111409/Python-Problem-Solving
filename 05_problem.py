
'''
Mangle The String

Create a function that takes a string and replaces every letter 
with the letter following it in the alphabet ("c" becomes "d", "z" becomes "a", "b" becomes "c", etc). 
Then capitalize every vowel (a, e, i, o, u) and return the new modified string.

Examples
mangle("Fun times!") ➞ "GvO Ujnft!"

mangle("The quick brown fox.") ➞ "UIf rvjdl cspxO gpy."

mangle("Omega") ➞ "Pnfhb"

Notes
If a letter is already uppercase, return it as uppercase (regardless of being a vowel).
"y" is not considered a vowel.
'''

def mangle(string):
    new_string = ""
    
    for c in string:
        if c.lower() == "z" :
            new_string += "A"
            
        else:
            if c.isalpha():
                letter = chr(ord(c) + 1)
                
                if letter in "aeiou":
                    new_string += letter.upper()
                else:
                    new_string += letter
                    
            else:
                new_string += c
        
    return new_string


print(mangle("y"))
print(mangle("Fun times!") == "GvO Ujnft!")
print(mangle("Omega") == "Pnfhb")
print(mangle("I will never be this young again. Ever. Oh damn... I just got older.") == "J xjmm Ofwfs cf UIjt zpvOh bhbjO. Fwfs. PI EbnO... J kvtU hpU pmEfs.")
print(mangle("Should we start class now, or should we wait for everyone to get here?") == "TIpvmE xf tUbsU dmbtt Opx, ps tIpvmE xf xbjU gps fwfszpOf Up hfU Ifsf?")
print(mangle("Check back tomorrow; I will see if the book has arrived.") == "DIfdl cbdl Upnpsspx; J xjmm tff jg UIf cppl Ibt bssjwfE.")
print(mangle("The lake is a long way from here.") == "UIf mblf jt b mpOh xbz gspn Ifsf.")
print(mangle("It was getting dark, and we weren't there yet.") == "JU xbt hfUUjOh Ebsl, bOE xf xfsfO'U UIfsf zfU.")
print(mangle("The mysterious diary records the voice.") == "UIf nztUfsjpvt Ejbsz sfdpsEt UIf wpjdf.")
print(mangle("Cats are good pets, for they are clean and are not noisy.") == "DbUt bsf hppE qfUt, gps UIfz bsf dmfbO bOE bsf OpU Opjtz.")
print(mangle("abcz")  , "bcdA", "Don't forget that \"z\" becomes \"a\"!")
print(mangle("ABCZ") , "BCDA", "If a letter is already uppercase, return it as uppercase.")
