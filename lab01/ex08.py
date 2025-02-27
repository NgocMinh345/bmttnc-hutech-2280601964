# hàm kiểm tra số nhị phân có chia hết cho 5 hay không
def chia_het_cho_5(so_nhi_phan):
    # chuyển số nhị phân sang số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # kiểm tra số thập phân có chia hết cho 5 hay không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân(phân tách bởi dấu phẩy): ")
#tách chuỗi thành các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(",")
sochiahetcho5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
 #in ra các số nhị phân chia hết cho 5
if len(sochiahetcho5) > 0:
        ketqua = ",".join(sochiahetcho5)
        print("Các số nhị phân chia hết cho 5 là:", ketqua)
else:
        print("Không có số nhị phân nào chia hết cho 5")