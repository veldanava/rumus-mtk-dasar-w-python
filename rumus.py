print('RUMUS MATEMATIKA DASAR by ZNAINDEV')
print("https://github.com/veldanava" "\n")

#dibuat oleh znaindev

#rumus kecepatan.
def rumus_kecepatan():
    print('hitung kecepatan')
    jarak = int(input('masukan jarak:'))
    waktu = int(input('masukan waktu:'))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan, "\n")

#rumus segitiga
def luas_segitiga():
    print('hitung luas segitiga')
    alas = int(input('masukan alas:'))
    tinggi = int(input('masukan tinggi:'))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga: ", luas, "\n")

#rumus balok
def luas_balok():
    print('hitung luas balok')
    panjang = int(input('masukan panjang balok:'))
    lebar = int(input('masukan lebar balok:'))
    tinggi = int(input('masukan tinggi balok:'))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok: ", luas, "\n")

#rumus bola
def luas_bola():
    print('hitung luas bola')
    r = int(input('masukan jari-jari:'))
    luas = 4 * 3.14 * (r**2)
    print("luas bola: ", luas, "\n")

#function
while True:
    userInput = int(input(
        "pilih rumus yg ingin digunakan: \n\n1.rumus kecepatan\n2.luas segitiga\n3.luas balok\n4.luas bola\n\n0.keluar\n\nsilahkan pilih: "))
    if(userInput == 1):
        rumus_kecepatan()
    elif(userInput == 2):
        luas_segitiga()
    elif(userInput == 3):
        luas_balok()
    elif(userInput == 4):
        luas_bola()
    else: 
        break

