# Fungsi untuk menampilkan item-menu
def display_menu():
    global head
    current = head
    # Melintasi linked list dan mencetak nama dan harga menu
    while current is not None:
        print(current.NamaMenu, "Rp.", current.Harga)
        current = current.next

if __name__ == "__main__":
    print("Selamat Datang di E-Order Warung D4 MIE Ice Cream dan Mie Pedas tersedia di warung ini!!\n")
    print("DAFTAR MENU WARUNG D4 MIE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Menambahkan beberapa item-menu
    add_menu_item("Miexue Ice Cream", 5000)
    add_menu_item("Boba Shake", 16000)
    add_menu_item("Mi Sundae", 14000)
    add_menu_item("Mi Ganas", 11000)
    add_menu_item("Creamy Mango Boba", 22000)

    # Menampilkan menu
    display_menu()

    # Menginisialisasi variabel untuk mengelola pesanan
    MaxPesanan = 10
    pesanan = [None] * MaxPesanan
    harga = [0] * MaxPesanan
    Jml_Pesanan = 0
    total_harga = 0

