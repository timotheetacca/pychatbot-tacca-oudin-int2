# pychatbot-tacca-oudin-int2 
> ###### 2023-L1 EFREI Tacca Timothée, Oudin Julien

[> Link to Github](https://github.com/timotheetacca/pychatbot-tacca-oudin-int2/)
<br />
<br />


This tool allows users to analyze speeches of different presidents.

This chat-bot gives you the ability to extract presidential names, associate names with first names, list available presidential names, clean text files, remove punctuation and accents, calculate TF-IDF scores, and perform various analyzes of speeches.

Be sure to have a folder with .txt files to treat, we recommand the name 'speeches' but you can use any other name !
We recommand you to use the name 'cleaned' for the name of the folder where the files will be treated, but you can use any other name !

## Functions

`extract_president_names(directory)` : Extracts president names from text files
 
`extract_president_names_folder(directory)` : Extracts president names from text files in a directory

`associate_name(name)` : Associates a president's last name with their first name

`list_presidents_names(directory)` : Lists unique president names extracted from text files in a directory

Those following functions do not containt any built-in function such as : .isdigit() or .lower(), we made them ourselves :
>>
`convert_text_cleaned(filename, cleaned_directory)` : Converts a text file to lowercase and saves it in a cleaned directory 

>>
`convert_folder_cleaned(directory, cleaned_directory)` : Converts text files to lowercase in a folder and saves them in a cleaned directory

>>
`remove_punctuation_text(filename, cleaned_directory)` : Remove punctuation and accents from a text and saves it in a cleaned directory.

>>
`remove_punctuation_folder(cleaned_directory)` : Removes punctuation and accents in a directory and saves them in a cleaned directory

## TF-IDF Analysis Functions

The following functions are related to TF-IDF (Term Frequency-Inverse Document Frequency) analysis:

`tf_score(filename, cleaned_directory)` : Calculate the TF score for each word 

`idf_score(cleaned_directory)` : Calculate the IDF score for each word

`tf_idf_matrix(cleaned_directory)` : Calculate the TF-IDF matrix
 
`print_tf_idf_matrix(cleaned_directory, matrix=None)` : Prints the TF-IDF matrix for the documents in a directory

`least_important_words(cleaned_directory, matrix=None)` : Generates a list of words with the least importance, where their TF-IDF = 0 in all files

`highest_tf_idf_score(cleaned_directory, matrix=None)` : Determine the word with the highest TF-IDF score

`most_repeated_word_by_president(directory, president_name, cleaned_directory, least_important_included=False, matrix=None)` : Determine what's the most repeated word among the important ones or among all words depending on the value choosen for *least_important_included*

`presidents_who_mentioned(directory, cleaned_directory, chosen_word)` : Determine which presidents mentioned a specific word, and who mentioned it the most

`first_president_to_mention(cleaned_directory, chosen_word, matrix=None)` : Determine the first president to mention specific word(s)

`word_mentioned_by_all(directory, cleaned_directory, matrix=None)` : Determine which word has been mentioned by all president among the important ones



These functions enable users to analyze the TF-IDF scores of words used in speeches, identify least important words, find the word with the highest TF-IDF score, determine the most repeated word by a president, find presidents who mentioned specific words, and identify the first president to mention specific words.

## Usage

To use these functions, ensure you have text files in a directory. Adjust the directory paths in function calls accordingly for your specific setup.

For example:

```python
# Extract president names
print(extract_president_names("speeches"))

# Convert text files to lowercase in a cleaned directory
print(convert_folder_cleaned("speeches", "cleaned"))

# Remove punctuation from text files in the cleaned directory
print(remove_punctuation_folder("cleaned"))

# Perform TF-IDF analysis
matrix = tf_idf_matrix("cleaned")
print(print_tf_idf_matrix("cleaned", matrix))

# Analyze specific word mentions by presidents
print(most_repeated_word_by_president("speeches", "Chirac", "cleaned", least_important_included=False, matrix=matrix))

# Identify the first president who mentioned a specific word and the other one that also mentionned it
print(presidents_who_mentioned("speeches", "cleaned", "nation"))

# Find the first president to mention a theme
print(first_president_to_mention("cleaned", "climat", matrix))

# Determine the word mentionned by all the presidents
print(word_mentioned_by_all("speeches","cleaned",matrix))
