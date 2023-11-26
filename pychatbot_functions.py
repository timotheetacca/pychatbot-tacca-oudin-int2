import os, math

def extract_president_names(directory, filename):
  """
  Extracts president names from text files in a directory

  Parameters
  ----------
  directory (str): The directory containing text files
  filename (str): The specific filename to search for in the directory

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
          numbers = "0123456789"
          while president_name[-1] in numbers:
              president_name = president_name[:-1]

          message = president_name
      else:
          message = f"No file with the name '{filename}' found in the directory ⚠"
  return message


def extract_president_names_folder(directory):
    """
    Extracts president names from text files in a directory

    Parameters
    ----------
    directory (str): The directory containing text files

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
                files_presidents.append(extract_president_names(directory, filename))

        if files_presidents!=[]:
            files_presidents = ", ".join(files_presidents)
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
      #Make a set of the extract_president_names() to avoid duplicates and then print a list of name separeted by comas
      president_names = ", ".join(set((extract_president_names_folder(directory).split(", "))))
      message= f"Here's the list of president (without duplicates) available in our data base : {president_names}"
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
        name_parts = filename.split("_")
        new_filename = f"{name_parts[0]}_{name_parts[1].split('.')[0]}_cleaned.txt"
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






#TF-IDF PART






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
        file_count = 0
        for filename in os.listdir(cleaned_directory):
            # Check if the file is a punctuation-removed text file
            if filename.endswith("_removed_punctuation.txt"):
                file_count += 1
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
            word_idf[word] = math.log(file_count / value)
        message= word_idf
    return message



def tf_idf_matrix(cleaned_directory):
    """
    Calculate the TF-IDF matrix

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files

    Returns
    ----------
    list: TF-IDF matrix represented as a list of lists.
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    if not os.path.exists(cleaned_directory):
        message = f"You don't have any folder named '{cleaned_directory}' ⚠ "
    else:
        # Get IDF score
        idf_scores = idf_score(cleaned_directory)

        # Initialize an empty TF-IDF matrix
        tf_idf_matrix = []
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                # Get the TF scores for the document
                tf_scores = tf_score(filename, cleaned_directory)

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


def print_tf_idf_matrix(cleaned_directory, matrix=None):
    """
    Prints the TF-IDF matrix for the documents in a directory

    Parameters
    ----------
    clean_directory (str): The directory containing cleaned text files
    matrix (list): The TF-IDF matrix. If not provided, the function will generate it.

    Returns
    ----------
    print row by row the matrix
    or
    str: A message indicating an error
    """
    message = "Error, couldn't process ⚠ "
    # Check if the 'cleaned' directory exists
    if not os.path.exists(cleaned_directory):
        message = f"You don't have any folder named '{cleaned_directory}' ⚠ "

    else:
        # Create and store the matrix if the user didn't provide one
        if matrix is None:
            matrix = tf_idf_matrix(cleaned_directory)

        # Get the list of filenames from the directory
        filenames = []
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                filenames.append(filename.split('_')[1].split('.')[0])

        # Calculate the maximum length of word for clean alignment
        max_word_length = max(len(row[0]) for row in matrix)

        # Generate the header 
        header = [f"| {' ':<{max_word_length}}"]
        for filename in filenames:
            header.append(f"{filename:^{max_word_length}}")  # Center each filename in a cell of width max_word_length
        print(" | ".join(header) + " |")

        # Print the matrix rows
        for row in matrix[:30]:
            word = row[0]
            values = row[1]
            word_padding = ' ' * (max_word_length - len(word))  # Calculate padding for the word
            word_output = f"| {word}{word_padding} |"

            formatted_values = []
            for value in values:
                if value is not None:
                    if value <= 10:
                        formatted_values.append(f"{value:.4f}")
                    else:
                        formatted_values.append(f"{value:.3f}")
                else:
                    formatted_values.append(" ")

            values_output = ' | '.join(f"{val:<{max_word_length}}" for val in formatted_values)
            row_output = f"{word_output} {values_output} |"
            print(row_output)
            message = ""

    return message



def least_important_words(cleaned_directory, matrix=None):
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
        # Create and store the matrix if the user didn't create one
        if matrix==None:
            matrix = tf_idf_matrix(cleaned_directory)
            print("New matrix created")

        # Count the number of files
        file_count = 0
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                  file_count += 1

        least_important_words = []
        for row in matrix:
            # Stores the word if its TF-IDF = 0 in all files
            if row[1] == [0.0] * file_count: 
                least_important_words.append(row[0])

        least_important_words = ", ".join(least_important_words)
        message= f"Here's the list of least important words: {least_important_words}"
    return message




def highest_tf_idf_score(cleaned_directory, matrix=None):
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
            matrix = tf_idf_matrix(cleaned_directory)
            print("New matrix created")

        # Count the number of files
        file_count = 0
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                  file_count += 1

        max_score = 0.0
        max_word = ""
        for row in matrix:
            for i in range(file_count): 
                # Check if the value is not None and greater than the current max
                if row[1][i] is not None and row[1][i] > max_score:
                    max_score = row[1][i]
                    max_word = row[0]

        message= f"The word with the highest TF-IDF score is '{max_word}' with a score of: {max_score:.4f}"
    return message




def most_repeated_word_by_president(directory, president_name, cleaned_directory ,least_important_included="False", matrix=None):
    """
    Determine what's the most repeated word among the important ones

    Parameters
    ----------
    directory (str):  The directory containing text files
    president_name (str): The name of the president to analyze
    cleaned_directory (str): The directory containing cleaned text files
    least_important_included (str): Display a word that doesn't appear in the least_important_word()
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
      if matrix==None:
          matrix = tf_idf_matrix(cleaned_directory)
          print("New matrix created")

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
          if least_important_included=="True":
              while most_repeated_word in least_important_words(cleaned_directory, matrix):
                  # Remove the most repeated word from the total_tf_score dictionary
                  del total_tf_score[most_repeated_word]
                  # Check if there are still words left in the dictionary and find the new most repeated word
                  most_repeated_word = max(total_tf_score, key=total_tf_score.get)


          frequency = total_tf_score[most_repeated_word]
          message= f"The most repeated word by {president_name} is '{most_repeated_word}', he repeated it {frequency} times."
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



def first_president_to_mention(cleaned_directory, chosen_word, matrix=None):
    """
    Determine the first president to mention specific word(s)

    Parameters
    ----------
    cleaned_directory (str): The directory containing cleaned text files
    chosen_word (str): The word(s) to search for
    matrix (list): A matrix containing TF-IDF scores

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
      number_of_letters_removed=0
      while (len(chosen_word))- number_of_letters_removed > 5:
          number_of_letters_removed+=1

      for row in matrix:
        # Check if the row's word is equal to the chosen word
        if chosen_word[:-number_of_letters_removed] in row[0]:
            # Analyze the matrix elements, if it's not None, it appends its index to the mention_indices list
            for i in range(len(row[1])):
                # Check if the element is not None, and append its index to the mention_indices list
                if row[1][i] is not None:
                    mention_indices.append(i)
                    words.append(row[0])
      mention_indices=list(set(mention_indices))

      # Check if the word already have been 
      if mention_indices==[]:
          message= f"'{chosen_word}' hasn't been mentioned by any president available in our database ⚠ "
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
          message= f"The first president to talk about '{chosen_word}' was {president_name.split('_')[1]} in {nomination_year}. He used the words: {filtered_words}"
    return message


def word_mentioned_by_all(directory, cleaned_directory, matrix=None):
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
        # If the matrix is not provided, create a new one
        if matrix is None:
            matrix = tf_idf_matrix(cleaned_directory)
            print("New matrix created")

        # Get the list of filenames from the directory
        filenames = []
        for filename in os.listdir(cleaned_directory):
            if filename.endswith("_removed_punctuation.txt"):
                # Get the original name of the file
                original_name = filename.split("_")[0] + "_" + filename.split("_")[1] + "." + filename.split(".")[-1]
                filenames.append(extract_president_names(directory, original_name))

        # Extract the list of presidents
        presidents = sorted(list_presidents_names(directory).split(": ")[1].split(", "))

        mentioned_words = []
        for row in matrix:
            files_mentioned = []
            for i in range(len(row[1])):
                if row[1][i] != None and row[0] not in least_important_words(cleaned_directory, matrix).split(": ")[1].split(", "):
                    # Store the name of the presidents that mention this word
                    files_mentioned.append(filenames[i])

            files_mentioned=list(set(files_mentioned))
            # Check if the word has been mentioned by all the presidents. 
            #If a president has more than 1 text, the word has to be mentioned in only 1 of their texts
            if sorted(files_mentioned) == presidents:
                mentioned_words.append(row[0])

        mentioned_words=", ".join(mentioned_words)
        message = f" Here's the list words mentioned by all president among the so-called 'important' words : {mentioned_words}" 
    return message
