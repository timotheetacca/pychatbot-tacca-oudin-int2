import os, math
def extract_president_names(directory, extension):
    files_presidents = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):

            # Every file is named : "Nomination_{name}" so we split the file name using _ as space
            name_parts = filename.split("_") 
            president_name = (name_parts[1])[:-4] 

            # Remove the numbers at the end of the file name
            numbers="0123456789"
            while president_name[-1] in numbers:
                president_name = president_name[:-1]
            files_presidents.append(president_name)
    return files_presidents



def associate_name(name):
    first_names = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if name in first_names:
        # If the name exists in the dictionary, return the first name and a message
        return first_names[name]+" "+name+"'s first name is : "+first_names[name]
    else:
        # If the name doesn't exist in the dictionary, return an error message
        return f"The name {name} doesn't exist in our data base ⚠ "




def list_presidents_names(directory, extension):
    #Make a set of the extract_president_names() to avoid duplicates
    president_names = set(extract_president_names(directory, extension))
    return president_names

  

def convert_text_cleaned(filename):
    """
    Convert a text file to lowercase
    
    Parameters
    ----------
    filename (str): The name of the text 
    
    Returns
    ----------
    str: A message indicating the status of the operation
    """
    
    # Check if the 'cleaned' directory exists; if not, create it
    if not os.path.exists("cleaned"):
        os.makedirs("cleaned")
    
    # Check if the input file exists
    if not os.path.exists(os.path.join("speeches", filename)):
        return f"There is no file named '{filename}' in speeches ⚠ "
    
    # Open the input file in read mode
    input_filepath = os.path.join("speeches", filename)
    with open(input_filepath, "r") as not_cleaned_file:
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
    new_filepath = os.path.join("cleaned", new_filename)
    
    # Write the cleaned text to the output file
    with open(new_filepath, "w") as cleaned_file:
        cleaned_file.write(cleaned_text)
    
    return f"File '{filename}' has been successfully converted to lowercase and saved in 'cleaned'."

      

def convert_folder_cleaned(directory):
    # Check if their is documents in the 'speeches' directory
    if not os.path.exists(directory):
        return "You don't have any speeches ⚠ "
      
    # Read files from the 'speeches' folder
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        convert_text_cleaned(filename)
    return "'Speeches' as been successfully cleaned"


def convert_text_cleaned(filename):
    """
    Convert a text file to lowercase
    
    Parameters
    ----------
    filename (str): The name of the text 
    
    Returns
    ----------
    str: A message indicating the status of the operation
    """
    
    # Check if the 'cleaned' directory exists; if not, create it
    if not os.path.exists("cleaned"):
        os.makedirs("cleaned")
    
    # Check if the input file exists
    if not os.path.exists(os.path.join("speeches", filename)):
        return f"There is no file named '{filename}' in speeches ⚠ "
    
    # Open the input file in read mode
    input_filepath = os.path.join("speeches", filename)
    with open(input_filepath, "r") as not_cleaned_file:
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
    new_filepath = os.path.join("cleaned", new_filename)
    
    # Write the cleaned text to the output file
    with open(new_filepath, "w") as cleaned_file:
        cleaned_file.write(cleaned_text)
    
    return f"File '{filename}' has been successfully converted to lowercase and saved in 'cleaned'."

      

def convert_folder_cleaned(directory):
    # Check if their is documents in the 'speeches' directory
    if not os.path.exists(directory):
        return "You don't have any speeches ⚠ "
      
    # Read files from the 'speeches' folder
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        convert_text_cleaned(filename)
    return "'Speeches' as been successfully cleaned"

def remove_punctuation_text(filename):
    """
    Remove punctuation and accents from a text 
  
    Parameters
    ----------
    filename (str): The name of the text 
  
    Returns
    ----------
    str: A message indicating the status of the operation
    """
    # Check if the 'cleaned' directory exists
    if not os.path.exists("cleaned"):
        return "You don't have any cleaned text ⚠ "
  
    # Check if the input file exists
    if not os.path.exists(os.path.join("cleaned", filename)):
        return f"There is no file named '{filename}' in cleaned ⚠ "
  
    with open(os.path.join("cleaned", filename), "r", encoding="utf8") as not_removed_punctuation:
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
        new_filename = filename.split("_")[0] + "_" + filename.split("_")[1] + "_removed_punctuation.txt"
        new_filepath = os.path.join("cleaned", new_filename)
  
        # Write the cleaned text to a new file
        with open(new_filepath, "w") as cleaned_file:
            cleaned_file.write(cleaned_text)
          
    return f"File '{filename}' has been successfully processed to remove punctuation and saved in 'cleaned'"


          
def remove_punctuation_folder(directory):
  # Check if the 'cleaned' directory exists
  if not os.path.exists(directory):
      return "You don't have any cleaned text ⚠ "
    
  # Read files from the 'cleaned' folder
  for filename in os.listdir(directory):
      filepath = os.path.join(directory, filename)
      remove_punctuation_text(filename)
  return "'Cleaned' files no longer have accents"


# Call of the function extract_name()
presidents = extract_president_names("speeches", "txt")
for president in presidents:
    print(president)
print("")

# Call of the function associate_name()
print(associate_name("Chirac"))
print(associate_name("Julien"))
print("")

# Call of the function list_presidents_names()
for name in (list_presidents_names("speeches", "txt")):
    print(name)
print("")

# Call of the function convert_text_cleaned()
print(convert_text_cleaned("Nomination_Julien.txt"))
print(convert_folder_cleaned("cleaned"))
print("")

# Call of the function remove_punctuation()
print(remove_punctuation_text("Nomination_Timothée.txt"))
print(remove_punctuation_folder("cleaned"))
print("")
