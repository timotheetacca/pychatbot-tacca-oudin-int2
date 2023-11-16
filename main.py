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