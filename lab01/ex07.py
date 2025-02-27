# nhập các dòng từ người dùng
print ("nhập các dòng văn bản(Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower == 'done':
        break
    lines.append(line)
    #chuyển các dòng thành chữ in hoa và in ra màn hình 
    print ("\nChữ in hoa của các dòng văn bản:")
    for line in lines:
        print (line.upper())