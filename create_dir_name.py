import os

def dir_save():
    path_onedrive = os.path.expanduser('~/OneDrive')
    path_dir_save = None
    if os.path.exists(path_onedrive):
        user = os.getenv('USERNAME')
        path_dir_save = f'C:\\Users\\{user}\\OneDrive\\Imagens\\screenshot-app\\'

    else:
        path_dir_save = f'C:\\Users\\{user}\\Imagens\\screenshot-app\\'

    if not os.path.exists(path_dir_save):
        print("criando diretorio : screenshot-app ")
        os.makedirs(path_dir_save)
    else:
        print("diretorio screenshot-app já existe")
    return path_dir_save