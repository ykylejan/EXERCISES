country = input("Enter country: ")
vowel = "aeiouAEIOU"

if country.isalpha():
    if country.startswith(vowel):
        print("l", country)
    else:
        if country.endswith("e"):
            if country == "Belize":
                print("le", country)
            elif country == "Cambodge":
                print("le", country)
            elif country == "Mexique":
                print("le", country)
            elif country == "Mozambique":
                print("le", country)
            elif country == "Zaïre":
                print("le", country)
            elif country == "Zimbabwe":
                print("le", country)
            else:
                print("la", country)
        elif country.endswith("s"):
            print("les", country)
        else:
            print("le", country)
else:
    print("Error, country names only.")



