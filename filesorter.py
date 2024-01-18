import os, shutil

path = r"C:\Users\lhmpev7\PycharmProjects\PBL"
all_files = os.listdir(path)

for i in all_files:
    extension = i.split('.')
    if os.path.isfile(path+f"/{extension}"):
        shutil.move(path+f'/{i}', path+f"/{extension}/{i}")
    else:
        with open(path+f"/{extension}", "a") as file:
            shutil.move(path+f'/{i}', path+f"/{extension}/{i}")