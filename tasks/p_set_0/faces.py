

def convert(words, conv_dict):
    result = words
    for k, v in conv_dict.items():
        result = result.replace(k, v)
    return result


def main():
    replace_faces = input("Type words with faces \n")
    conv_dict = {":)": "🙂",
                 ":(": "🙁"}
    print(convert(replace_faces, conv_dict))


if __name__ == "__main__":
    main()