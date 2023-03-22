#mencari FPB
def hitungfpb(a, b): 
    #fungsi dengan nama hitungfpb
    if b == 0: 
        #membuat kondisi jika nilai b sama dengan 0
        return a 
        #mengembalikan nilai dari a
    else: 
        #jika kondisi tidak terpenuhi, maka program akan menjalankan bawahnya
        return hitungfpb(b, a % b) 
        #perumpamaan jika nilai b tidak sama dengan 0 maka akan memanggil fungsi a,b

#mencari KPK
def carikpk(a, b): 
    #fungsi dengan nama hitungkpk
    return (a * b) / hitungfpb(a, b) 
    #mengembalikan nilai berupa hasil perkalian dan memanggilan fungsi hitungfpb

def show():
    angka1 = int(input("Masukkan bilangan pertama: ")) 
    #inputan angka1 
    angka2 = int(input("Masukkan bilangan kedua: ")) 
    #inputan angka2
    print("Apa yang ingin kamu hitung?") 
    pil = int(input("Ketik 1 untuk FPB\nKetik 2 untuk KPK\n ")) 
    #pilihan menghitung fpb atau kpk
    
    
    if pil == 1: 
        #melakukan perhitungan fpb
        fpb = hitungfpb(angka1, angka2) 
        #memanggil fungsi variabel fpb
        print(f"FPB dari {angka1} dan {angka2} adalah {fpb}") 
        #memunculkan hasil
    
    elif pil == 2: 
        #melakukan perhitungan kpk
        kpk = hitungkpk(angka1, angka2) 
        #memanggil variabel kpk
        print(f"KPK dari {angka1} dan {angka2} adalah {kpk}") 
        #memunculkan hasil
    else:
        print("error") 
        #pesan muncul jika inputan salah
        
    lagi = int(input("Apakah ingin hitung lagi?\nketik 1 untuk lanjut\nketik 2 untuk keluar\n")) 
    #memasukkan inputan untuk perulangan atau tidak
    
    if lagi == 1:
        return show()
    elif lagi == 2:
        return exit() 
    #jika angka 1 yang dipilih maka akan terjadi perulangan
    #jika yang dipilih angka 2 maka berhenti
    else: 
        print("Error") 
        #pesan muncul ketika salah memasukkan input
        

show() 
#memanggil fungsi




