import random

class mocky: # patient zero
    username = "Denis Kharitonov"
    email = "denis_kharitonov_10_000@gmail.com"
    password = "password000"

class rand_mocky:
    number = random.randint(1,999)  # 000 заререзвировано для mocky
    username = f"RandyRandom{number:03d}"
    email = f"denis_kharitonov_10_{number:03d}@gmail.com"
    password = f"password{number:03d}"
    incorrect_password = f"{number:03d}"
