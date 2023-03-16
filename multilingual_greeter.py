
# Add a function called language_input that gives the user an option to choose 1 of at least 3 languages.
# Ask the user for his name in the chosen language.
# Greet the user in the chosen language.

def language_input():
    
    choosen_lang = input("Choose one language 1. English 2. Spanish 3. Hindi: ")
    if choosen_lang == "English":
     name = input("Enter name in English : ")
     print("Hello "+ name)
    elif choosen_lang == "Spanish":
       name = input("Enter name in Spanish: ")
       print("Hello " + name)
    elif choosen_lang == "Hindi":
        name = input("Enter name in Hindi: ")
        print("Hello " + name)
    
language_input()
                         