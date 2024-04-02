from faker import Faker
from model.users.tt_nguoi_dung import tt_nguoi_dung

def generate_users(num_users) -> list: 
    fake_data_engine = Faker()
    users = []
    for i in range(1, num_users): 
        user = tt_nguoi_dung(fake_data_engine.first_name(), fake_data_engine.last_name(), fake_data_engine.email())
        user.cccd = user.random_cid()
        user.ngay_sinh = user.random_dob()
        user.gioi_tinh = user.random_gender()
        user.so_dt = user.random_phonenum()
        user.dia_chi = user.random_address()
        
        for item in users: 
            if(user.cccd == item.cccd):
                user.cccd = user.random_cid()
            else:
                users.append(user)

    return users
