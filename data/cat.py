# Import dataset từ kagglehub:
# Vào kaggle chọn dataset cần import 
# --> chọn download sẽ hiện ra popup có đoạn code phía dưới này để import dataset

import kagglehub
path = kagglehub.dataset_download("joannanplkrk/its-raining-cats")
print("Path to dataset files:", path)

# Thêm các thư viện cần sử dụng
import kagglehub
path = kagglehub.dataset_download("joannanplkrk/its-raining-cats")
print("Path to dataset files:", path)

# Xem trong dataset vừa import có những nội dung gì

import os
path = "/home/gitpod/.cache/kagglehub/datasets/joannanplkrk/its-raining-cats/versions/8"
# path này hiện ở terminal lúc chạy xong phần import dataset từ kaggle
all_files = os.listdir(path) # method os.listdir(path) dùng để lấy danh sách các file có trong path 
print("Các tệp và thư mục trong:", path)
for item in all_files:
    print(item)

cat_breed = pd.read_csv("/home/gitpod/.cache/kagglehub/datasets/joannanplkrk/its-raining-cats/versions/8/cat_breeds_clean.csv")
cat_breed.head()

# Nhập dòng lệnh này trong new terminal để mở jupyterlab
# jupyter lab --ServerApp.allow_origin_regex='.*gitpod.io$' --ServerApp.allow_remote_access=True --ServerApp.allow_hosts='*'
