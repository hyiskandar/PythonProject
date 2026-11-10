
import cv2
import numpy as np

# Membaca gambar
gambar = cv2.imread("foto.png")

if gambar is None:
    print("Foto tidak ditemukan!")
else:
    # Mengatur ukuran gambar
    tinggi, lebar = gambar.shape[:2]
    skala = min(800 / lebar, 600 / tinggi, 1)

    gambar = cv2.resize(
        gambar,
        (int(lebar * skala), int(tinggi * skala))
    )

    hasil = gambar.copy()

    while True:
        print("\n=== RGB COLOR LAB ===")
        print("1. Informasi gambar")
        print("2. Membaca warna piksel")
        print("3. Filter merah")
        print("4. Filter hijau")
        print("5. Filter biru")
        print("6. Tampilkan gambar asli")
        print("7. Simpan hasil")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            tinggi, lebar, channel = gambar.shape

            print("Lebar:", lebar)
            print("Tinggi:", tinggi)
            print("Channel warna:", channel)

            print("Total piksel:", tinggi * lebar)

        elif pilihan == "2":
            try:
                x = int(input("Masukkan koordinat X: "))
                y = int(input("Masukkan koordinat Y: "))

                if 0 <= x < lebar and 0 <= y < tinggi:
                    warna = gambar[y, x]

                    print("Nilai BGR:", warna)
                    print("Biru:", int(warna[0]))
                    print("Hijau:", int(warna[1]))
                    print("Merah:", int(warna[2]))
                else:
                    print("Koordinat di luar gambar!")

            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilihan == "3":
            hasil = gambar.copy()
            hasil[:, :, 0] = 0
            hasil[:, :, 1] = 0

            cv2.imshow("Filter Merah", hasil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif pilihan == "4":
            hasil = gambar.copy()
            hasil[:, :, 0] = 0
            hasil[:, :, 2] = 0

            cv2.imshow("Filter Hijau", hasil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif pilihan == "5":
            hasil = gambar.copy()
            hasil[:, :, 1] = 0
            hasil[:, :, 2] = 0

            cv2.imshow("Filter Biru", hasil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif pilihan == "6":
            hasil = gambar.copy()

            cv2.imshow("Gambar Asli", hasil)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif pilihan == "7":
            berhasil = cv2.imwrite("hasil_filter.jpg", hasil)

            if berhasil:
                print("Gambar tersimpan sebagai hasil_filter.jpg")
            else:
                print("Gagal menyimpan gambar!")

        elif pilihan == "8":
            cv2.destroyAllWindows()
            print("Terima kasih sudah belajar OpenCV!")
            break

        else:
            print("Pilihan tidak valid!")
