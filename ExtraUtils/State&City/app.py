import csv

def read(f):
    with open(file=f, mode="r", encoding="UTF-8") as fp:
        reader = csv.DictReader(fp)
        for each in reader:
            print(each)


def main():
    f = read("ostan.csv")




if __name__ == "__main__":
    main()