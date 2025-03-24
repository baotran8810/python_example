# Nhập ba số thực dương a, b, c.
# 	1.	Kiểm tra xem a, b, c có thể là độ dài ba cạnh của một tam giác hay không. (Điều kiện tam giác: a + b > c, a + c > b, và b + c > a).
# 	2.	Nếu có thể tạo thành một tam giác, hãy xác định loại tam giác đó:
# 	•	Tam giác đều (các cạnh bằng nhau)
# 	•	Tam giác vuông (thỏa mãn định lý Pythagore: a^2 + b^2 = c^2 hoặc hoán vị các cạnh)
# 	•	Tam giác vuông cân (vừa vuông vừa có hai cạnh bằng nhau)
# 	•	Tam giác cân (có ít nhất hai cạnh bằng nhau nhưng không phải tam giác đều)
# 	•	Tam giác thường (không thuộc các loại trên)

# Yêu cầu in ra kết luận tương ứng với dữ liệu đầu vào.
def tamgiac():
    a = int(input("Nhập số thực dương a: "))
    b = int(input("Nhập số thực dương b: "))
    c = int(input("Nhập số thực dương c: "))    
    if a + b > c and a + c > b and b + c > a:
        if a ==b ==c:
            print("Tam giác đều")
        elif a**2 + b**2 >= c**2 or c**2 + b**2 >= a**2 or a**2 + b**2 >= c**2:
            print("Tam giác vuông")
            if a == b or b == c or a == c:
                print("Tam giác vuông cân")
        elif a == b or b == c or a == c:
            print("Tam giác cân")
        else: print("Tam giác thường")
    else: print("Đây không phải là tam giác")

# Đề bài:
# Viết chương trình cho phép người dùng nhập vào một tháng và một năm (cả hai đều là số nguyên). Hãy xác định và in ra số ngày của tháng đó trong năm tương ứng.
def mmyyyy():
    m = int(input(("Nhập vào tháng ")))
    y = int(input(("Nhập vào năm ")))
    if 1<=m<=12 and y>0:
        if m ==1 or m==3 or m== 5 or m==7 or m==8 or m==10 or m==12:
            print(f"Tháng {m} có 31 ngày")
        elif m ==2:
            if y%4==0:
                print(f"Tháng {m} có 29 ngày")
            else: print(f"Tháng {m} có 28 ngày")
        else: print(f"Tháng {m} có 30 ngày")
    else: print("Nhập cái gì có nghĩa giùm")
# Yêu cầu chi tiết:
# 	1.	Tháng là giá trị nguyên trong khoảng 1 \leq \text{tháng} \le 12.
# 	2.	Năm là giá trị nguyên dương, ví dụ 2023, 2024, v.v.
# 	3.	Đối với các tháng 1,3,5,7,8,10,12: số ngày là 31.
# 	4.	Đối với các tháng 4,6,9,11: số ngày là 30.
# 	5.	Riêng tháng 2:
# 	•	28 ngày đối với năm thường,
# 	•	29 ngày nếu là năm nhuận.
# 	6.	Năm nhuận xác định theo nguyên tắc:
# 	•	Năm chia hết cho 400 → năm nhuận,
# 	•	hoặc năm chia hết cho 4 và không chia hết cho 100 → năm nhuận.
# 	•	(Ngược lại là năm thường.)

# Ví dụ minh họa:
# 	•	Nhập tháng = 2, năm = 2024 → Kết quả: “29 ngày” (vì 2024 là năm nhuận).
# 	•	Nhập tháng = 2, năm = 2023 → Kết quả: “28 ngày”.
# 	•	Nhập tháng = 11, năm = 2025 → Kết quả: “30 ngày”.


# Đề bài:
# Viết chương trình cho phép người dùng nhập vào một số nguyên dương a. Hãy in ra bảng cửu chương của số a đó theo định dạng thông thường (từ phép nhân 1 đến phép nhân 10).
def bcc():
    a = int(input("Nhập số nguyên a: "))
    print(f"Bảng cửu chương {a} là:")
    for i in range (1,11):
        print(f" {a} x {i} = {a*i}")

# Nhập vào danh sách học sinh gồm n học sinh, mỗi học sinh gồm các thông tin: họ tên, điểm môn toán, lý, hóa. Yêu cầu:
# 1. In ra danh sách học sinh và điểm từng môn + điểm trung bình.
# 2. Tính điểm trung bình của cả lớp.
# 3. Tìm học sinh có điểm trung bình cao nhất và thấp nhất.
# 4. In ra danh sách điểm trung bình theo thứ tự giảm dần.
# 5. In ra danh sách học sinh có điểm trung bình dưới 5.
def danhsach():
    listHoTen = []
    listDiemToan = []
    listDiemLy = []
    listDiemHoa = []
    listDiemTB = []
    n=int(input("Số lượng học sinh: "))
    for i in range (1,n+1):
        hoten = input(f"Nhap ho ten cua hoc sinh {i}: ")
        listHoTen.append(hoten)
        diemtoan = float(input(f"Nhap diem toan cua hoc sinh {i}: "))
        listDiemToan.append(diemtoan)
        diemly = float(input(f"Nhap diem ly cua hoc sinh {i}: "))
        listDiemLy.append(diemly)
        diemhoa = float(input(f"Nhap diem hoa cua hoc sinh {i}: "))
        listDiemHoa.append(diemhoa)
        dtb = (diemtoan + diemly + diemhoa)/3
        listDiemTB.append(dtb)
    print(f"Ho ten: {listHoTen}")
    print(f"Diem toan {listDiemToan}")
    print(f"Diem ly {listDiemLy}")
    print(f"Diem hoa {listDiemHoa}")
    print(f"Diem trung binh {listDiemTB}")
    print(f"Diemtrung binh cua ca lop la:  {sum(listDiemTB)/n}")

    caoDiem = 0;
    thapDiem =0;
    for i in range (0,n):
        if listDiemTB[i] == max(listDiemTB):
            caoDiem = i
            
        if listDiemTB[i] == min(listDiemTB):
            thapDiem = i
            
    print(f"Hoc sinh co diem trung binh cao nhat la {listHoTen[caoDiem]}")
    print(f"Hoc sinh co diem trung binh thap nhat la {listHoTen[thapDiem]}")

    print(f"Danh sach diem trung binh theo thu tu giam dan la: {listDiemTB.sort(reverse=True)}")
    print("Danh sach hoc sinh co diem trung binh duoi 5 la ")
    for i in range (0,n):
        if listDiemTB[i] <= 5:
            print({listHoTen[i]})

# Đề bài: Quản lý đơn hàng trong cửa hàng trực tuyến
def quanlydonhang():
    listDonhang = []
    n = int(input("Số lượng đơn hàng cần thêm vào là: "))
    i = 0;
    while i < n:
        donhang = input(f"Nhập đơn hàng số {i+1} ").split(",")
        # print(donhang[2])
        if donhang[2].lower() == "true":
            donhang[2] = True
        elif donhang[2].lower() == "false":
            donhang[2] = False
        else: 
            print("Nhập cho đúng True/False")
            continue
        thongtindonhang = [donhang[0],int(donhang[1]),donhang[2]]
        # if len(thongtindonhang) != 3 :
        #     print("Nhập cho đúng 3 phần tử!!! ")
        # else:
        listDonhang.append(thongtindonhang)
        i+=1
    # for i in range (1,n+1):
        #"don hang a, 123, True "
        #["donh", int(123), "True"]
  

        # madonhang = str(input(f"Nhập đơn hàng thứ {i}: "))
        # giatri = int(input(f"Nhập giá trị đơn hàng {i}: "))
        # trangthai = bool(int(input(f"Trạng thái đơn hàng {i}: ")))
        #2
        # donhang = [madonhang,giatri,trangthai]
        # listDonhang.append(thongtindonhang)
    print(listDonhang)
    Tongdoanhthu = 0
    Doncogiatricaonhat = listDonhang[0]
    listChuagiao = []
    for i in range (0,n):
        if listDonhang[i][2] == True:
            Tongdoanhthu = Tongdoanhthu + listDonhang[i][1]
    
        if listDonhang[i][1] > Doncogiatricaonhat[1]:
            Doncogiatricaonhat = listDonhang[i]
    
        if listDonhang[i][2] == False:
            listChuagiao.append(listDonhang[i])

    print(Tongdoanhthu)
    print(Doncogiatricaonhat)
    print(listChuagiao)

# Một cửa hàng trực tuyến cần quản lý danh sách đơn hàng của khách. Mỗi đơn hàng bao gồm:
#   •  Mã đơn hàng (kiểu str)
#   •  Tổng giá trị đơn hàng (kiểu int)
#   •  Trạng thái giao hàng (kiểu bool), trong đó True là đã giao, False là chưa giao.

# Cửa hàng lưu danh sách đơn hàng dưới dạng list, trong đó mỗi đơn hàng được biểu diễn bằng một List (mã đơn, giá trị, trạng thái).

# Viết chương trình Python để thực hiện các chức năng sau:
#   1.  Thêm đơn hàng mới vào danh sách.
#   2.  Hiển thị danh sách đơn hàng theo thứ tự nhập.
#   3.  Tính tổng doanh thu từ các đơn hàng đã giao.
#   4.  Tìm đơn hàng có giá trị cao nhất.
#   5.  Lọc ra danh sách các đơn hàng chưa giao.

# Yêu cầu:
#   •  Viết các hàm thực hiện từng chức năng trên.
#   •  Cho phép nhập dữ liệu từ người dùng để thêm đơn hàng.
#   •  Hiển thị kết quả rõ ràng.

# orders = [
#     ("DH001", 500, True),
#     ("DH002", 1200, False),
#     ("DH003", 750, True),
#     ("DH004", 300, False),
#     ("DH005", 1000, True),
# ]

if __name__ == "__main__":
    quanlydonhang()


   
# Đề bài:
# Một cửa hàng bán đồ điện tử, nơi có các loại sản phẩm như điện thoại, máy tính xách tay và tai nghe. Mỗi sản phẩm có thông tin như tên sản phẩm, loại sản phẩm, số lượng trong kho và giá bán. Bạn cần xây dựng một chương trình quản lý kho hàng cho cửa hàng này.

# Yêu cầu:

# Nhập thông tin sản phẩm:
# Nhập danh sách các sản phẩm, mỗi sản phẩm có các thông tin: tên sản phẩm, loại sản phẩm (điện thoại, máy tính xách tay, tai nghe), số lượng trong kho, và giá bán.
# Xử lý thông tin:
# Tính tổng giá trị của kho hàng (tổng giá trị = số lượng * giá bán cho mỗi sản phẩm).
# Tính tổng số lượng các sản phẩm trong kho.
# Tìm sản phẩm có giá trị cao nhất trong kho hàng.
# Tìm kiếm sản phẩm:
# Nhập tên sản phẩm và kiểm tra xem sản phẩm đó có trong kho không. Nếu có, in ra thông tin chi tiết về sản phẩm, nếu không thì thông báo sản phẩm không có trong kho.
# Cập nhật số lượng sản phẩm:
# Nhập tên sản phẩm và số lượng cần thêm vào kho. Cập nhật số lượng của sản phẩm đó trong kho.
# Xuất thông tin:
# In ra thông tin tất cả các sản phẩm trong kho hàng (tên sản phẩm, loại, số lượng, giá bán).
# In ra tổng số lượng và tổng giá trị của kho hàng.


products = [
    {"name": "iPhone 14", "category": "Điện thoại", "quantity": 50, "price": 20000000},
    {"name": "Dell XPS 13", "category": "Máy tính xách tay", "quantity": 30, "price": 25000000},
    {"name": "AirPods Pro 2", "category": "Tai nghe", "quantity": 100, "price": 5000000},
    {"name": "Samsung Galaxy S23", "category": "Điện thoại", "quantity": 40, "price": 18000000},
    {"name": "MacBook Air M2", "category": "Máy tính xách tay", "quantity": 20, "price": 28000000}
]