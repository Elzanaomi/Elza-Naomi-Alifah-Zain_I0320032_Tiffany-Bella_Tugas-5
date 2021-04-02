# input nama dan jenis kelamin
nama = input("Masukkan Nama Anda :")
jk = input("Masukkan Jenis Kelamin Anda (l/p) :")

# output menyapa pengunjung
if jk == "l" :
    print("Selamat datang, Tuan",nama,"!")
elif jk == "p" :
    print("Selamat datang, Nyonya",nama,"!")