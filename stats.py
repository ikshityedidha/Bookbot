def number_of_words(book_text):
    return len(book_text.split())

def character_count(book_text):
    dictionary = {}
    required_book = book_text.lower()
    for character in required_book:
         if character not in dictionary:
            dictionary[character] = 1
         elif character in dictionary:
            dictionary[character]+=1

    return dictionary

def sort_on(dict):
    return dict["num"]

def sorted_dictionary(dictionary):
    required_list = []
    for key,value in dictionary.items():
        if key.isalpha():
            mini = {"char" : key,"num" : value }
            required_list.append(mini)
    required_list.sort(reverse = True,key = sort_on)
    return required_list
    

