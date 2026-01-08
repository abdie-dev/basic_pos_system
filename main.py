# system pos
gudang = {"sku": 123123123, "nama": "sepatu", "harga": 2000, "stok": 20}
print(gudang["nama"])


def role(role):
    if role != "spv":
        input_barang()


def input_barang():
<<<<<<< HEAD
    barang = input("masukan barang : ").strip().lower()
    jumlah = int(input("masukan jumlah : "))
    if barang in gudang["nama"] and jumlah <= gudang["stok"]:
        print(
            "barang {a} tersedia dan stok nya tersedia {b} lagi".format(
                a=gudang["nama"], b=gudang["stok"] - jumlah
=======
    barang = input("masukan barang").strip().lower()
    jumlah = int(input("masukan jumlah : "))
    if barang in gudang["nama"] and jumlah <= gudang["stok"]:
        print(
            "barang {a} tersedia dan stok nya tersedia {b}".format(
                a=gudang["nama"], b=gudang["stok"]
>>>>>>> 30a4d132d49aec2cb65030b668ba84d234b16011
            )
        )
        transaksi(jumlah)
    else:
        if barang != gudang["nama"]:
            print("barang tidak ada")
        else:
            if gudang["stok"] <= 0:
                print(
                    "stok tidak mencukupi!! ( tersisa : {a} di gudang) ".format(
                        a=gudang["stok"]
                    )
                )


def transaksi(jumlah):
    ask_cont = input("masih ada barang lain (y/n)").lower()
    if ask_cont == "y":
        gudang["stok"] -= jumlah
        return input_barang()
    else:
        ask_pembayaran = int(input("jenis pembayaran \n1. Cash\n2. Tunai\nPilihan : "))
        try:
            if ask_pembayaran == 2:
                total_belanja = jumlah * gudang["harga"]
                print("total belanja nya : {a}".format(a=total_belanja))
            elif ask_pembayaran == 1:
                uang_diterima = int(input("uang di terima : "))
                total_belanja = jumlah * gudang["harga"]
                try:
                    if uang_diterima <= total_belanja:
                        hitung_kurang = uang_diterima - total_belanja
                        print(f"maaf uang nya kurang : {hitung_kurang}")
                    else:
                        print(
                            "total belanjaan : {a}\nuang diterima : {b}".format(
                                a=total_belanja, b=uang_diterima
                            )
                        )
                        hitung_kembalian(uang_diterima, total_belanja)
                except ValueError:
                    print(ValueError)
            else:
                return ValueError

        except ValueError:
            print("pilih jenis pembayaran")


def hitung_kembalian(uang, total):
    kembalian = uang - total
    print(f"kembalian : {kembalian}")


def __lihat_laporan__():
    laporan = {input_barang()}
    return laporan


def start():
    crole = input("masukan role kamu : ").lower()
    role(crole)


start()
