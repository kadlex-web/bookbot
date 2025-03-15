# Takes the given file and splits it. Then finds the length of the list and returns it
def get_word_count(file):
    split_file = file.split()
    return len(split_file)