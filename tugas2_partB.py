def cetak_nilai_ganjil_dikuadrat(n):
    for i in range(n):
        if i % 2 != 0: 
            print(i**2)

n = int(input("Masukkan nilai n: "))
cetak_nilai_ganjil_dikuadrat(n)