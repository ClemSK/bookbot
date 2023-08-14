# Open and read the contents of "frankenstein.txt"
with open("books/frankenstein.txt", "r") as file:
    contents = file.read()

# Print the contents to the console
# print(contents)

list_of_words = contents.split()
# print(list_of_words)

# count words
def count_words():
   num_of_words = len(list_of_words)
  #  print(num_of_words)
   return num_of_words

count_words()

alphabet_dict = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

def count_letters():
    # define dictionary

    for word in list_of_words: # loop through words
        
        for letter in word:
            if letter.isalpha(): # check if a letter
                lowercase_letter = letter.lower()

                if lowercase_letter in alphabet_dict:
                    alphabet_dict[lowercase_letter] += 1

    # print(alphabet_dict)

count_letters()

def report():
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{len(list_of_words)} words found in the document")
    sorted_alphabet_dict = dict(sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True))
    for letter in sorted_alphabet_dict:
      # sort letters in descending order
      if letter.isalpha():
       print(f"The {letter} character was found {sorted_alphabet_dict[letter]} times")
    print('--- End report ---')

report()
    


