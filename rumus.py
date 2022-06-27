print("RUMUS MATEMATIKA DASAR by ZNAINDEV" "\n")
print("https://github.com/veldanava" "\n")

#dibuat oleh znaindev

print('========{v.1.0 by znaindev}========')

#rumus kecepatan.
def rumus_kecepatan():
    print('hitung kecepatan')
    jarak = int(input('masukan jarak:'))
    waktu = int(input('masukan waktu:'))
    kecepatan = jarak * waktu
    print("kecepatan yang didapat adalah: ", kecepatan, "\n")

#rumus segitiga
def luas_segitiga():
    print('hitung luas segitiga')
    alas = int(input('masukan alas:'))
    tinggi = int(input('masukan tinggi:'))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga adalah: ", luas, "\n")

#rumus balok
def luas_balok():
    print('hitung luas balok')
    panjang = int(input('masukan panjang balok:'))
    lebar = int(input('masukan lebar balok:'))
    tinggi = int(input('masukan tinggi balok:'))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok adalah: ", luas, "\n")


#rumus jajar genjang
def luas_jajar_genjang():
    print('hitung luas jajar genjang')
    alas = int(input('masukan alas jajar genjang:'))
    tinggi = int(input('masukan tinggi jajar genjang:'))
    luas = alas * tinggi
    print("luas jajar genjang adalah: ", luas, "\n")

#rumus bola
def luas_bola():
    print('hitung luas bola')
    r = int(input('masukan jari-jari:'))
    luas = 4 * 3.14 * (r**2)
    print("luas bola adalah: ", luas, "\n")

#belah ketupat
def ketupat():
    print('menghitung luas belah ketupat:')
    diagonalsatu = int(input('masukan diagonal satu:'))
    diagonaldua = int(input('masukan diagonal dua:'))
    luas = (0.5 * diagonalsatu * diagonaldua)
    print("luas belah ketupat yang didapat adalah: ", luas, "\n")

#rumus skala
def skala():
    print('hitung skala pada peta')
    jarakpeta = int(input('masukan jarak peta:'))
    jaraksebenar = int(input('jarak sebenarnya:'))
    skala = (jarakpeta / jaraksebenar)
    print("skala yang didapat adalah: ", skala, "\n")

#rumus barisan deret aritmatika
def deret():
    print('menghitung deret aritmatika')
    sukupertama = int(input('masukan suku pertama:'))
    banyaksuku = int(input('banyak suku (N):'))
    sukuN = float(input('masukan suku ke-N:'))
    deret = banyaksuku / 2 , (sukupertama + sukuN)
    print("deret barisan yang didapat adalah: ", deret, "\n")

#pembagian
def bagi():
    print('menghitung pembagian:')
    pertama = int(input('masukan bilangan pertama:'))
    kedua = int(input('masukan bilangan kedua:'))
    bagi = pertama / kedua
    print("hasil pembagian yang didapat adalah: ", bagi, "\n")

#perkalian
def kali():
    print('menghitung perkalian:')
    satu = int(input('masukan bilangan pertama:'))
    dua = int(input('masukan bilangan kedua:'))
    kali = satu * dua
    print("hasil perkalian yang didapat adalah: ", kali, "\n")

#diskon
def diskon():
    print('menghitung diskon suatu barang:')
    diskon = int(input('masukan diskon suatu barang dalam bentuk persen:'))
    barang = float(input('masukan harga barang:'))
    diskon = diskon / 100 * barang
    print("harga yang didapat setelah diskon adalah: ", diskon, "\n")

#pinjaman
def pinjaman():
    print('menghitung pinjaman perbulan:')
    jumlahpinjaman = float(input('masukan jumlah pinjaman:'))
    angsuran = int(input('masukan nilai angsuran:'))
    bunga = float(input('masukan jumlah bunga:'))
    pinjaman = (jumlahpinjaman / angsuran * bunga/100)
    print("maka angsuran yang harus dibayar adalah: ", pinjaman, "\n")

#function
while True:
    userInput = int(input(
        "pilih rumus yg ingin digunakan: \n\n1.hitung kecepatan\n2.luas segitiga\n3.luas balok\n4.luas bola\n5.jajar genjang\n6.skala\n7.deret aritmatika\n8.pembagian\n9.perkalian\n10.diskon\n11.pinjaman\n12.belah ketupat\n\n0.keluar\n\nsilahkan pilih: "))
    if(userInput == 1):
        rumus_kecepatan()
    elif(userInput == 2):
        luas_segitiga()
    elif(userInput == 3):
        luas_balok()
    elif(userInput == 4):
        luas_bola()
    elif(userInput == 5):
        luas_jajar_genjang()
    elif(userInput == 6):
        skala()
    elif(userInput == 7):
        deret()
    elif(userInput == 8):
        bagi()
    elif(userInput == 9):
        kali()
    elif(userInput == 10):
        diskon()
    elif(userInput == 11):
        pinjaman()
    elif(userInput == 12):
        ketupat()
    else: 
        break

