from datetime import datetime


def printHello():
    print("Hello Github")
    print(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


def main():
    printHello()


if __name__ == "__main__":
    main()
