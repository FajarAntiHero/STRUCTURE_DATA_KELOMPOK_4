import numpy as np
import os

class MatrixHandler:
    def __init__(self):
        self.matrixA = None
        self.matrixB = None
        self.result = None
        self.namaA = ""
        self.namaB = ""
        self.opName = ""
        self.has_matrix = False
        self.combined = False

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def input_matrix(self, nama=""):
        x = int(input("Masukkan panjang Matriks (baris): "))
        y = int(input("Masukkan lebar Matriks (kolom): "))
        if not nama:
            nama = input("Masukkan nama Matriks: ")
        data = []
        for i in range(x):
            baris = []
            for j in range(y):
                val = float(input(f"{nama} Baris:[{i+1}] Kolom:[{j+1}] : "))
                baris.append(val)
            data.append(baris)
        return np.array(data), nama

    def show_menu(self):
        print("=== Menu Matriks ===")
        print("1. Input 2 Matriks")
        print("2. Operasikan Matriks (elemen-per-elemen)")
        print("3. Perkalian Matriks (dot product)")
        print("4. Hapus Matriks")
        print("0. Keluar")
        try:
            return int(input("Pilih menu: "))
        except ValueError:
            return -1

    def input_matrices(self):
        self.clear_terminal()
        self.matrixA, self.namaA = self.input_matrix()
        self.clear_terminal()
        self.matrixB, self.namaB = self.input_matrix()
        self.has_matrix = True
        self.combined = False

    def operate_matrices(self):
        if not self.has_matrix:
            print("Silakan input matriks terlebih dahulu.")
        elif self.matrixA.shape != self.matrixB.shape:
            print("Dimensi matriks tidak cocok untuk operasi elemen-per-elemen.")
        else:
            op = input("Pilih operasi (+ - * /): ")
            try:
                if op == '+':
                    self.result = self.matrixA + self.matrixB
                    self.opName = "Penjumlahan"
                elif op == '-':
                    self.result = self.matrixA - self.matrixB
                    self.opName = "Pengurangan"
                elif op == '*':
                    self.result = self.matrixA * self.matrixB
                    self.opName = "Perkalian"
                elif op == '/':
                    if np.any(self.matrixB == 0):
                        raise ZeroDivisionError("Pembagian dengan nol.")
                    self.result = self.matrixA / self.matrixB
                    self.opName = "Pembagian"
                else:
                    print("Operasi tidak valid.")
                    input("Tekan Enter untuk kembali...")
                    return
                self.combined = True
            except Exception as e:
                print("Terjadi kesalahan saat operasi:", e)
        input("Tekan Enter untuk kembali...")

    def dot_product(self):
        if not self.has_matrix:
            print("Silakan input matriks terlebih dahulu.")
        elif self.matrixA.shape[1] != self.matrixB.shape[0]:
            print(f"Dimensi tidak cocok untuk dot product:\nKolom {self.namaA} harus sama dengan baris {self.namaB}")
        else:
            try:
                self.result = self.matrixA @ self.matrixB
                self.opName = "Perkalian Matriks (Dot Product)"
                self.combined = True
            except Exception as e:
                print("Terjadi kesalahan saat perkalian matriks:", e)
        input("Tekan Enter untuk kembali...")

    def clear_matrices(self):
        if not self.has_matrix:
            print("Belum ada matriks yang bisa dihapus.")
        else:
            if input("Yakin ingin menghapus semua matriks? (y/n): ").lower() == 'y':
                self.matrixA = self.matrixB = self.result = None
                self.namaA = self.namaB = self.opName = ""
                self.has_matrix = self.combined = False
                print("Matriks berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
        input("Tekan Enter untuk kembali...")

    def main(self):
        while True:
            self.clear_terminal()
            if self.has_matrix:
                print(f"Matriks {self.namaA}:\n{self.matrixA}\n")
                print(f"Matriks {self.namaB}:\n{self.matrixB}\n")
            if self.combined:
                print(f"Hasil {self.opName}:\n{self.result}\n")

            menu = self.show_menu()

            if menu == 1:
                self.input_matrices()
            elif menu == 2:
                self.operate_matrices()
            elif menu == 3:
                self.dot_product()
            elif menu == 4:
                self.clear_matrices()
            elif menu == 0:
                print("Keluar dari sub-program matrix...")
                break
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")