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


# Call of the function extract_name()
presidents = extract_president_names("speeches", "txt")
for president in presidents:
    print(president)
print("")
