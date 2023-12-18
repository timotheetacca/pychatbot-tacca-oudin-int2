import os, math

def file_count(directory,extension=""):
    """
    Count the number of file with a given extension or not

    Parameters
    ----------
    directory (str): The directory containing cleaned text files
    extension (str): The file name extension

    Returns
    ----------
    int: The number of file in the given directory
    """
    file_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(extension):
              file_count += 1
    return file_count

def extract_president_names(directory, filename, Full_name=False):
  """
  Extracts president names from text files in a directory

  Parameters
  ----------
  directory (str): The directory containing text files
  filename (str): The specific filename to search for in the directory
  Full_name (bool): Remove or not the numbers at the ends of a filename

  Returns
  ----------
  str: A message with the extracted president name
  or
  str: A message indicating an error
  """
  files_presidents = []
  message = "Error, couldn't process ⚠ "

  if not os.path.exists(directory):
      message = f"You don't have any folder named '{directory}' ⚠ "

  else:
      found_file = ""
      for files in os.listdir(directory):
            if filename == files and files.endswith(files.split(".")[-1]):
                found_file = files

      if found_file != "":
          # Every file is named: "Nomination_{name}" so we split the file name using _ as space
          name_parts = found_file.split("_")
          president_name = ((name_parts[1]).split("."))[0]

          # Remove the numbers at the end of the file name
          if Full_name == False:
              numbers = "0123456789"
              while president_name[-1] in numbers:
                  president_name = president_name[:-1]

          message = president_name
      else:
          message = f"No file with the name '{filename}' found in the directory ⚠"
  return message


def extract_president_names_folder(directory, Full_name=False):
    """
    Extracts president names from text files in a directory

    Parameters
    ----------
    directory (str): The directory containing text files
    Full_name (bool): Remove or not the numbers at the ends of a filename

    Returns
    ----------
    str: A message with the extracted president name
    or
    str: A message indicating an error
    """
    files_presidents = []
    message = "Error, couldn't process ⚠ "

    if not os.path.exists(directory):
        message = f"You don't have any folder named '{directory}' ⚠ "

    else:
        files_presidents = []
        for filename in os.listdir(directory):
            if filename.endswith(filename.split(".")[-1]):
                files_presidents.append(extract_president_names(directory, filename, Full_name))
        message = files_presidents
    return message


def associate_name(name):
    """
    Associates a president's last name with their first name

    Parameters
    ----------
    name (str): The last name of the president

    Returns
    ----------
    str: A message with the president's first name
    or
    str: A message indicating an error
    """
    message= "Error, couldn't process ⚠ "
    first_names = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if name in first_names:
        # If the name exists in the dictionary, return the first name and a message
        message= first_names[name]+" "+name+"'s first name is : "+first_names[name]
    else:
        # If the name doesn't exist in the dictionary, return an error message
        message=f"The name '{name}' doesn't exist in our data base ⚠ "
    return message




def list_presidents_names(directory):
    """
    Lists unique president names extracted from text files in a directory

    Parameters
    ----------
    directory (str):  The directory containing text files

    Returns
    ----------
    str: A message with the list of unique president names 
    or
    str: A message indicating an error 
    """
    message = "Error, couldn't process ⚠ "
    if not os.path.exists(directory):
        message = f"You don't have any folder named '{directory}' ⚠ "
    else:
      # Make a set of the extract_president_names() to avoid duplicates and then print a list of name separeted by comas
      message = list(set((extract_president_names_folder(directory))))
    return message


def convert_text_cleaned(filename, directory, cleaned_directory):
    """
    Convert a text file to lowercase

    Parameters
    ----------
    filename (str): The name of the text
    directory (str):  The directory containing text files
    cleaned_directory (str): The directory containing cleaned text files

    Returns
    ----------
    str: A message indicating the status of the operation
    """
    message= "Error, couldn't process ⚠ "
    # Check if the 'cleaned' directory exists; if not, create it
    if not os.path.exists(cleaned_directory):
        os.makedirs(cleaned_directory)

    # Check if the input file exists
    if not os.path.exists(os.path.join(directory, filename)):
        message= f"There is no file named '{filename}' in '{directory}' ⚠ "
    else:
        # Open the input file in read mode
        input_filepath = os.path.join(directory, filename)
        with open(input_filepath, "r", encoding="utf-8") as not_cleaned_file:
            text = not_cleaned_file.read()

        cleaned_text = ""
        for char in text:
            # Check if the character is a capital letter or accented capital letter
            if ord("A") <= ord(char) <= ord("Z") or ord("À") <= ord(char) <= ord("ß"):
                cleaned_text += chr(ord(char) + 32)  # Convert uppercase letters to lowercase
            else:
                cleaned_text += char

        # Define the new filename for the cleaned file
        name_parts = filename.split(".txt")
        new_filename = f"{name_parts[0]}_cleaned.txt"
        new_filepath = os.path.join(cleaned_directory, new_filename)

        # Write the cleaned text to the output file
        with open(new_filepath, "w", encoding="utf-8") as cleaned_file:
            cleaned_file.write(cleaned_text)

        message= f"File '{filename}' has been successfully converted to lowercase and saved in '{cleaned_directory}'."
    return message



def convert_folder_cleaned(directory, cleaned_directory):
    """
    Converts text files from a directory and saves them in a cleaned directory

    Parameters
    ----------
    directory (str):  The directory containing text files
    cleaned_directory (str): The directory containing cleaned text files

    Returns
    ----------
    str: A message indicating the status of the operation
    """
    message= "Error, couldn't process ⚠ "
    # Check if there are documents in the 'speeches' directory
    if not os.path.exists(directory):
        message= f"You don't have any cleaned text in '{directory}' ⚠ "
    else:       
      # Read files from the 'speeches' folder
      for filename in os.listdir(directory):
          filepath = os.path.join(directory, filename)
          convert_text_cleaned(filename, directory,cleaned_directory)
          message= f"'{directory}' as been successfully cleaned"
    return message



def remove_punctuation_text(filename, cleaned_directory):
    """
    Remove punctuation and accents from a text 

    Parameters
    ----------
    filename (str): The name of the text
    clean_directory (str): The directory containing cleaned text files

    Returns
    ----------
    str: A message indicating the status of the operation 
    """
    message= "Error, couldn't process ⚠ "
    # Check if the 'cleaned' directory exists
    if not os.path.exists(cleaned_directory):
        message= f"You don't have any cleaned text in '{cleaned_directory}' ⚠ "
    elif not os.path.exists(os.path.join(cleaned_directory, filename)):
          message= f"There is no file named '{filename}' in '{cleaned_directory}' ⚠"
    else:
        with open(os.path.join(cleaned_directory, filename), "r", encoding="utf-8") as not_removed_punctuation:
            # Read the original text from the file

            text = not_removed_punctuation.read()
            cleaned_text = ""
            spacing = " \n\t"
            special_treatment = "'-_"
            accents = {"à": "a", "è": "e", "ù": "u", "â": "a", "é": "e", "ê": "e", "î": "i", "ô": "o", "û": "u",
                       "ë": "e", "ç": "c", "œ": "oe"}

            # Analyze each character in the text
            for char in text:
                if char in accents:
                    cleaned_text += accents.get(char, '*')  # Replace all accents with their non-accented versions
                elif (ord("a") <= ord(char) <= ord("z")) or (char in spacing) or (ord('0') <= ord(char) <= ord('9')):
                    cleaned_text += char  # Keep lowercase letters, special characters, and numbers
                elif char in special_treatment:
                    cleaned_text += " "  # Replace "'" and "-" with a space
                else:
                    cleaned_text += ""  # Exclude all other characters

            # Define the new filename for the cleaned file
            new_filename = filename.split("_")[0] + "_" + (filename.split("_")[1])  + "_removed_punctuation.txt"
            new_filepath = os.path.join(cleaned_directory, new_filename)


            # Write the cleaned text to a new file
            with open(new_filepath, "w") as cleaned_file:
                cleaned_file.write(cleaned_text)

            message= f"File '{filename}' has been successfully processed to remove punctuation and saved in '{cleaned_directory}'"
    return message


def remove_punctuation_folder(cleaned_directory):
    """
    Removes punctuation from text files in a directory

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files

    Returns
    ----------
    str: A message indicating the status of the operation 
    """
    message= "Error, couldn't process ⚠ "
    # Check if the 'cleaned' directory exists
    if not os.path.exists(cleaned_directory):
        message= f"You don't have any cleaned text in '{cleaned_directory}' ⚠ "

    # Read files from the 'cleaned' folder
    for filename in os.listdir(cleaned_directory):
        filepath = os.path.join(cleaned_directory, filename)
        remove_punctuation_text(filename, cleaned_directory)
        message=f"'{cleaned_directory}' files no longer have accents"
    return message


def tf_score(filename, cleaned_directory):
    """
    Calculate the TF score for each word 

    Parameters
    ----------
    filename (str): The name of the cleaned text file
    clean_directory (str): The directory containing cleaned text files

    Returns
    ----------
    dict: A dictionary containing words as keys and their TF scores as values
    or
    str: A message indicating an error
    """

    message= "You don't have any cleaned text ⚠ "
    # Initialize an empty dictionary to store word counts
    words_dictionary = {}

    # Create the file path to the cleaned text file
    filepath = os.path.join(cleaned_directory, filename)

    # Check if the file exists
    if not os.path.isfile(filepath):
        message= f"There is no file named '{filename}' in '{cleaned_directory}' ⚠ "

    else:
        with open(filepath, "r") as tf_file:
            # Read the file and split it into words
            text = tf_file.read()
            words = text.split()

            # Analyze each word in the text
            for word in words:
                # If the word is already in the dictionary add 1 to its count
                if word in words_dictionary:
                    words_dictionary[word] += 1
                else:
                    # If the word is not in the dictionary add it with a count of 1
                    words_dictionary[word] = 1
        message= words_dictionary
    return message


def idf_score(cleaned_directory):
    """
    Calculate the IDF score for each word

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files

    Returns
    ----------
    dict: A dictionary containing words as keys and their IDF scores as values
    or
    str: A message indicating an error
    """
    message= "You don't have any cleaned text ⚠ "
    if not os.path.exists(cleaned_directory):
        message= f"You don't have any folder named '{cleaned_directory}' ⚠ "
    else:
        # Initialize an empty dictionary to store word counts in documents
        words_in_documents = {}

        # Count the number of documents and create a set of words in each document
        number_of_files= file_count(cleaned_directory,"_removed_punctuation.txt")
        for filename in os.listdir(cleaned_directory):
            # Check if the file is a punctuation-removed text file
            if filename.endswith("_removed_punctuation.txt"):
                filepath = os.path.join(cleaned_directory, filename)
                with open(filepath, 'r') as file:
                    text = file.read()
                    words = set(text.split())

                    # Calculate in how many files the word appears
                    for word in words:
                        if word in words_in_documents:
                            # If the word is already in the dictionary, increment its count by 1 
                            words_in_documents[word] += 1
                        else:
                            # If the word is not in the dictionary, add it
                            words_in_documents[word] = 1

        # Calculate IDF for each word
        word_idf = {}
        for word, value in words_in_documents.items():
            word_idf[word] = math.log10(number_of_files / value)
        message= word_idf
    return message

def tf_idf_matrix(cleaned_directory_idf, cleaned_directory_tf):
  """
  Calculate the TF-IDF matrix

  Parameters
  ----------
  cleaned_directory_idf (str): The directory containing cleaned text files for the IDF
  cleaned_directory_tf (str): The directory containing cleaned text files for the TF

  Returns
  ----------
  list: TF-IDF matrix represented as a list of lists.
  or
  str: A message indicating an error
  """
  message = "Error, couldn't process ⚠ "
  if not os.path.exists(cleaned_directory_idf):
      message = f"You don't have any folder named '{cleaned_directory_idf}' ⚠ "
  elif not os.path.exists(cleaned_directory_tf):
      message = f"You don't have any folder named '{cleaned_directory_tf}' ⚠ "

  else:
      # Get IDF score
      idf_scores = idf_score(cleaned_directory_idf)

      # Initialize an empty TF-IDF matrix
      tf_idf_matrix = []
      for filename in os.listdir(cleaned_directory_tf):
          if filename.endswith("_removed_punctuation.txt"):
              # Get the TF scores for the document
              tf_scores = tf_score(filename, cleaned_directory_tf)

              for key in idf_scores.keys():
                  found = False

                  # Check if the word is already in the TF-IDF matrix
                  for i in range(len(tf_idf_matrix)):
                      if tf_idf_matrix[i][0] == key:
                          if key in tf_scores:
                              # If the word is used in this text, add the TF-IDF score to the matrix
                              tf_idf_matrix[i][1].append(idf_scores[key] * tf_scores[key])
                          else:
                              # Else, add "None" to indicate the word is not in this document
                              tf_idf_matrix[i][1].append(None)
                          found = True

                  # If the word is not in the TF-IDF matrix, create a new row
                  if not found:
                      if key in tf_scores:
                          # If the word is used in this text, add the TF-IDF score to a new row
                          tf_idf_matrix.append([key, [idf_scores[key] * tf_scores[key]]])
                      else:
                          # Else add "None" to indicate the word is not in this document
                          tf_idf_matrix.append([key, [None]])
      message = tf_idf_matrix   
  return message


def print_tf_idf_matrix(cleaned_directory_idf, cleaned_directory_tf, matrix):
    """
    Prints the TF-IDF matrix for the documents in a directory

    Parameters
    ----------
    clean_directory_idf (str): The directory containing cleaned text files for the IDF
    clean_directory_tf (str): The directory containing cleaned text files for the TF
    matrix (list): The TF-IDF matrix. If not provided, the function will generate it.

    Returns
    ----------
    print row by row the matrix
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    # Check if the 'cleaned' directory exists
    if not os.path.exists(cleaned_directory_idf):
      message = f"You don't have any folder named '{cleaned_directory_idf}' ⚠ "
    elif not os.path.exists(cleaned_directory_tf):
      message = f"You don't have any folder named '{cleaned_directory_tf}' ⚠ "

    else:
        # Get the list of filenames from the directory
        filenames = []
        for filename in os.listdir(cleaned_directory_tf):
            if filename.endswith("_removed_punctuation.txt"):
                filenames.append(filename.split('_')[1].split('.')[0])

        # Calculate the maximum length of word for clean alignment
        max_word_length = max(len(row[0]) for row in matrix)

        # Generate the header 
        header = [f"│ {' ':<{max_word_length}}"]
        for filename in filenames:
            header.append(f"{filename:^{max_word_length}}")  # Center each filename in a cell of width max_word_length
        print(" │ ".join(header) + " │")

        # Print the matrix rows
        for row in matrix:
            word = row[0]
            values = row[1]
            word_padding = ' ' * (max_word_length - len(word))  # Calculate padding for the word
            word_output = f"│ {word}{word_padding} │"
            formatted_values = []
            for value in values:
                if value is not None:
                    # Cut the number so it fit in the matrix
                    if value <= 10:
                        formatted_values.append(f"{value:.4f}")
                    else:
                        formatted_values.append(f"{value:.3f}")
                else:
                    formatted_values.append(" ")

            values_output = ' │ '.join(f"{val:<{max_word_length}}" for val in formatted_values)
            row_output = f"{word_output} {values_output} │"
            print(row_output)
            message = ""

    return message



def least_important_words(cleaned_directory, matrix):
    """
    Generates a list of words with the least importance, where their TF-IDF = 0 in all files

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files
    matrix (list): A matrix containing TF-IDF scores

    Returns
    ----------
    str: A message indicating the list of least important words
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
        message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    else:
        # Count the number of files
        number_of_files=file_count(cleaned_directory,"_removed_punctuation.txt")

        least_important_words = []
        for row in matrix:
            # Stores the word if its TF-IDF = 0 in all files
            if row[1] == [0.0] * number_of_files: 
                least_important_words.append(row[0])

        least_important_words = ", ".join(least_important_words)
        message= least_important_words
    return message




def highest_tf_idf_score(cleaned_directory, matrix):
    """
    Determine the word with the highest TF-IDF score

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files
    matrix (list): A matrix containing TF-IDF scores

    Returns
    ----------
    str: A message indicating the word with the highest TF-IDF score and its score
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
        message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    else:

        # Create and store the matrix if the user didn't create one
        if matrix == None:
            matrix = tf_idf_matrix(cleaned_directory,cleaned_directory)
            print("New matrix created")

        # Count the number of files
        number_of_files=file_count(cleaned_directory,"_removed_punctuation.txt")

        max_score = 0.0
        max_word = ""
        for row in matrix:
            for i in range(number_of_files): 
                # Check if the value is not None and greater than the current max
                if row[1][i] is not None and row[1][i] > max_score:
                    max_score = row[1][i]
                    max_word = row[0]

        message= [max_word,max_score]
    return message




def most_repeated_word_by_president(directory, president_name, cleaned_directory ,matrix, least_important_included=True):
    """
    Determine what's the most repeated word among the important ones

    Parameters
    ----------
    directory (str):  The directory containing text files
    president_name (str): The name of the president to analyze
    cleaned_directory (str): The directory containing cleaned text files
    least_important_included (bool): Display a word that doesn't appear in the least_important_word()
    matrix (list): A matrix containing TF-IDF scores

    Returns
    ----------
    str: A message indicating the most repeated word by a president with their frequency
    or
    str: A message indicating an error
    """
    message= "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
      message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    if not os.path.exists(directory):
      message = f"You don't have any folder named '{directory}' ⚠ "
    else:
      # Check if the president_name is in the list of presidents
      if president_name in list_presidents_names(directory):
          total_tf_score = {}

          for filename in os.listdir(directory):
            # Check if the file name starts with "Nomination_{president_name}" in case presidents have multiple speeches
            if filename.startswith(f"Nomination_{president_name}"):
                # Update the total_tf_score dictionary with TF scores of the current file
                tf_scores = tf_score("".join(filename.split(".")[:-1]) + "_removed_punctuation.txt", cleaned_directory)  # Calculate TF scores
                for word, score in tf_scores.items():
                    if word in total_tf_score:
                        total_tf_score[word] += score
                    else:
                        total_tf_score[word] = score

          # Find the most repeated word in the combined TF scores
          most_repeated_word = max(total_tf_score, key=total_tf_score.get)
          # Check if the most repeated word is among the least important words
          if total_tf_score == {}:
              message = f"No significant word found for {president_name}."
          if least_important_included==False:
              while most_repeated_word in least_important_words(cleaned_directory, matrix):
                  # Remove the most repeated word from the total_tf_score dictionary
                  del total_tf_score[most_repeated_word]
                  # Check if there are still words left in the dictionary and find the new most repeated word
                  most_repeated_word = max(total_tf_score, key=total_tf_score.get)


          frequency = total_tf_score[most_repeated_word]
          if least_important_included==True:
              message= f"The most repeated word among all words by {president_name} is '{most_repeated_word}', he repeated it {frequency} times."
          else:
              message= f"The most repeated among the important words by {president_name} is '{most_repeated_word}', he repeated it {frequency} times."
      else:
          # If the president_name is not in the list, return an error message
          message= f"The name '{president_name}' doesn't exist in our database ⚠ "

    return message



def presidents_who_mentioned (directory, cleaned_directory, chosen_word):
    """
    Determine which presidents mentioned a specific word, and who mentioned it the most

    Parameters
    ----------
    directory (str):  The directory containing text files
    clean_directory (str): The directory containing cleaned text files
    chosen_word (str): The word to search for

    Returns
    ----------
    str: A message indicating the presidents who mentioned the word and who mentioned it the most with their frequency
    or
    str: A message indicating an error
    """
    message= "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
      message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    elif not os.path.exists(directory):
      message = f"You don't have any folder named '{directory}' ⚠ "
    else:
      chosen_word_dict = {}
      for filename in os.listdir(directory):
        president_name=extract_president_names(directory, filename) 

        # Calculate TF scores for the current file 
        tf_scores = tf_score("".join(filename.split(".")[:-1]) + "_removed_punctuation.txt", cleaned_directory)

        # Update chosen_word_dict with TF scores of the current file
        for word, score in tf_scores.items():
            if word == chosen_word:
                if president_name in chosen_word_dict:
                    chosen_word_dict[president_name] += score
                else:
                    chosen_word_dict[president_name] = score

      if chosen_word_dict == {}:
        message= f"The word '{chosen_word}' hasn't been mentioned by any president available in our database ⚠ "
      else:
        # Find the list of presidents who mentioned the chosen word
        list_president = ", ".join(list(chosen_word_dict.keys()))

        # Find the president who mentioned the word the most
        repeated_it_the_most = max(chosen_word_dict, key=chosen_word_dict.get)
        frequency = chosen_word_dict[repeated_it_the_most]
        message = f"The word '{chosen_word}' has been mentioned by {list_president}. {repeated_it_the_most} mentioned it the most, he repeated it {frequency} times."
    return message



def first_president_to_mention(cleaned_directory, chosen_word, matrix, theme_or_word=False):
    """
    Determine the first president to mention specific word(s)

    Parameters
    ----------
    cleaned_directory (str): The directory containing cleaned text files
    chosen_word (str): The word(s) to search for
    matrix (list): A matrix containing TF-IDF scores
    theme_or_word (bool): Determine if the user want to search for a specific word or a theme

    Returns
    ----------
    str: A message indicating the presidents who mentioned the word(s) first
    or
    str: A message indicating an error
    """
    message= "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
      message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    else:
      date_nominations = {
        "Nomination_Giscard dEstaing": 1974, "Nomination_Mitterrand1": 1981, "Nomination_Mitterrand2": 1988,
        "Nomination_Chirac1": 1995, "Nomination_Chirac2": 2002, "Nomination_Sarkozy": 2007,
        "Nomination_Hollande": 2012, "Nomination_Macron": 2017}

      mention_indices = []
      words=[]
      number_of_letters_removed=len(chosen_word)
      result=""
      # Convert to lowercase 
      for char in chosen_word:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + ord('a') - ord('A'))
        else:
            result += char
      chosen_word=result

      #Determine the answer depending on the user preference
      theme_or_word_answer='word'
      if theme_or_word==True:
        number_of_letters_removed=5
        theme_or_word_answer='theme'

      for row in matrix:
        # Check if the row's word is equal to the chosen word
        if chosen_word[:number_of_letters_removed] in row[0]:
            # Analyze the matrix elements, if it's not None, it appends its index to the mention_indices list
            for i in range(len(row[1])):
                # Check if the element is not None, and append its index to the mention_indices list
                if row[1][i] is not None:
                    mention_indices.append(i)
                    words.append(row[0])
      mention_indices=list(set(mention_indices))

      # Check if the word already have been 
      if mention_indices==[]:
          message= f"The {theme_or_word_answer} '{chosen_word}' hasn't been mentioned by any president available in our database ⚠ "
      else:
          filenames_who_mentioned = []
          filenames = []
          #Store the files names in file processing order
          for filename in os.listdir(cleaned_directory):
              if filename.endswith("_removed_punctuation.txt"):
                  filenames.append(filename.split('_')[0] + "_" + filename.split('_')[1])

          #Add the file names that mentionned the theme
          for index in mention_indices:
              filenames_who_mentioned.append(filenames[index])

          # Initialize the date to the smallest value of the dictionnary
          nomination_year = date_nominations[filenames_who_mentioned[0]]
          president_name = filenames_who_mentioned[0]

          # Find the earliest mention year and associated president name
          for i in range(1, len(filenames_who_mentioned)):
              # If the nomination date is smaller, it takes the president name and nomination year
              if date_nominations[filenames_who_mentioned[i]] < nomination_year:
                  nomination_year = date_nominations[filenames_who_mentioned[i]]
                  president_name = filenames_who_mentioned[i]

          tf_president=tf_score(f"{president_name}_removed_punctuation.txt", cleaned_directory)

          filtered_words = []
          for word in words:
              # Check if the word is present in 'tf_president'
              if word in tf_president:
                  # Append the word to 'filtered_words' if present in 'tf_president'
                  filtered_words.append(word)

          filtered_words=list(set(filtered_words))

          # Remove the numbers at the end of the file name
          numbers="0123456789"
          while president_name[-1] in numbers:
              president_name = president_name[:-1]

          filtered_words=", ".join(filtered_words)
          message= f"The first president to talk about the {theme_or_word_answer} '{chosen_word}' was {president_name.split('_')[1]} in {nomination_year}. He used the words: {filtered_words}"
    return message



def word_mentioned_by_all(directory, cleaned_directory, matrix):
    """
    Determine which word has been mentioned by all president among the important ones

    Parameters
    ----------
    directory (str):  The directory containing text files
    cleaned_directory (str): The directory containing cleaned text files
    matrix (list): A matrix containing TF-IDF scores

    Returns
    ----------
    str: A message indicating the words (not including least important words) mentioned by all presidents 
    or
    str: A message indicating an error
    """

    message = "Error, couldn't process ⚠ " 

    # Check if directories exist
    if not os.path.exists(cleaned_directory):
        message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    elif not os.path.exists(directory):
        message = f"You don't have any folder named '{directory}' ⚠ "
    else:

        # Get the list of filenames from the directory
        filenames = []
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                # Get the original name of the file
                original_name = filename.split("_")[0] + "_" + filename.split("_")[1] + "." + filename.split(".")[-1]
                filenames.append(extract_president_names(directory, original_name))

        # Extract the list of presidents
        presidents = sorted(list_presidents_names(directory))

        mentioned_words = []
        for row in matrix:
            files_mentioned = []
            for i in range(len(row[1])):
                if row[1][i] != None and row[0] not in least_important_words(cleaned_directory, matrix):
                    # Store the name of the presidents that mention this word
                    files_mentioned.append(filenames[i])

            files_mentioned=list(set(files_mentioned))
            # Check if the word has been mentioned by all the presidents. 
            #If a president has more than 1 text, the word has to be mentioned in only 1 of their texts
            if sorted(files_mentioned) == presidents:
                mentioned_words.append(row[0])

        mentioned_words=", ".join(mentioned_words)
        message = f"Here's the list words mentioned by all president among the so-called 'important' words : {mentioned_words}" 
    return message


def list_files(directory,extension=""):
  list_of_files=[]
  for filename in os.listdir(directory):
      if filename.endswith(extension):
          list_of_files.append(filename)
  return list_of_files



def question_tokenization(request, question_directory, question_cleaned_directory):
    """
    Clean a question asked by the user

    Parameters
    ----------
    request (str): The quetion asked by the user
    question_directory (str): The directory containing question 
    question_cleaned_directory (str): The directory containing cleaned question 

    Returns
    ----------
    str: A message indicating the status of the operation
    """
    message= "Error, couldn't process ⚠ "
    # Check if the 'question_directory' directory exists; if not, create it
    if not os.path.exists(question_directory):
        os.makedirs(question_directory)
    # Check if the 'question_cleaned_directory' directory exists; if not, create it
    if not os.path.exists(question_cleaned_directory):
        os.makedirs(question_cleaned_directory)

    # Create a new .txt file in the question folder as log
    new_filepath = os.path.join(question_directory, "log_question.txt")
    with open(new_filepath, "a", encoding="utf-8") as log_question:
      log_question.write(request+"\n")

    # Clean the request of the user
    convert_folder_cleaned(question_directory,question_cleaned_directory)
    remove_punctuation_folder(question_cleaned_directory)
    message = f" Your request has been successfully cleaned and processed to remove punctuation and saved in '{question_cleaned_directory}'"
    return message



def words_in_the_question(question_cleaned_directory , matrix):
    """
    Clean a question asked by the user

    Parameters
    ----------
    question_cleaned_directory (str): The directory containing cleaned questions
    matrix (list): A matrix containing TF-IDF scores

    Returns
    ----------
    list: A list of words in the specified line of the question
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    if not os.path.exists(question_cleaned_directory):
        message = f"You don't have any cleaned text in '{question_cleaned_directory}' ⚠ "
    else:
        for filename in os.listdir(question_cleaned_directory):
            # Check if the file is a punctuation-removed text file
            if filename.endswith("_removed_punctuation.txt"):
                filepath = os.path.join(question_cleaned_directory, filename)
                with open(filepath, 'r',encoding="utf-8") as questions:
                  words_list = questions.readline().split()
                  message = words_list
    return message


def scalar_product(matrix_A, matrix_B, file_name_A, file_name_B, directory):
    """
    Calculates the scalar product of a document and the question

    Parameters
    ----------
    matrix_A (list): A matrix A containing TF-IDF scores
    matrix_B (list): A matrix B containing TF-IDF scores
    file_name_A (str): The file name of B of the document B to analyze
    file_name_B (str): The file name of A of the document B to analyze
    directory (str): The directory containing texts

    Returns
    ----------
    int: The scalar product of the 2 vectors
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "

    # Check if the specified directory exists
    if not os.path.exists(directory):
        message = f"You don't have any folder named '{directory}' ⚠ "
    else:
        # Extract president names from the specified directory
        list_presidents = extract_president_names_folder(directory, True)

        # Find the document number for the matrix A
        document_number_A=None
        Found=True
        for i in range (len(list_presidents)):
          if (file_name_A == list_presidents[i] or file_name_A== "log_question") and Found==True:
              document_number_A=i
              Found=False

        # Find the document number for the matrix B
        Found=True
        document_number_B=None
        for i in range (len(list_presidents)):
          if (file_name_B == list_presidents[i] or file_name_B== "log_question") and Found==True:
              document_number_B=i
              Found=False

        # Check if the president name was found
        if document_number_A is None:
            message = f"The name '{file_name_A}' doesn't exist in our database ⚠ "
        if document_number_B is None:
            message = f"The name '{file_name_B}' doesn't exist in our database ⚠ "

        else:
            scalar_product = 0

            # Calculate the scalar product of a given document with the question
            if (len(matrix_A)) == (len(matrix_B)) :
                for i in range(len(matrix_A)):
                    # Check for None values in matrix_A and matrix_B
                    if matrix_B[i][1][document_number_B]== None or matrix_A[i][1][document_number_A] == None:
                        scalar_product += 0.0  # If any value is None, add 0 to the scalar product
                    else:
                        # Multiply non-None values and add to the scalar product
                        scalar_product += matrix_A[i][1][document_number_A] * matrix_B[i][1][document_number_B]
    
                message = scalar_product  

    return message



def norm_of_a_vector(matrix, file_name, directory):
  """
  Calculates the norm of a vector of a document

  Parameters
  ----------
  matrix (list): A matrix containing TF-IDF scores
  file_name (str): The name of the document to analyze
  directory (str): The directory containing texts

  Returns
  ----------
  int: The norm of the vector
  or
  str: A message indicating an error
  """
  message = "Error, couldn't process ⚠ "

  # Check if the specified directory exists
  if not os.path.exists(directory):
      message = f"You don't have any folder named '{directory}' ⚠ "
  else:
      # Extract president names from the specified directory
      list_presidents = extract_president_names_folder(directory, True)

      # Find the document number for the given president name
      Found=True
      document_number=None
      for i in range (len(list_presidents)):
        if file_name == list_presidents[i] or file_name== "log_question" and Found==True:
            document_number=i
            Found=False

      # Check if the president name was found
      if document_number is None:
          message = f"The name '{file_name}' doesn't exist in our database ⚠ "

      else:
          norm_of_a_vector = 0

          # Calculate the norm of a given document 
          for i in range(len(matrix)):
              # Check for None values in matrix
              if matrix[i][1][document_number] is None:
                  norm_of_a_vector += 0.0  # If any value is None, add 0 to the norm
              else:
                  # Multiply non-None values and square it
                  norm_of_a_vector += matrix[i][1][document_number]**2

          message = math.sqrt(norm_of_a_vector)

  return message


def similarity(matrix_A, matrix_B, file_name_A, file_name_B, directory):
  """
  Calculates the similarity of vectors of a document

  Parameters
  ----------
  matrix_A (list): A matrix A containing TF-IDF scores
  matrix_B (list): A matrix B containing TF-IDF scores
  file_name_A (str): The file name of B of the document B to analyze
  file_name_B (str): The file name of A of the document B to analyze
  directory (str): The directory containing texts

  Returns
  ----------
  int: The similarity between 2 vectors
  or
  str: A message indicating an error
  """
  message = "Error, couldn't process ⚠ "
  # Check if the specified directory exists
  if not os.path.exists(directory):
      message = f"You don't have any folder named '{directory}' ⚠ "
  else:
        
      # Calculate the scalar product of the document vectors
      scalar_product_value = scalar_product(matrix_A, matrix_B, file_name_A, file_name_B, directory)
      
      # Calculate the product of the norms of the document vectors
      norm_product = norm_of_a_vector(matrix_A, file_name_A, directory) * norm_of_a_vector(matrix_B, file_name_B, directory)
    
      # Avoid division by zero and calculate the similarity
      if norm_product != 0:
          message = scalar_product_value / norm_product
      else:
          message=0
  
  return message

def calculating_most_relevant_document(matrix_A, matrix_B, directory):
    """
    Calculates the norm of a vector of a document

    Parameters
    ----------
    matrix_A (list): A matrix A containing TF-IDF scores
    matrix_B (list): A matrix B containing TF-IDF scores
    directory (str): The directory containing texts

    Returns
    ----------
    str: The name of the most relevant document
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    # Check if the specified directory exists
    if not os.path.exists(directory):
        message = f"You don't have any folder named '{directory}' ⚠ "
    else:
        list_documents_similarity=[]
        for filename in os.listdir(directory):
            # Extract the president name from the file
            president_name=extract_president_names(directory, filename, True)
            # Calculate the similarity and appends the filename and the similarity number
            list_documents_similarity.append([filename, similarity(matrix_A, matrix_B, president_name, "log_question", directory)])
            max=list_documents_similarity[0]
    
            #Get the highest similarity number among all the documents
            for i in range (len(list_documents_similarity)):
                if max[1] < list_documents_similarity[i][1]:
                    max=list_documents_similarity[i]
    
            message = max[0]
    return message


def generate_an_answer(matrix_A, matrix_B, directory, cleaned_question_directory):
    """
    Generates an answer based on TF-IDF similarity between the question and documents.
  
    Parameters
    ----------
    matrix_A (list): TF-IDF matrix of documents.
    matrix_B (list): TF-IDF matrix of the question.
    directory (str): Directory containing text documents.
    cleaned_question_directory (str): Directory containing cleaned questions.
  
    Returns
    ----------
    str: The generated answer or an error message.
    """
    message = "Error, couldn't process ⚠ "
    # Calculate the highest TF-IDF score and associated word in the question
    highest_tf_idf_question_word = highest_tf_idf_score(cleaned_question_directory, matrix_B)
  
    # Find the most relevant document based on matrices A and B
    most_relevant_document = calculating_most_relevant_document(matrix_A, matrix_B, directory)
  
    filepath = os.path.join(directory, most_relevant_document)
    # Check if the TF-IDF score is 0, indicating an error in processing the question
    if highest_tf_idf_question_word[1] == 0:
        message = "An error appeared while processing the question, we weren't able to generate a logical answer, the subject of your question is too general, please ask another question ⚠ "
    else:
        # Try to open the most relevant document and read its content
        with open(filepath, "r", encoding="utf-8") as opened_most_relevant_document:
            text = opened_most_relevant_document.read()
            sentences = text.split(".")
  
            # Initialize a default message for TF-IDF inaccuracy
            message = "An error appeared while processing the question, the degree of similarity couldn't be calculated because of the TF-IDF inaccuracy, please ask another question ⚠ "
  
            # Check if the highest TF-IDF word is present in the sentence
            word_found=False
            for sentence in sentences:
                # Lower the sentence without using .lower()
                answer=""
                for word in sentence.split(" "):
                  answer += word.lower()+" "

                # Refine the answer
                if highest_tf_idf_question_word[0] in answer and not word_found:
                    word_found = True
                    message = (sentence)+"."
    return message


def refine_an_answer(cleaned_question_directory, answer):
  """
  Refines the answer generated by adding context-based responses.

  Parameters
  ----------
  cleaned_question_directory (str): Directory containing cleaned questions.
  answer (str): The original answer.

  Returns
  ----------
  str: The refined answer with added context or an error message.
  """
  # Check if the cleaned_question_directory folder exists
  if not os.path.exists(cleaned_question_directory):
      message = f"You don't have any folder named '{cleaned_question_directory}' ⚠ "
  else:
      # Check if there's an error message in the answer
      if "An error appeared while processing the question" not in answer:
          # Define mappings between question starters and responses
          question_starters = {
              "comment": "Après analyse, ",
              "pourquoi": "Car, ",
              "peux tu": "Oui, bien sûr ! ",
              "quand": "À ce moment-là, ",
              "quel": "Le choix dépend mais en général, ",
              "qui": "Souvent, ",
              "est ce que": "Effectivement, ",
              "quoi": "Cela peut être déterminé par beaucoup de facteurs. ",
              "peut on": "Dans certaines circonstances, ",
          }

          # Define the filepath for the log_question_removed_punctuation.txt file
          filepath = os.path.join(cleaned_question_directory, "log_question_removed_punctuation.txt")

          # Read the content of the log_question_removed_punctuation.txt file
          with open(filepath, 'r', encoding='utf-8') as file:
              request = file.read()

          message = "Your request isn't considered a question, please ask a question ⚠"

          # Iterate through question starters and check if any is present in the request
          for starter, response in question_starters.items():
              if starter in request:
                  # Handle the case where the response should start with a lowercase letter
                  if response[-2] not in ".!" and not ord('A') <= ord(response[1]) <= ord('Z'):
                      answer_list = list(answer.lstrip('\n'))
                      # Remove a capital if the reponse ends with a . or a !
                      if ord('A') <= ord(answer_list[0]) <= ord('Z'):
                          answer_list[0] = chr(ord(answer_list[0]) + 32)
                      else:
                          answer_list[0]
                      # Refine the answer
                      refined_answer = response + ''.join(answer_list)
                  else:
                      refined_answer = response + answer.lstrip('\n')
                  message = refined_answer

      else:
          message = answer

  return message


def change_directories():
  """
  Asks the user for directory information and stores it in a file.

  Returns
  ----------
  list: A list containing directory information.
  """
  # Prompt the user to enter the folder where the texts are located
  directory = str(input(f"\033[91mBefore you begin, please enter the name of the folder where your texts are located : \033[0m"))

  # Validate that the entered directory exists
  while not os.path.exists(directory):
      print(f"\033[91mYou don't have any folder named '{directory}' ⚠ \033[0m")
      directory = str(input(f"\033[91mEnter the name of the file where your texts are located : \033[0m"))

  # Prompt the user to enter names for various folders
  cleaned_directory = str(input(f"\033[91mEnter a name for the folder where the files will be treated : \033[0m"))
  question_directory = str(input(f"\033[91mEnter a name for the folder where the questions will be stored : \033[0m"))
  cleaned_question_directory = str(input(f"\033[91mEnter a name for the folder where the questions will be treated  : \033[0m"))

  # Write the entered directories to a file named "directories.txt"
  with open("directories.txt", "w", encoding="utf-8") as file:
      directories_list = [directory, cleaned_directory, question_directory, cleaned_question_directory]
      directories_text = "\n".join(directories_list)
      file.write(directories_text)

  return [directory, cleaned_directory, question_directory, cleaned_question_directory]



def check_for_directories():
  """
  Checks if directories are already set, returns stored directories or asks the user for new ones.

  Returns
  ----------
  list: A list containing directory information.
  or
  bool: False if directories are not set.
  """
  # Check if the "directories.txt" file exists
  if os.path.exists("directories.txt"):
      # Read the content of the file and split it into lines
      with open("directories.txt", "r") as file:
          directories = file.read().splitlines()

          # Check if the number of lines is not equal to 4 (expected number of directories)
          if len(directories) != 4:
              return False
      return directories
  else:
      # If the file doesn't exist, call the change_directories function to set up directories
      return change_directories()