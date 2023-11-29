def shorten(sentence):
    new_sentence = ""
    for i in sentence:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            continue
        new_sentence += i
    return new_sentence


def main():
    long = input("Input: ")
    short = shorten(long)
    print("Output:", short)


if __name__ == "__main__":
    main()