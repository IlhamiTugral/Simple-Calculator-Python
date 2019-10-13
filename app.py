"""
Konsol Hesap Makinası Uygulaması
Author: Ilhami Tugral
Date: 13/10/19
"""

num1 = 0
num2 = 0
operation = 0
status = True

print("+---| Hesap Makinası |----+")
print("|                         |")
print("| 1-) Toplama İşlemi      |")
print("| 2-) Çıkarma İşlemi      |")
print("| 3-) Çarpma İşlemi       |")
print("| 4-) Bölme İşlemi        |")
print("| 5-) Kalan Hesaplama     |")
print("|                         |")
print("| 0-) Cikis               |")
print("+-------------------------+")
print("\n")

while status:
    operation = int(input("İşlem türünü seçiniz: "))
    
    if operation <= 5:
        if operation != 0:
            num1 = float(input("Birinci Sayı: "))
            num2 = float(input("İkinci Sayı: "))
        else:
            print("Geçersiz işlem türü")
        
        if operation == 1:
            print(num1, " + ", num2, " = ", (num1+num2))
        elif operation == 2:
            print(num1, " - ", num2, " = ", (num1-num2))
        elif operation == 3:
            print(num1, " * ", num2, " = ", (num1*num2))
        elif operation == 4:
            print(num1, " / ", num2, " = ", (num1/num2))
        elif operation == 5:
            print(num1, " % ", num2, " = ", (num1%num2))
        else:
            print("Hesap Makinasından çıkılıyor...")
            status = False
    print("\n")