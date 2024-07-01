import streamlit as st


def load_word(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    words = set([line.strip().lower() for line in lines])
    return words


def levenshtein_distance(token1, token2):
    len1 = len(token1)
    len2 = len(token2)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if (token1[i - 1] == token2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1]
                               [j], dp[i - 1][j - 1]) + 1

    return dp[len1][len2]


file_path = "./source/source/data/vocab.txt"


def main():
    st.title("Word correction using Levenshtein Distance")
    vocabs = load_word(file_path=file_path)
    word = st.text_input("Input your word")

    leven_distance = dict()
    if st.button("Compute"):
        for vocab in vocabs:
            distance = levenshtein_distance(vocab, word)
            leven_distance[vocab] = distance
        sorted_distances = dict(
            sorted(leven_distance.items(), key=lambda x: x[1]))

        correct_word = list(sorted_distances.keys())[0]
        st.write(f"Correct word: {correct_word}")

        col1, col2 = st.columns(2)
        col1.write("Vocabulary")
        col1.write(vocabs)

        col2.write("Distance")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
