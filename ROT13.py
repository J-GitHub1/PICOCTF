capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
phrase_length = 0
pass_phrase = ""
phrase=""
letter=""
new_letter=""
phrase = ("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}")

phrase_length = len(phrase)

print(phrase_length)

for i in range(phrase_length):
    
    letter = phrase[i]
    if letter in capital_letters:
        position = capital_letters.index(letter)
        position  = (position + 13) % 26
        new_letter = capital_letters[position]
    
        
    elif letter in lowerCase_letters:
            position = lowerCase_letters.index(letter)
            position  = (position + 13) % 26
            new_letter = lowerCase_letters[position]
            
    else:
        new_letter = letter
    pass_phrase=pass_phrase + new_letter

print(pass_phrase)
