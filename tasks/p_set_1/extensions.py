

def main():
    mappings = [{"extension": "gif", "mapping": "image/gif"},
                {"extension": "jpg", "mapping": "image/jpg"},
                {"extension": "jpeg", "mapping": "image/jpeg"},
                {"extension": "png", "mapping": "image/png"},
                {"extension": "pdf", "mapping": "application/pdf"},
                {"extension": "txt", "mapping": "text/txt"},
                {"extension": "zip", "mapping": "application/zip"}]

    file_name = input("File name:")
    name, extension = file_name.strip().rsplit(".", maxsplit=1)

    for i in mappings:
        if extension.lower() == i["extension"]:
            print(name + "/" + i["mapping"])

            break


if __name__ == "__main__":
    main()

