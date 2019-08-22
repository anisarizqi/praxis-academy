class Book:
	def __init__(self, name, author, dueDate):
		self.name = name
		self.author = author
		self.dueDate = dueDate

	def Checkout(self):
		print("Nama Buku 	= " + self.name)
		print("Penulis		=  " + self.author)
		print("Tanggal pinjam  =  " + self.dueDate)

buku = Book("Dilan 1991", "Pidi Baiq", "23 Agustus 2019")
buku.Checkout()
