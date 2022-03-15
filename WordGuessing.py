'''
cresting a game of guessiing a word
'''
import random


def word_guess():

    s_chance = 1
    while s_chance <= 3:     # 3 chances
        print("it is chance : ", s_chance, " to guess whloe word")
        print("enter whole word")
        s_result = input()       # input sstring as whole
        if s_result == list_of_word[random_index]:

            # converting winner name into Upper case just for look
            name_in_upper = name_of_player.upper()
            print("................ ", name_in_upper,
                  " wins...............guessed right............")
            break
        else:
            s_chance = s_chance+1

    if s_chance <= 3:
        quit()              # to exit if win
    else:

        print("you can't where not able to guess right word , word was=",
              list_of_word[random_index])
        quit()            # exit if loss


print("enter your name : ")
name_of_player = input()        # taking players name
print("hello ", name_of_player, " time to play words guessing / hangsman!")

print("START GUESSING ")

list_of_word = ["mukesh", "google", "dhano", "shrikant", "bmw", "amresh",
                "omen", "black", "amazon", "startup"]  # randome list for words

random_index = random.randint(0, 9)    # picking a randome word


print("Word to be Guessed is of given Character(1 underscore means 1 character)")

# print list_of_word[random_index]
for i in list_of_word[random_index]:  # printing the underscore_for the randome word
    print("_"),


print("Guess the word you have 10 chances")

number_of_chance = 1
result = []
# a list which will get the charchter input of user
for i in list_of_word[random_index]:
    result.append("_")

# print result
while number_of_chance <= 10:  # for 10 chances
    print("does you guessed the proper word if yes then press 1 , you will get last 3 chances to guess correct word ")
    print("press 1 else press anyother number to contiune as normal latter by latter guessing ")
    switch_choice = input()                # for direct word guessing
    if switch_choice == 1:
        word_guess()
    # else:
    #     print("")

    print("Chance : ", number_of_chance,
          " Guess the Latter which might be present in given word : ")
    value_by_player = input()   # player input
    j = 0
    flag = 1
    # to store the coreect input in new list
    for i in list_of_word[random_index]:
        if i == value_by_player:
            flag = 2
            result[j] = value_by_player

        j = j+1

    if flag == 2:           # printing the correct or wrong about input
        print("Correct......")
        for i in result:
            print(i,)

    else:
        print("Oops......")
        for i in result:
            print(i,)

   # word=str(list_of_word[random_index])  using this we can convert a list element into string

    # using this we are converting a input list into a string
    word = ''.join(str(e) for e in result)

    # while c<word.__len__():

    if list_of_word[random_index] == word:  # checking for a winner
        flag2 = 1
    else:
        flag2 = 2

    if flag2 == 1:  # printing a winner
        # converting winner name into Upper case just for look
        name_in_upper = name_of_player.upper()
        print(name_in_upper,
              " wins!!!!!!!!! guessed right.")
        break

    number_of_chance = number_of_chance+1

print("you can't where not able to guess right word , word was =",
      list_of_word[random_index])
