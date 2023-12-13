import sys


def main():
    names = []
    adieu = 'Adieu, adieu, to '
    while True:
        try:
            name = input('Name: ')
            names.append(name)

        except EOFError:
            if len(names) == 1:
                out = adieu + names[0]
            # elif len(names) == 2:
            #     out = adieu + "".join([i + ", " for i in names])
            else:
                out = adieu + names[0] + "".join([", " + i for i in names[1:-1]]) + ' and ' + names[-1]
            print(out)
            sys.exit()

if __name__ == '__main__':
    main()
