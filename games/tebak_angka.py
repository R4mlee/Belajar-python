import random

print("")
mysterious_number = random.randint(1, 200)

answer = int(input("Coba tebak angka misterinya: "))

max_try = 2
try_value = 0

while try_value != max_try:
    chance = max_try - try_value
    
    if answer == mysterious_number:
        print("Hebat!! Kamu berhasil menebak angkanya\n")
        break
    elif answer < mysterious_number:
        print("Tebakanmu masih terlalu kecil")
        print(f"Sisa kesempatan mu: {chance}\n")
    elif answer > mysterious_number:
        print("Angkanya terlalu besarrr")
        print(f"Sisa kesempatan mu: {chance}\n")

    answer = int(input("Tebak lagi angkanya: "))
    try_value += 1
    
else:
    print("Kesempatanmu sudah habis")