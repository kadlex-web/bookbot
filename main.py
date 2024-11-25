def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_word_count(file_contents)
        print(num_words)
        
def get_word_count(file):
    split_file = file.split()
    return len(split_file)


main()