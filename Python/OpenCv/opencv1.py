
import cv2

gambar = cv2.imread("foto.png")

if gambar is None:
    print("Foto tidak ditemukan!")

else:
    tinggi, lebar = gambar.shape[:2]
    skala = min(800 / lebar, 600 / tinggi, 1)

    gambar = cv2.resize(
        gambar,
        (int(lebar * skala), int(tinggi * skala))
    )

    while True:
        print("\n=== MINI PHOTO EDITOR ===")
        print("1. Gambar asli")
        print("2. Hitam putih")
        print("3. Efek blur")
        print("4. Deteksi tepi")
        print("5. Simpan gambar")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            hasil = gambar.copy()

        elif pilihan == "2":
            hasil = cv2.cvtColor(
                gambar, cv2.COLOR_BGR2GRAY
            )

        elif pilihan == "3":
            hasil = cv2.GaussianBlur(
                gambar, (15, 15), 0
            )

        elif pilihan == "4":
            abu = cv2.cvtColor(
                gambar, cv2.COLOR_BGR2GRAY
            )
            hasil = cv2.Canny(abu, 100, 200)

        elif pilihan == "5":
            print("Pilih menu 1-4 dahulu untuk membuat hasil.")
            continue

        elif pilihan == "6":
            break

        else:
            print("Pilihan tidak valid!")
            continue

        if pilihan in ("1", "2", "3", "4"):
            cv2.imshow("Mini Photo Editor", hasil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if pilihan in ("1", "2", "3", "4"):
            simpan = input("Simpan hasil ini? (y/n): ").lower()

            if simpan == "y":
                cv2.imwrite("hasil_edit.jpg", hasil)
                print("Hasil berhasil disimpan!")

    cv2.destroyAllWindows()
    print("Program selesai!")
