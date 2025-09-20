import random
from libs import welcome_message, exit_program

welcome_message()

def menu():
    print("Program tersedia saat ini: \n1.Game Tebak Angka \n2.Keluar Program \n\n")
    chose = int(input("Pilih program yang akan kamu jalankan: "))

    if chose == 1:
        pass
    else:
        exit_program()
        
def main():
    welcome_message()
    menu()
    
if __name__ == "__main__":
    main()