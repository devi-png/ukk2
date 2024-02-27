def pertambahan (a,b):
    return a + b
def pengurangan (a,b):
    return a - b
def perkalian (a,b):
    return a * b
def pembagian (a,b):
    if b == 0:
        print("Erorr !!! Maaf tidak bisa dibagi dengan bilangan 0")
    else:
        return a / b
while True:
    print("Selamat Datang dikalkulator Sederhana")
    print("Semoga Bisa Membantu Anda")
    print("==================================")
    a =int(input("Masukan Angka Pertama :"))
    b =int(input("Masukan Angka Kedua :"))
    print("Masukan Pilihan Operasi \n" \
          "1. pertambahan \n" \
          "2. pengurangan \n" \
          "3. perkalian \n" \
          "4. pembagian \n"
          "5. keluar")
    pilih =int(input("Masukan Operasi yang anda inginkan 1,2,3,4,5 :"))
    
    if pilih == 1:
        print(a,"+",b,"=", pertambahan(a,b))
    elif pilih == 2:
        print(a,"-",b,"=", pengurangan(a,b))
    elif pilih == 3:
        print(a,"*",b,"=", perkalian (a,b))
    elif pilih == 4:
        print(a,"/",b,"=", pembagian (a,b))
    elif pilih == 5:
        break
    else:
        print("invalid input")