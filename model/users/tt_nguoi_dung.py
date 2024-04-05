import random
from datetime import datetime, timedelta

class tt_nguoi_dung:
    cccd = ""
    ho_lot = ""
    ten = ""
    ngay_sinh = datetime(1900, 1, 1)
    gioi_tinh = 1
    so_dt = ""
    email = ""
    dia_chi = ""

    def __init__(self, ho_lot, ten, email) -> None:
        self.ho_lot = ho_lot
        self.ten = ten
        self.email = email

    def random_cid(self) -> str:
        random_data = str(random.randint(10000000000, 99999999999))

        return str(f'0{random_data}')

    def random_dob(self) -> datetime:
        birth_year = random.randint(1954, 1998)
        birth_date = datetime(birth_year, 1, 1) + timedelta(days=random.randint(0, 365))

        return birth_date

    def random_phonenum(self) -> str:
        random_data = random.randint(100000000, 999999999)
        randomed_phonenum = str(f"0{random_data}")

        return randomed_phonenum

    def random_gender(self) -> int:
        genders = [ 0, 1 ]

        return random.choice(genders)

    def random_address(self) -> str:
        locations = ["TP. Hồ Chí Minh", "Hà Nội", "Hải Phòng", "Đà Nẵng", "Cần Thơ"]
        selection = random.choice(locations)

        return str(selection)

    def export_insert_clause(self) -> str:
        formatedDateTime = self.ngay_sinh.strftime("%Y-%b-%d %H:%M:%S")

        return str(
            f"""INSERT INTO tt_nguoi_dung VALUES ('{self.cccd}', '{self.ho_lot}', '{self.ten}', TO_TIMESTAMP(\'{formatedDateTime}\', \'YYYY-MON-DD HH24:MI:SS\'), '{self.gioi_tinh}', '{self.so_dt}', '{self.email}', '{self.dia_chi}');"""
        )
