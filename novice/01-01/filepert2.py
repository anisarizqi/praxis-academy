#membatasi angka dibelakang koma
print('{0:.3f}'.format(1.0/3))

#memberi spasi
print('{0:^11}'.format('hello'))

#memanggil variabel
print('{nama} wrote {buku}'. format(nama='andi', buku='a byte of phyton'))

#escape sequece --> untuk mengatasi ambigu petik pada text
print('what\'s your name')

a=2

a = a * 3
a *= 3