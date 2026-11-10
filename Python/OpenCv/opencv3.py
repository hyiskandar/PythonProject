
import cv2
import numpy as np

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

    hasil = gambar.copy()

    while True:
        print("\n=== IMAGE MANIPULATION LAB ===")
        print("1. Tampilkan gambar asli")
        print("2. Resize gambar")
        print("3. Crop gambar")
        print("4. Rotasi 90 derajat")
        print("5. Atur kecerahan")
        print("6. Atur kontras")
        print("7. Simpan hasil")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            hasil = gambar.copy()

        elif pilihan == "2":
            try:
                persen = float(input("Ukuran baru (%): "))

                if persen <= 0:
                    print("Ukuran harus lebih dari 0!")
                    continue

                tinggi, lebar = gambar.shape[:2]

                hasil = cv2.resize(
                    gambar,
                    (
                        max(1, int(lebar * persen / 100)),
                        max(1, int(tinggi * persen / 100))
                    )
                )

            except ValueError:
                print("Masukkan angka yang valid!")
                continue

        elif pilihan == "3":
            tinggi, lebar = gambar.shape[:2]

            x1 = lebar // 4
            y1 = tinggi // 4
            x2 = 3 * lebar // 4
            y2 = 3 * tinggi // 4

            hasil = gambar[y1:y2, x1:x2].copy()

        elif pilihan == "4":
            hasil = cv2.rotate(
                gambar,
                cv2.ROTATE_90_CLOCKWISE
            )

        elif pilihan == "5":
            try:
                nilai = int(input("Kecerahan (-100 sampai 100): "))

                if not -100 <= nilai <= 100:
                    print("Nilai harus antara -100 dan 100!")
                    continue

                hasil = cv2.convertScaleAbs(
                    gambar,
                    alpha=1,
                    beta=nilai
                )

            except ValueError:
                print("Masukkan bilangan bulat!")
                continue

        elif pilihan == "6":
            try:
                nilai = float(input("Kontras (0.5 sampai 3): "))

                if not 0.5 <= nilai <= 3:
                    print("Kontras harus antara 0.5 dan 3!")
                    continue

                hasil = cv2.convertScaleAbs(
                    gambar,
                    alpha=nilai,
                    beta=0
                )

            except ValueError:
                print("Masukkan angka yang valid!")
                continue

        elif pilihan == "7":
            berhasil = cv2.imwrite("hasil_edit.jpg", hasil)

            if berhasil:
                print("Hasil disimpan sebagai hasil_edit.jpg")
            else:
                print("Gagal menyimpan gambar!")

            continue

        elif pilihan == "8":
            break

        else:
            print("Pilihan tidak valid!")
            continue

        cv2.imshow("Image Manipulation Lab", hasil)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("Program selesai!")
