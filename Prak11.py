# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:19:54 2021
@author: Abdullah
"""

nama_file = ""
temp_update = ""
indeks = 0


def cek_file():
    global nama_file
    while True:
        nama_file = input("Masukkan nama file: ")
        try:
            open(nama_file)
            print("")
            break
        except FileNotFoundError:
            print("File tidak ditemukan\n")


def pilihan1():
    print("[1. BACA DATA]")
    print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3")
    print("--------------------------------")
    baca_data1 = open(nama_file)
    print(baca_data1.read())


def pilihan2():
    print("[2. MENCARI RATA-RATA NILAI PRAK TIAP MAHASISWA]")
    data_nilai = []
    baca_data2 = open(nama_file).readlines()
    nama = input("Masukkan nama mahasiswa: ").capitalize()
    for nilai in range(len(baca_data2)):
        data_nilai.append(baca_data2[nilai].split())
        if nama in data_nilai[nilai][0]:
            prak1, prak2, prak3 = int(data_nilai[nilai][1]), int(data_nilai[nilai][2]), int(data_nilai[nilai][3])
            print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3")
            print("--------------------------------")
            print("{} \t {} \t {} \t {}\n".format(nama, prak1, prak2, prak3))
            print("Rerata nilai praktikum {} =".format(nama), (prak1 + prak2 + prak3) / 3, "\n")
            break


def mulai():
    cek_file()

    while True:
        print("MENU")
        print("1. Baca Data")
        print("2. Mencari Nilai Rata-Rata Praktikum Mahasiswa")
        print("3. Update Nilai Praktikum Mahasiswa")
        print("4. Simpan Perubahan Nilai")
        print("5. Exit")
        pilihan = input("Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            pilihan1()

        elif pilihan == "2":
            pilihan2()

        elif pilihan == "5":
            print("[5. EXIT]")
            print("TERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, atau 5 untuk keluar\n")


if __name__ == "__main__":
    mulai()
