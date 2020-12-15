is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or are tall")
else:
    print("You are neither mail nor tall")


def tall_male_checker(is_male, is_tall):
    if is_male and is_tall:
        print("You are a tall male")
    elif is_male and not is_tall:
        print("You are a short male")
    elif not is_male and is_tall:
        print("You are not a male but are tall")
    else:
        print("You are either not male and not tall")


tall_male_checker(True, True);
tall_male_checker(True, False);
tall_male_checker(False, True);
tall_male_checker(False, False);