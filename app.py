from sentence import create_sentence


ui1 = input("Please input the sentence you'd like to use ")

ui2 = input("Please input the word you'd like to use ")

ui3 = input("Please input the number you'd like to use ")

ui4 = input("Please input the symbol you'd like to use ")

def create_password():
    sent_letters = create_sentence(ui1)
    letters_result = []

    finished = False
    i = 0

    while finished == False:
        if i >= len(sent_letters) and i >= len(ui2):
            finished = True
        if i <= len(sent_letters) - 1:
            letters_result.append(sent_letters[i])
        if i <= len(ui2) - 1:
            letters_result.append(ui2[i])
        i = i + 1
    
    print(letters_result)


create_password()


