class Library:
    def __init__(self):
        self.f = open("books.txt", "a+")
        self.deleted = []
        self.book = []

    def __del__(self):
        self.f.close()

    def list_books(self):
        # Dosyanın başına git
        self.f.seek(0)
        # Dosyadaki tüm satırları oku ve her satırı bir listeye at
        book_list = self.f.read().splitlines()
        # Her bir satırdaki kitap bilgilerini ayırarak ekrana yazdır
        for book_info in book_list:
            # Satırı virgülle ayır
            book_data = book_info.split(',')
            # Eğer beklenen dört değer yoksa, satırı atla ve bir uyarı ver
            if len(book_data) < 4 :
                if book_info in self.deleted:
                    continue
                
                x=f"Invalid data format in line: {book_info}. Skipping..."
                continue
            
            book_name, book_author, release_year, book_pages = book_data
            #book_data listesinin her bir öğesini sırasıyla 
            #book_name, book_author, release_year ve book_pages değişkenlerine atar. 
            print(f"Book: {book_name}  Author: {book_author}")

    def add_book(self):
        book_name = input("Please enter the title of the book:")
        book_author = input("Please enter the author's name of the book:")
        release_year = input("Please enter the publication year of the book:")
        book_pages = input("Please enter the number of pages of the book:")

        information = f"\n{book_name},{book_author},{release_year},{book_pages}"

        self.f.write(information)

    def remove_book(self):
        delete = input("Please enter the title of the book to be deleted:")
        # Dosyanın başına git
        self.f.seek(0)
        # Dosyadaki tüm satırları oku ve her satırı bir listeye at
        book_list = self.f.readlines()
        # Kaldırılacak kitabı bul
        for book_info in book_list:
            # Satırı virgülle ayır
            book_data = book_info.strip().split(',')
            if len(book_data) < 4: 
                continue
            book_title = book_data[0]
            # Kitabın listedeki index'ini bul
            if delete == book_title:
                print(f"The book named {delete} got deleted.")
                
                self.deleted.append(book_info)
                book_list.remove(book_info)
                break
        else:
            print(f"The book titled {delete} does not exist.")
            return

        # Dosyanın içeriğini temizle
        self.f.seek(0)
        self.f.truncate()
        # Yeni kitap listesini dosyaya yaz
        for book_info in book_list:
            self.f.write(book_info)

    def search_book(self):
        word = input("Aramak istediğiniz yazarı veya kitabı giriniz: ").lower()  # Küçük harfe dönüştür
        found = False  # Kitabın veya yazarın bulunup bulunmadığını belirlemek için bir bdeğişken
        
        # Dosyanın başına git
        self.f.seek(0)
        # Dosyadaki tüm satırları oku ve her satırı bir listeye at
        book_list = self.f.read().splitlines()
        
        # Her bir satırı kontrol et
        for book_info in book_list:
            # Satırı virgülle ayır
            book_data = book_info.split(',')
            if len(book_data) < 4:
                continue
            
            book_name, book_author, _, _ = book_data  # Kitap adı ve yazarı
            # Kitap adını ve yazar adını küçük harfe dönüştür
            book_name_lower = book_name.lower() 
            #Listede büyük-küçük harfle yazılmış olsa bile arama yapılırken bu dikkate alınmaz.
            book_author_lower = book_author.lower()
            # Aranan kelime kitap adında veya yazar adında geçiyorsa
            if word in book_name_lower or word in book_author_lower:
                found = True
                print(f"Book: {book_name}  Author: {book_author}")

        # Eğer kitap veya yazar bulunmadıysa
        if not found:
            print("Aradığınız kitap/yazar listede bulunmamaktadır.")


lib = Library()
while True:
    print("\n")
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search Book ")
    print("5) Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    print("\n")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice=='4':
        lib.search_book()
    elif choice == '5':
        print("Bye Bye...")
        break
    else:
        print("You entered wrong input.")