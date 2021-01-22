
def remove_space(str_1):
    new_str = str_1.split()
    new_str = " ".join(new_str)
    return new_str

def remove_space2(str_1):
    new_str = ""
    count = 0
    check_index = 0
    for letter in str_1:
        if letter == " ":
            if (check_index == 0) and count == 0:
                count += 1
                pass
            elif count == 0:
                new_str += letter
                count += 1
        else:
            count = 0
            new_str += letter
        
        check_index += 1
    return new_str

# ===== test case 0 ============
print("============= Test case 0 =============\n")
print(remove_space("Bonjour dirac haha"))
print(remove_space2("Bonjour dirac haha"))

# ===== test case 1 ============
print("\n============= Test case 1 =============\n")
print(remove_space("Bonjour           dirac        haha"))
print(remove_space2("Bonjour          dirac        haha"))


# ===== test case 2 ============
print("\n============= Test case 2 =============\n")
print(remove_space("         Bonjour               dirac        haha"))
print(remove_space2("        Bonjour               dirac         haha"))

# ===== test case 3 ============
print("\n============= Test case 3 =============\n")
print(remove_space("        Bonjour         dirac   haha        "))
print(remove_space2("       Bonjour         dirac   haha        "))

# ===== test case 4 ============
print("\n============= Test case 4 =============\n")
print(remove_space("Bonjourdirachaha                "))
print(remove_space2("Bonjourdirachaha               "))