from sentence import create_sentence


ui1 = input("Please input the sentence you'd like to use ")

sent_letters = create_sentence(ui1.lower())

if len(sent_letters) < 2:
    ui1 = input("Sentence must be at least two words ")
    sent_letters = create_sentence(ui1.lower())

ui2 = input("Please input the word you'd like to use ")

ui3 = input("Please input the number you'd like to use ")

if ui3.isnumeric() == False:
    ui3 = input("Number must be a number ")

ui4 = input("Please input any additional symbols, numbers, or letters you'd like to add to the end ")

def create_password():
    
    word = ui2.lower()
    letters_result = []

    finished = False
    i = 0

    while finished == False:
        if i >= len(sent_letters) and i >= len(word):
            finished = True
        if i <= len(sent_letters) - 1:
            letters_result.append(sent_letters[i])
        if i <= len(word) - 1:
            letters_result.append(word[i])
        i = i + 1

    index = 0
    for each in letters_result:
        if index % 3 == 0:
            del letters_result[index]
            letters_result.insert(index, each.upper())
        index = index + 1
    

    letters_result.append(ui3)
    letters_result.append(ui4)
    result = "".join(letters_result)
    
    print(f"Password: {result}")


create_password()


