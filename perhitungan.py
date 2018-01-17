import os
#program  tanah daerah pontianak
print (35*'=')
print ("Pengecekkan harga tanah sekitar Pontianak")
print ("Dengan harga bervariasi sesuai lokasi")
print ("Pilihlah tanah yang strategis menurut anda")
print (35*'=')

print (35*'=')
print ("Masukkan Data Pembeli!")
nama = input ("Masukkan Nama Anda : ")
loop = True
while loop :
	jeniskelamin = input("Masukkan jenis kelamin anda(L/P) : ")
	if jeniskelamin.upper() == "L":
		jeniskelamin = "Laki Laki"
		loop = False
	elif jeniskelamin.upper() == "P":
		jeniskelamin = "Perempuan"	
		loop=False
	else :
		input("Jenis kelamin yang anda memasukkan salah, masukkan lagi !")
		os.system ('cls')
		print (35*'=')
		print ("Penjualan Tanah Daerah Pontianak")
		print ("Dengan harga bervariasi sesuai lokasi")
		print ("Pilihlah tanah yang strategis menurut anda")
		print (35*'=')

		print (35*'=')
		print ("Masukkan Data Pembeli!")
		print("Masukkan Nama Anda : " + str(nama))

alamat = input ("Masukkan Alamat Anda : ")
no_hp = int(input ("Masukkan No. Hp Anda : "))
print (35*'=')

print (35*'=')
print("Masukkan luas tanah yang anda inginkan (p,l)")
def cekAngka(angka, min, max):
  angka = int(angka)
  if(angka >= min and angka <= max):
    return True
  return False

def apakahAngka(angka):
	try:
		angka = int(angka)
		return True
	except ValueError:
		return False

def mintaAngka(pesan,min,max):
	a = input(pesan)
	if(not apakahAngka(a)):
		print("Harap Masukkan Angka !")
		return mintaAngka(pesan,min,max)
	if(not cekAngka(a,min,max)):
		print("Angka tidak boleh melebihi {} dan kurang dari {}".format(max,min))
		return mintaAngka(pesan,min,max)
	return int(a)
	
def tanyaPanjang():
	global harga,a,b
	a = mintaAngka("Masukkan panjang tanah ? [Min 10m Max 80m] : ",10,80)
	b = mintaAngka("Masukkan lebar tanah ? [Min 10m Max 80m] : ",10,80)
	harga = a*b
	if harga in range(100,401):
		harga = 20000000
	elif harga in range(400,801):
		harga = 30000000 
	elif harga in range(800,1201):
		harga = 40000000
	elif harga in range(1200,1601):
		harga = 50000000
	elif harga in range(1600,2001):
		harga = 60000000
	elif harga in range(2000,2401):
		harga = 70000000
	elif harga in range(2400,2801):
		harga = 80000000
	elif harga in range(2800,3201):
		harga = 90000000
	elif harga in range(3200,3601):
		harga = 100000000
	elif harga in range(3600,4001):
		harga = 110000000
	elif harga in range(4000,4401):
		harga = 120000000
	elif harga in range(4400,4801):
		harga = 130000000	
	elif harga in range(4800,5201):
		harga = 140000000	
	elif harga in range(5200,5601):
		harga = 150000000	
	elif harga in range(5600,6001):
		harga = 160000000
	elif harga in range(6000,6401):
		harga = 170000000	

tanyaPanjang()


print (35*'=')
#array
jarak = 0
bulan = ('Daerah Sekitar Jl. Ahmad Yani' , 'Daerah Sekitar Jl. Parit H. Husein I' , 'Daerah sekitar Jl. Parit H. Husein II' , 'Daerah Sekitar Jl. Ampera' , 'Daerah Sekitar Jl. Gajah Mada' , 'Daerah Sekitar Jl. Imam Bonjol' , 'Daerah Sekitar Jl. Danau Sentarum' ,
 'Daerah Sekitar Jl. Purnama' , 'Daerah Sekitar Jl. Adi Sucipto' , 'Daerah Sekitar Jl. TanjungPura' , 'Daerah Sekitar Jl. Perdana' , "Daerah Sekitar Jl. Merdeka","Daerah Sekitar Jl. Swignyo","Daerah Sekitar Pancasila","Daerah Sekitar Sungai Jawi","Daerah Sekitar UNTAN",
 "Daerah Sekitar Jeruju","Daerah Sekitar Kota Baru","Daerah Sekitar Tanjung Hulu","Daerah Sekitar Tanjung Raya")

nilai = [2600, 1700, 3500, 8100, 3300, 1500, 6200, 2700, 8400, 3300, 1600, 4500, 5800, 4900, 7400, 750, 7900, 6100, 5600, 4000]

while(jarak < 20):
	if(nilai[jarak]%1==0):
		print("Tanah di " + str(bulan[jarak]) + " Memiliki Jarak ke Pusat Kota " + str(nilai[jarak]) + ("m"))
	jarak = jarak + 1

import os
print (35*'=')
print("Daftar Lokasi Tanah :")
print("Lihat keterangan diatas")
print (35*'=')
def print_menu():
	print ("1. Daerah Sekitar Jl. Ahmad Yani", "			", "11. Daerah Sekitar Jl. Perdana")
	print ("2. Daerah Sekitar Jl. Parit H. Husein I", "		", "12. Daerah Sekitar Jl. Merdeka")
	print ("3. Daerah sekitar Jl. Parit H. Husein II", "		", "13. Daerah Sekitar Jl. Swignyo")
	print ("4. Daerah Sekitar Jl. Ampera", "				", "14. Daerah Sekitar Pancasila")
	print ("5. Daerah Sekitar Jl. Gajah Mada", "			", "15. Daerah Sekitar Sungai Jawi")
	print ("6. Daerah Sekitar Jl. Imam Bonjol", "			", "16. Daerah Sekitar UNTAN")
	print ("7. Daerah Sekitar Jl. Danau Sentarum", "			", "17. Daerah Sekitar Perum")
	print ("8. Daerah Sekitar Jl. Purnama", "				", "18. Daerah Sekitar Kota Baru")
	print ("9. Daerah Sekitar Jl. Adi Sucipto", "			", "19. Daerah Sekitar Tanjung Hulu")
	print ("10. Daerah Sekitar Jl. TanjungPura", "			", "20. Daerah Sekitar Tanjung Raya")


def pilihLokasi():
	global harga,a,b
	print_menu()
	choice = mintaAngka("Pilihlah lokasi yang anda inginkan : ",1,20)
	os.system('cls')
	if choice == 1:
		harga = harga + harga*12/100
	elif choice == 2:
		harga = harga + harga*6/100
	elif choice == 3:
		harga = harga + harga*7/100
	elif choice == 4:
		harga = harga - harga*5/100
	elif choice == 5:
		harga = harga + harga*11/100
	elif choice == 6:
		harga = harga + harga*3/100
	elif choice == 7:
		harga = harga + harga*2/100
	elif choice == 8:
		harga = harga + harga*5/100
	elif choice == 9:
		harga = harga + harga*3/100
	elif choice == 10:
		harga = harga + harga*9/100
	elif choice == 11:
		harga = harga + harga*7/100
	elif choice == 12:
		harga = harga - harga*3/100
	elif choice == 13:
		harga = harga + harga*1/100
	elif choice == 14:
		harga = harga + harga*4/100
	elif choice == 15:
		harga = harga + harga*2/100
	elif choice == 16:
		harga = harga + harga*4/100
	elif choice == 17:
		harga = harga - harga*5/100
	elif choice == 18:
		harga = harga - harga*2/100
	elif choice == 19:
		harga = harga - harga*6/100
	elif choice == 20:
		harga = harga - harga*3/100
	print("Nama 		 : ", nama)
	print("Jenis kelamin	 :  " +str(jeniskelamin))
	print("Alamat 		 : ", alamat)
	print("No. Hp 		 : ", no_hp)
	print("Luas Tanah	 : ", a,"*",b, "=", a*b, "m2")
	print("Perkiraan Harga Tanah yang Anda inginkan adalah")
	print("Rp ", harga)
	akhir = input("Apakah anda ingin mengulang lagi? [Y/N]")
	if(akhir.lower() == "y"):
		pilihLokasi()
	else:
		exit()
		
pilihLokasi()
