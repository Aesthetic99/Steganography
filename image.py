from stegano import lsb

def space():
    print("\n\n")

def menu():
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice



def encode():
    #take input from user
    image = input("Enter image name(with extension): ")
    data = input("Enter data to be encoded : ")

    #hide message in image
    lsb.hide(image, data).save("new.png")

def decode():
    #take input from user
    image = input("Enter image name(with extension) :")

    print ()
    #show message from image
    print(lsb.reveal(image))

def error():
    print("Invalid input")

def main():
    while True:
        choice = menu()
        if choice == 1:
            encode()
            space()
        elif choice == 2:
            decode()
            space()
        elif choice == 3:
            break
        else:
            error()
            space()
            main()

if __name__ == '__main__':
    main()


