def count_letters(str_input):
    new_dic = {}
    str_input = str_input.lower()
    for letter in str_input:
        if letter == " ":
            continue
        if letter in list(new_dic.keys()):
            new_dic[letter.upper()] += 1
        else:
            new_dic[letter.upper()] = 1 
    return new_dic

# ===== test case 0 =============
print("=========== Test case 0 ============\n")
print(count_letters("my first name is dirac"))

# ===== test case 1 =============
print("\n=========== Test case 1 ============\n")
print(count_letters("       my           first      name        is        dirac       "))

# ===== test case 2 =============
print("=========== Test case 2 ============\n")
print(count_letters("MMMMmmmmmy first name is Dirac. I am a congolese born in Kinshasa."))