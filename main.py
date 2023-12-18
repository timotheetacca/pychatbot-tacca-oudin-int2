from pychatbot_functions import *
running=False

def print_help():
  print("""\033[93m┌────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1  │ Extracts president names from a single file in the specified directory                                            │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2  │ Extracts president names from all files in the specified folder                                                   │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3  │ Associates a given name with its corresponding president                                                          │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4  │ Lists all presidents names in the specified directory                                                             │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 5  │ Converts a raw text file into a cleaned text file in the specified directory                                      │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 6  │ Converts all raw text files in a folder into cleaned text files in the specified directory                        │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 7  │ Removes punctuation from a single text file and saves the cleaned version in the specified directory              │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 8  │ Removes punctuation from all text files in a folder and saves the cleaned versions in the specified directory     │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 9  │ Computes TF (Term Frequency) scores for words in a single text file using cleaned text in the specified directory │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 10 │ Computes IDF (Inverse Document Frequency) scores for words in all cleaned text files in the specified directory   │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 11 │ Computes TF-IDF matrix for words in all cleaned text files in the specified directory                             │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 12 │ Prints the TF-IDF matrix for words in all cleaned text files in the specified directory                           │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 13 │ Identifies least important words based on TF-IDF scores in all cleaned text files in the specified directory      │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 14 │ Identifies the word with the highest TF-IDF score in all cleaned text files in the specified directory            │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 15 │ Identifies the most repeated word by a specific president in all cleaned text files in the specified directory    │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 16 │ Lists presidents who mentioned a specific word in all cleaned text files in the specified directory               │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 17 │ Identifies the first president to mention a specific word in all cleaned text files in the specified directory    │
├────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 18 │ Identifies words mentioned by all presidents in all cleaned text files in the specified directory                 │
└────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
\033[0m""")

print(f"""\033[94m


                       █████████                                              
                  ██████████████████                                        
               ████████████████████████                                     
             █████████████   █████████████                                  
           ████████████████ ███████████████                                 
          █████████████████ ████████████████                                
         ██████████████         █████████████                               
        █████████████  █████████  ████████████                              
       █████████████  █  █████  █  ████████████                             
      █████████████   █  █████  █   ████████████                            
      █████████████   ███████████   ████████████                            
      █████████████                 ████████████                            
      ███████████               █     ██████████                            
      ███████████                     ██████████                           
       ██████████ █                 █ █████████                             
        █████████ █                 █ ████████                              
         ███████  ██               ██  ██████                               
           █████  ████           ████  █████                                
            █████████████     ████████████                                  
              ██████████████████████████                                    
                ██████████████████████                                      
                     █████████████                                          
                          █████                                             
                             ███                                            
                               ██

""")

print("\033[1mWelcome to our Python Chat Bot ! You can now test some functionalities. If you want to stop testing "
      "enter 'stop'.\n\033[0m")

# Check for existing directories
directories_info = check_for_directories()

# If directories don't exist, ask the user to create them
if directories_info == False:
    directories_info = change_directories()
    # Set the directories according to the file
    directory = directories_info[0]
    cleaned_directory = directories_info[1]
    question_directory = directories_info[2]
    cleaned_question_directory = directories_info[3]
    running = True

else:
    # Set the directories according to the file
    directory = directories_info[0]
    cleaned_directory = directories_info[1]
    question_directory = directories_info[2]
    cleaned_question_directory = directories_info[3]
    # Ask if the user wants to change directories
    change_directories_answer = input(f"\033[91mExisting directories have been detected. If you wish to change directories enter '0', else press 'Enter' : \033[0m")

    while change_directories_answer != "0" and change_directories_answer != "":
        print("\033[91mInvalid input ⚠\033[0m")
        change_directories_answer = input(f"\033[91mExisting directories have been detected. If you wish to change directories enter '0', else press 'Enter' : \033[0m")

    if change_directories_answer == "0":
        directories_info = change_directories()
        # Set the directories according to the file
        directory = directories_info[0]
        cleaned_directory = directories_info[1]
        question_directory = directories_info[2]
        cleaned_question_directory = directories_info[3]

    running = True

# Clean the speeches and create a matrix
convert_folder_cleaned(directory, cleaned_directory)
remove_punctuation_folder(cleaned_directory)
matrix = tf_idf_matrix(cleaned_directory, cleaned_directory)

# User mode selection
user_mode = input("\033[94m\nIf you want to get access to our chat mode press 'Enter', else if you want to get access to all the commands of our chatbot press '0' : \033[0m")

while user_mode != "0" and user_mode != "":
    print("\033[91mInvalid input ⚠\033[0m")
    user_mode = input("\033[94m\nIf you want to get access to our chat mode press 'Enter', else if you want to get access to all the commands of our chatbot press '0' : \033[0m")
print("")

if user_mode == "":
  while running == True:
    # Iterate over each files in the question files and delete its content
    if os.path.exists(question_directory):
        # Get the list of files in the question_directory
        files = os.listdir(question_directory)
        for file_name in files:
            file_path = os.path.join(question_directory, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write('')
            else:
                print("\033[91mError, couldn't process ⚠ \033[0m")

    # User input
    request = input("\033[92mYou: \033[0m")
    if request != 'stop':
        # Tokenize the user's question and save it to a file
        question_tokenization(request, question_directory, cleaned_question_directory)

        # Create a TF-IDF matrix for the user's question
        matrix_question = tf_idf_matrix(cleaned_directory, cleaned_question_directory)

        # Generate an answer using the TF-IDF matrix
        answer = generate_an_answer(matrix, matrix_question, directory, cleaned_question_directory)

        # Display the chatbot's response
        print(f"\n\033[94mChatbot:\033[0m", refine_an_answer(cleaned_question_directory, answer), "\n")
    else:
        running=False



if user_mode == "0":
  # Display the help menu
  print_help()

  # Main loop for user interaction
  while running == True:
      # Request user input for selecting a function
      request = input("\033[94mEnter the number associated with the function. If you want the list of commands and their numbers, type 'help': \033[0m")

      if request == '1':
          # Extract president names from a single file
          filename = input("\033[94mEnter the filename: \033[0m")
          full_name = input("\033[94mPress '0' if you want to remove numbers from the file name, else press any other key: \033[0m")
          Full_name = False if full_name == '0' else True
          print(extract_president_names(directory, filename, Full_name), "\n")

      elif request == '2':
          # Extract president names from all files in a folder
          filename = input("\033[94mEnter the filename: \033[0m")
          full_name = input("\033[94mPress '0' if you want to remove numbers from the file name, else press any other key: \033[0m")
          Full_name = False if full_name == '0' else True
          print(extract_president_names_folder(directory, Full_name), "\n")


      elif request == '3':
          # Associates a given name with its corresponding president
          name = input("\033[94mWhich president's last name do you want to know ? : \033[0m")
          print(associate_name(name),"\n")

      elif request == '4':
          # Lists all presidents names in the specified directory
          print(list_presidents_names(directory),"\n")

      elif request == '5':
          # Converts a raw text file into a cleaned text file in the specified directory
          filename = input("\033[94mEnter the filename : \033[0m")
          print(convert_text_cleaned(filename, directory, cleaned_directory),"\n")

      elif request == '6':
          # Converts all raw text files in a folder into cleaned text files in the specified directory
          print(convert_folder_cleaned(directory, cleaned_directory),"\n")

      elif request == '7':
          # Removes punctuation from a single text file and saves the cleaned version in the specified directory
          filename = input("\033[94mEnter the filename : \033[0m")
          print(remove_punctuation_text(filename, cleaned_directory),"\n")

      elif request == '8':
          # Removes punctuation from all text files in a folder and saves the cleaned versions in the specified directory
          print(remove_punctuation_folder(cleaned_directory))

