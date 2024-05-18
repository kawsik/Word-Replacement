def replacement():
    sentence = input("Enter some sentence: ")
    before = input("Word you want to replace: ")
    after = input("Word you want to replace it with: ")
    print(f"{sentence.replace(before,after)}\nHere we replaced the word {before} with {after}.")

replacement()