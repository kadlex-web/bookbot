def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split_file = file_contents.split(" ")
        print(len(split_file))
main()