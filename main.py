from pychatbot_functions import *
running = True

help_user = """
If you want to see the first name of a president, enter '1'
If you want to see the list of presidents, enter '2'
If you want to see the TF-IDF matrix, enter '3'
If you want to see the least important words, enter '4'
If you want to see the most important word, enter '5'
If you want to know the most repeated word by a president, enter '6'
If you want to know the list of presidents who have mentioned a chosen word, enter '7'
If you want to see who is the first president to mention a chosen word, enter '8'
If you want to see the words mentioned by all presidents, enter '9'
"""

print("Welcome to our Python Chat Bot ! You can now test some functionalities. If you want to stop testing "
      "enter 'stop'.\n")

# Get the directory and cleaned_directory from the use
directory = str(input("Before you begin, please enter the name of the file where your texts are located : "))
while not os.path.exists(directory):
  print(f"You don't have any folder named '{directory}' ⚠ ")
  directory = str(input("Before you begin, please enter the name of the file where your texts are located : "))

cleaned_directory = str(input("Please enter a name of the folder where the files will be treated : "))


# Clean the speeches and create a matrix
convert_folder_cleaned(directory,cleaned_directory)
remove_punctuation_folder(cleaned_directory)
matrix=tf_idf_matrix(cleaned_directory)

print("\nThe list of the functions you can test is the following :\n")
print(help_user,"\n")

while running == True:
    user_input = str(input("Enter the number associated to the function. If you want the list of commands and their numbers type 'help' : "))
    print()
    if user_input == 'stop':
        running = False
    elif user_input == 'help':
        print(help_user)

    elif user_input == "1":
        name_pres = str(input("Which president's last name do you want to know ? : "))
        print(associate_name(name_pres), "\n")

    elif user_input == "2":
        print(list_presidents_names(directory), "\n")

    elif user_input == "3":
        print_tf_idf_matrix(cleaned_directory,matrix)
        print("\n")

    elif user_input == "4":
        print(least_important_words(cleaned_directory,matrix), "\n")

    elif user_input == "5":
        print(highest_tf_idf_score(cleaned_directory, matrix), "\n")

    elif user_input == "6":
        president_name = str(input("Which president do you want to know about ? : "))
        all_word = str(input("Type 'True' if you want to have all words included or 'False' if you want just important words : "))
        # Makes sure the user enters the right value
        while all_word not in ["True", "False"]:
            all_word = str(input("Type 'True' if you want to have all words included or 'False' if you want just important words : "))

        print(most_repeated_word_by_president(directory,president_name ,cleaned_directory, all_word, matrix), "\n")

    elif user_input == "7":
        chosen_word = str(input("What is the word you are looking for ? : "))
        print(presidents_who_mentioned(directory, cleaned_directory, chosen_word), "\n")

    elif user_input == "8":
        word=str(input("What is the word you are looking for ? : "))
        print(first_president_to_mention(cleaned_directory, word, matrix), "\n")

    elif user_input == "9":
        print(word_mentioned_by_all(directory, cleaned_directory, matrix), "\n")

    elif user_input < "1" or user_input > "10" or user_input not in ["stop","help"]:
        print("Invalid input ⚠")


print("Thanks for using our chat-bot !")