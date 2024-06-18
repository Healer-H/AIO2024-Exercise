def word_count(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()

    dictionary = {}
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return {key : dictionary[key] for key in sorted(dictionary)}

if __name__ == "__main__":
    file_path = "P1_data.txt"
    print(word_count(file_path=file_path))