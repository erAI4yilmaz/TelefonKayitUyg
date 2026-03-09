




#HATALAR; get() YERİNE başka bişey kullanmışız ve setdefault u yanlış kullanmışız






sozluk= {
    'ali':'321',
    'mehmet':'532'
    
    
    
    }


while True:
    print(
        """ 
        1-numara sorgula
        2-numara ekle
        3-numara sil
        4-çıkış
        
        """
        
        
        )
    secim=input("seçim: ")
    
    if secim=='1':
        kisi=input("sorgulanacak kişi: ")
        if kisi in sozluk.keys():
            print(sozluk.get(kisi))
        else:
            print("kişi listede yok")
            
    elif secim=='2':
        eklenecek=input("eklenecek kişi: ")
        numara=input("eklenecek numara: ")
        
        
        if eklenecek in sozluk.keys():
            print("eklenecek kişi listede var")
        else:
            sozluk.setdefault(eklenecek,numara)
            print("ekleme başarılı")
            
    elif secim=='3':
        silinecek=input("silinecek kişi: ")
        if silinecek in sozluk.keys():
            sozluk.pop(silinecek)
            print("silme başarılı")
        else:
            print("silinecek kişi listede yok")
            
    elif secim =='4':
        break
    else:
        print("yanlış kod girdiniz")