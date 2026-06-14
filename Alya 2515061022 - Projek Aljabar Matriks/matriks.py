import alya022 as ay

if __name__ == "__main__":
    A = ay.MATRIKS([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = ay.MATRIKS([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print(f"\nMatriks A : {A}")
    print(f"\nMatriks B : {B}")

    print(f"\nPenjumlahan A + B : {A.penjumlahan(B)}")
    print(f"\nPengurangan A - B : {A.pengurangan(B)}")
    print(f"\nPerkalian A x B   : {A.perkalian(B)}")