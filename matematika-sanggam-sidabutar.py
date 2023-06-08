import os
import datetime 

def cmd():
    func = os.system()
    return func
def date():
    func = datetime.datetime.now()
    return func
def start():
    while True:
        password = input('password: ')
        if password == 'sanggam':
            class matematika():
                def tambah(self,a,b):
                    rumus = a + b
                    return rumus
                def kurang(self,a,b):
                    rumus = a - b
                    return rumus
                def kali(self,a,b):
                    rumus = a * b
                    return rumus
                def bagi(self,a,b):
                    rumus = a / b
                    return rumus
                def print(self):
                    try:
                        waktu = date()
                        tanggal = waktu.strftime('%d')
                        bulan = waktu.strftime('%B')
                        tahun = waktu.strftime('%Y')
                        print(tanggal,tahun,bulan)
                        angka = int(input('input angka pertama: '))
                        angka2 = int(input('input angka kedua: '))
                        operator = input('ketik nama operator: ')
                        if operator == 'tambah' or operator == 'Tambah':
                            hasil = self.tambah(angka,angka2)
                            print(hasil)
                            var_use = input('gunakan lagi?y/n ')
                            if var_use == 'y':
                                ulang = start()
                                print(ulang)
                            else:
                                print('program stop')
                                pesan = input('kirim pesan untuk author: ')
                                kirim = cmd(f'xdg-open https://wa.me/+6285275797174?text={pesan}')
                                print(kirim)
                        elif operator == 'kurang' or operator == 'Kurang':
                            hasil = self.kurang(angka,angka2)
                            print(hasil)
                            var_use = input('gunakan lagi?y/n ')
                            if var_use == 'y':
                                ulang = start()
                                print(ulang)
                            else:
                                print('program stop')
                                pesan = input('kirim pesan untuk author: ')
                                kirim = cmd(f'xdg-open https://wa.me/+6285275797174?text={pesan}')
                                print(kirim)
                        elif operator == 'kali' or operator == 'Kali':
                            hasil = self.kali(angka,angka2)
                            print(hasil)
                            var_use = input('gunakan lagi?y/n ')
                            if var_use == 'y':
                                ulang = start()
                                print(ulang)
                            else:
                                print('program stop')
                                pesan = input('kirim pesan untuk author: ')
                                kirim = cmd(f'xdg-open https://wa.me/+6285275797174?text={pesan}')
                                print(kirim)        
                        elif operator == 'bagi' or operator == 'Bagi':
                            hasil = self.bagi(angka,angka2)
                            print(hasil)
                            var_use = input('gunakan lagi?y/n ')
                            if var_use == 'y':
                                ulang = start()
                                print(ulang)
                            else:
                                print('program stop')
                                pesan = input('kirim pesan untuk author: ')
                                kirim = cmd(f'xdg-open https://wa.me/+6285275797174?text={pesan}')
                                print(kirim)
                        else:
                            print('operator tidak ada')
                            ulang = start()
                            print(ulang)
                    except ValueError:
                        print('harap masukan angka')
                        ulang = start()
                        print(ulang)
            var_object = matematika()
            var_object.print()
            break
mulai = start()        
print(mulai)


