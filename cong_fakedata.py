from faker import Faker
import random
from datetime import datetime, timedelta

NUM_USER = 1000
fake_data_engine = Faker()

def generate_fake_users():
    users = []
    # Lấy số điện thoại 10 hoặc 12 số
    num_digits = random.choice([10, 12])  # Chọn ngẫu nhiên số lượng chữ số (10 hoặc 12)
    if num_digits == 10:
        phone_number = "0"  # Bắt đầu chuỗi số điện thoại với số 0
    else:
        phone_number = "84"

    for _ in range(NUM_USER):
        # Căn cước công dân
        cccd = "0"

        for _ in range(11):  # Tạo 11 chữ số ngẫu nhiên
            digit = random.randint(0, 9)
            cccd += str(digit)
        # Họ lót
        surname = fake_data_engine.last_name()
        # Tên
        name = fake_data_engine.first_name()
        # Ngày sinh
        birth_year = random.randint(1800, 2010)
        birth_date = datetime(birth_year, 1, 1) + timedelta(days=random.randint(0, 365))
        # Giới tính
        prefixes = ["Nam", "Nữ"]
        prefix = random.choice(prefixes)
        sex = f"{prefix}"
        # Số điện thoại
        digit = random.randint(0, 9)  # Tạo một chữ số ngẫu nhiên từ 0 đến 9
        phone_number += str(digit)
        # Email
        email = fake_data_engine.email()
        # Địa chỉ
        prefixes = ["Hồ Chí minh", "Hà Nội", "Hải Phòng", "Đà Nẵng", "Cần Thơ"]
        prefix = random.choice(prefixes)
        address = f"{prefix}"

        user = {
            "cccd": cccd,
            "surname": surname,
            "name": name,
            "birthYear": birth_date.strftime("%Y-%m-%d"),
            "sex": sex,
            "phone": phone_number,
            "email": email,
            "address": address,
        }
        users.append(user)

    return users


num_users = 100  # Số lượng người dùng giả mạo cần tạo
fake_users = generate_fake_users(num_users)

for user in fake_users:
    # Bảng tt_nguoi_dung
    print(
        f"""INSERT INTO tt_nguoi_dung VALUES ({user['cccd']},'{user['surname']}','{user['name']}',{user['birthYear']},'{user['sex']}','{user['phone']}','{user['email']}','{user['address']}');"""
    )
