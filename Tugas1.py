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
# Masuk ke dalam loop pemesanan
    while True:
        order = input("\nSilahkan ketik pesanan Anda: ")

        # Jika pengguna mengetik "done," keluar dari loop
        if order.lower() == "done":
            break

        current = head
        # Mencari item-menu dalam linked list
        while current is not None:
            if current.NamaMenu == order:
                # Menambahkan pesanan ke dalam array dan memperbarui total harga
                pesanan[Jml_Pesanan] = current.NamaMenu
                harga[Jml_Pesanan] = current.Harga
                Jml_Pesanan += 1
                total_harga += current.Harga
                print("Pesanan Anda", order, "sudah ditambahkan ke keranjang")
                break
            current = current.next

    # Menampilkan item yang dipesan dan total harga
    print("\nPesanan Anda:")
    for i in range(Jml_Pesanan):
        print(pesanan[i], "- Rp.", harga[i])

    print("Total harga pesanan Anda: Rp.", total_harga)
    print("Terima Kasih telah E-Order di Warung Kami")
