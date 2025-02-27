# Nhập ba số thực dương a, b, c.
# 	1.	Kiểm tra xem a, b, c có thể là độ dài ba cạnh của một tam giác hay không. (Điều kiện tam giác: a + b > c, a + c > b, và b + c > a).
# 	2.	Nếu có thể tạo thành một tam giác, hãy xác định loại tam giác đó:
# 	•	Tam giác đều (các cạnh bằng nhau)
# 	•	Tam giác vuông (thỏa mãn định lý Pythagore: a^2 + b^2 = c^2 hoặc hoán vị các cạnh)
# 	•	Tam giác vuông cân (vừa vuông vừa có hai cạnh bằng nhau)
# 	•	Tam giác cân (có ít nhất hai cạnh bằng nhau nhưng không phải tam giác đều)
# 	•	Tam giác thường (không thuộc các loại trên)

# Yêu cầu in ra kết luận tương ứng với dữ liệu đầu vào.


# Đề bài:
# Viết chương trình cho phép người dùng nhập vào một tháng và một năm (cả hai đều là số nguyên). Hãy xác định và in ra số ngày của tháng đó trong năm tương ứng.

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

# Yêu cầu chi tiết:
# 	1.	Nhập một số nguyên a \ge 1.
# 	2.	Xuất ra kết quả lần lượt:

# a \times 1 = \dots


# a \times 2 = \dots


# \dots


# a \times 10 = \dots



from os import name


if __name__ == "__main__":
    print("Chương trình in ra bảng cửu chương của số a")