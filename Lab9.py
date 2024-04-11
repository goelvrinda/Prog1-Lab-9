def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def encode():
    pass

def decode(password):
    decoded_pass = ''
    for i in password:
        decoded_num = str(int(i) - 3)
        decoded_pass += decoded_num
    return decoded_pass



def main():
    while True:
        menu()
        selection = int(input("Please enter an option: "))

        if selection == 1:
            pass
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        else:
            print("Invalid input!")
