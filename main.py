def main():
    path = "books/frankenstein.txt" #Input the location of the file you want to analyze
    file = get_file_contents(path)
    num_words = get_word_count(file)
    char_count = get_char_count(file)
    m = sorted(char_count.items(), key= lambda item:item[1], reverse=True)
    new_dict = {}
    for key, value in m:
        new_dict[key] = value
    get_status_report(path, num_words, new_dict)

#Takes a get_word_count function and get_char_count function and generates a clean report of all the data
def get_status_report(file, word_count, char_count):
    print("Welcome to your status report!\n")
    print(f"You requested a report on {file}\n")
    print(f"We found that the file contained {word_count} words.\n")
    for value in char_count:
        print(f"The character {value} was found {char_count[value]} times.")
    print("\n---End of Report---")

# Takes the given file and splits it. Then finds the length of the list and returns it
def get_word_count(file):
    split_file = file.split()
    return len(split_file)

"""Takes the given files, splits it, and changes all the characters to lowercase. Then loops through each word.
    If a character is already in the dictionary, it increments the value associated with the key. If not, it creates the key
    and assigns a value of 1."""
def get_char_count(file):
    char_dict = {}
    split_file = file.lower().split()

    for word in split_file:
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def get_file_contents(path):
    with open(path) as f:
        return f.read()
    
main()