from collections import Counter

def count_chars(string):
    dictionary = {}
    for char in string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    return dictionary

if __name__ == "__main__":
    string = "Happiness"
    print(count_chars(string))
    
    string = "smiles"
    print(count_chars(string))