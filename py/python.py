
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'

a="python"
b= "is"
c="a"
d="powerful"
f="language"
space=""
print(a+space+b + space+c+space+d+space+ f)



# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."

topic="strings in Python."
print(topic)



# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."

sent= "Learning about \":Python\" strings is fun."
print(sent)


# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.

sent="Also, count and print how many times the letter 's' appears in the string."
print(sent.count('s'))


# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.

sen="uppercase and lowercase conversion"
print(sen.isupper())

sent="UPPERCASE AND LOWERCASE CONVERSION"
print(sen.islower())

# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."

name="Let's learn about topic."


# Substring Extraction:
# Extract and print the word 'Python' from the topic string.

sent=" Extract and print the word Python from the topic string."
topic=sent[22:29]
print(sent)


# Create a list called programming_languages with the elements ['Python', 'Java']. Use the append() method to add 'C++' to the list. Then, use the extend() method to add ['JavaScript', 'Ruby'] to the list. Print the updated list.

programming_languages=['Python', 'Java']
programming_languages.append("C++")
programming_languages.extend ['JavaScript', 'Ruby']
print(programming_languages)


# List Insertion:
# Insert the string 'C#' at the third position in the programming_languages list and print the modified list.

programming_languages=['Python', 'Java']
programming_languages.append("C++")
programming_languages.insert(2)
print(programming_languages)




# List Removal:
# Remove the second element from the programming_languages list and print the updated list.



# List Clearing:
# Use a method to clear all elements from the programming_languages list and print the empty list.

programming_languages=['Python', 'Java','JavaScript', 'Ruby']
programming_languages.clear
print(programming_languages)




