def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_word_count(file_contents)
        x = get_char_count(file_contents)
        print(x)
        print(f"The book contains {num_words} words")

def get_word_count(file):
    split_file = file.split()
    return len(split_file)

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

main()