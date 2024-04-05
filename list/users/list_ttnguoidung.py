from faker import Faker
from model.users.tt_nguoi_dung import tt_nguoi_dung

def is_exists(cid, users) -> bool:
    listSize = len(users)
    for i in range(0, listSize):
        if(users[i].cccd == cid):
            return True
    
    return False

def generate_users(num_users) -> list: 
    fake_data_engine = Faker('vi')
    users = []
    for i in range(1, num_users): 
        user = tt_nguoi_dung(fake_data_engine.first_name(), fake_data_engine.last_name(), fake_data_engine.email())
        user.cccd = user.random_cid()
        user.ngay_sinh = user.random_dob()
        user.gioi_tinh = user.random_gender()
        user.so_dt = user.random_phonenum()
        user.dia_chi = user.random_address()
        
        while(is_exists(user.cccd, users)): 
            user.cccd = user.random_cid()

        users.append(user)

    return users
