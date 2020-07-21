
import random

print(""" 
--------------- 21 Oyununa Hoşgeldiniz. ------------------


-----------------------KURALLAR---------------------------
Puanınız, rakibin puanından büyük ise kazanırsınız
Puanınız 21 olursa direkt kazanırsınız.
Puanınız 21'i geçerse direkt kaybedersiniz.
----------------------------------------------------------
""")

kullaniciadi = input("Başlamak için ENTER'a basınız ")

rakipkart1=random.randint(1,10)
kullanicikart1=random.randint(1,10)

rakipkart2=random.randint(1,10)
kullanicikart2=random.randint(1,10)

rakipsonuc1=rakipkart1+rakipkart2
kullanicisonuc1=kullanicikart1+kullanicikart2


print("\nİlk Kart Puanınız:", kullanicikart1)
print("İkinci Kart Puanınız:", kullanicikart2)
print("Toplam Kart Puaniniz:", kullanicisonuc1)

print("\nRakip İlk Kart Puanı:", rakipkart1)
print("Rakip İkinci Kart Puanı:", rakipkart2)
print("Rakip Toplam Kart Puanı:", rakipsonuc1,"\n")

devam1 = input("""Kart çekmek istiyor musunuz?(e/h): """)

if devam1 == "e" and rakipsonuc1<=16:
	rakipkart3=random.randint(1,10)
	kullanicikart3=random.randint(1,10)

	rakipsonuc2=rakipsonuc1+rakipkart3
	kullanicisonuc2=kullanicisonuc1+kullanicikart3
	print("\n")
	print("Yeni Toplam Kart Puaniniz:", kullanicisonuc2)
	print("Yeni Rakip Toplam Kart Puanı:", rakipsonuc2)
	if rakipsonuc2>kullanicisonuc2 and rakipsonuc2<22:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc2>rakipsonuc2 and kullanicisonuc2<22:			
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif rakipsonuc2>22 and kullanicisonuc2>22:
		print("\n !!!! BERABERE !!!!\n")
	elif rakipsonuc2 == 21 and kullanicisonuc2!=21:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc2 == 21 and rakipsonuc2!=21:
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif kullanicisonuc2==rakipsonuc2:
		print("\n !!!! BERABERE !!!! \n")
	elif kullanicisonuc2>21 and rakipsonuc2<22:
		print("\n !!!! KAYBETTİN !!!!\n")
	elif rakipsonuc2>21 and kullanicisonuc2<22:
		print("\n", "!!!! KAZANDIN !!!!\n")

elif devam1 == "e" and rakipsonuc1>16:

	kullanicikart3=random.randint(1,10)
	kullanicisonuc3=kullanicisonuc1+kullanicikart3
	print("\n")
	print('Yeni Kart Puaniniz: ', kullanicisonuc3)
	print('Rakip Toplam Kart Puanı: ', rakipsonuc1)

	
	if rakipsonuc1>kullanicisonuc3 and rakipsonuc1<22:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc3>rakipsonuc1 and kullanicisonuc3<22:			
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif rakipsonuc1>22 and kullanicisonuc3>22:
		print("\n !!!! BERABERE !!!!\n")
	elif rakipsonuc1 == 21 and kullanicisonuc3!=21:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc3 == 21 and rakipsonuc1!=21:
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif kullanicisonuc3>21 and rakipsonuc1<22:
		print("\n !!!! KAYBETTİN !!!!\n")
	elif rakipsonuc1>21 and kullanicisonuc3<22:
		print("\n", "!!!! KAZANDIN !!!!\n")


elif devam1 == "h" and rakipsonuc1<=16:
		
	rakipkart3=random.randint(1,10)
	rakipsonuc2=rakipsonuc1+rakipkart3
		
	print("\n")
	print("Toplam Kart Puaniniz:", kullanicisonuc1)
	print("Rakip Toplam Kart Puanı:", rakipsonuc2)

	if rakipsonuc2>kullanicisonuc1 and rakipsonuc2<22:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc1>rakipsonuc2 and kullanicisonuc1<22:			
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif rakipsonuc2>22 and kullanicisonuc1>22:
		print("\n !!!! BERABERE !!!!\n")
	elif rakipsonuc2 == 21 and kullanicisonuc1!=21:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc1 == 21 and rakipsonuc2!=21:
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif kullanicisonuc1>21 and rakipsonuc2<22:
		print("\n !!!! KAYBETTİN !!!!\n")
	elif rakipsonuc2>21 and kullanicisonuc1<22:
		print("\n", "!!!! KAZANDIN !!!!\n")


elif devam1 == "h" and rakipsonuc1>16:
		
	print("\n")
	print("Toplam Kart Puaniniz:", kullanicisonuc1)
	print("Rakip Toplam Kart Puanı:", rakipsonuc1)

	if rakipsonuc1>kullanicisonuc1 and rakipsonuc1<22:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc1>rakipsonuc1 and kullanicisonuc1<22:			
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif rakipsonuc1>22 and kullanicisonuc1>22:
		print("\n !!!! BERABERE !!!!\n")
	elif rakipsonuc1 == 21 and kullanicisonuc1!=21:
		print("\n", "!!!! KAYBETTİN !!!!\n")
	elif kullanicisonuc1 == 21 and rakipsonuc1!=21:
		print("\n", "!!!! KAZANDIN !!!!\n")
	elif kullanicisonuc1>21 and rakipsonuc1<22:
		print("\n !!!! KAYBETTİN !!!!\n")
	elif rakipsonuc1>21 and kullanicisonuc1<22:
		print("\n", "!!!! KAZANDIN !!!!\n")

else:
	print("Geçersiz komut!!")
