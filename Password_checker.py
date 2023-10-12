"""
This program checks to ensure that a user enters a strong
password. It uses the criteria shown below:
Alphabets: 7 characters (one capital letter and six lower letters)
- Digits: 2
- Special character: 1 (!, @, #, $, %, ^, &, * )
- Spaces:0
- The total length of a normal password should be 10.
"""

while True:
    special_char = "!@#$%^&*"
    alphabet_cnt = 0
    upper = 0
    lower = 0
    digit_cnt = 0
    space_cnt = 0
    spec_char = 0

    password = input("Please type password: ")
    print("--------------------------------")

    # iterate the password and count the chars based on category
    for char in password:
        if char.isalpha() and char.isupper():
            alphabet_cnt += 1
            upper += 1
        elif char.isalpha() and char.islower():
            alphabet_cnt += 1
            lower += 1
        elif char.isdigit():
            digit_cnt += 1
        elif char.isspace():
            space_cnt += 1
        elif char in special_char:
            spec_char += 1

    if len(password) != 10:
        print(f"Wrong password. Please type again.")
        print(f"Alphabet number: {alphabet_cnt} (capital: {upper}, lower: {lower})")
        print(f"Digit number: {digit_cnt}")
        print(f"Space number: {space_cnt}")
        print(f"Special char number: {spec_char}")
        print("--------------------------------")
    elif alphabet_cnt != 7 or upper != 1 or lower != 6:
        print(f"Wrong password. Please type again.")
        print(f"Alphabet number: {alphabet_cnt} (capital: {upper}, lower: {lower})")
        print(f"Digit number: {digit_cnt}")
        print(f"Space number: {space_cnt}")
        print(f"Special char number: {spec_char}")
        print("--------------------------------")
    elif digit_cnt != 2:
        print(f"Wrong password. Please type again.")
        print(f"Alphabet number: {alphabet_cnt} (capital: {upper}, lower: {lower})")
        print(f"Digit number: {digit_cnt}")
        print(f"Space number: {space_cnt}")
        print(f"Special char number: {spec_char}")
        print("--------------------------------")
    elif spec_char != 1:
        print(f"Wrong password. Please type again.")
        print(f"Alphabet number: {alphabet_cnt} (capital: {upper}, lower: {lower})")
        print(f"Digit number: {digit_cnt}")
        print(f"Space number: {space_cnt}")
        print(f"Special char number: {spec_char}")
        print("--------------------------------")
    elif space_cnt != 0:
        print(f"Wrong password. Please type again.")
        print(f"Alphabet number: {alphabet_cnt} (capital: {upper}, lower: {lower})")
        print(f"Digit number: {digit_cnt}")
        print(f"Space number: {space_cnt}")
        print(f"Special char number: {spec_char}")
        print("--------------------------------")
    else:
        break

print("Normal password.")
