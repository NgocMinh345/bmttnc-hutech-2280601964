def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Moi ban nhap chuoi dao nguoc: ")
print("Chuoi dao nguoc la:", dao_nguoc_chuoi(input_string))