import sys
from stats import get_word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit
    path = sys.argv[1]
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
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {file}n")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for value in char_count:
        if value.isalpha():
            print(f"{value}: {char_count[value]}")
    print("\n---End of Report---")

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