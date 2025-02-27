sogiolam = float(input("Số giờ làm mỗi tuần: "))
luonggio = float(input("Lương mỗi giờ: "))
giotieuchuan = 44 #số giờ làm chuẩn mỗi tuần
#số giờ làm vượt chuẩn mỗi tuần
sogiovuotchuan = max(0, sogiolam - giotieuchuan)
#tính tổng thu nhập
thuclinh =giotieuchuan * luonggio + sogiovuotchuan * luonggio * 1.5
print("Tổng thu nhập hàng tháng của bạn là: ", thuclinh)