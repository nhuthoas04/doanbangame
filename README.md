# csn-da22tta-nguyennhuthoa-gamepad_web-django

# Cách chạy chương trình


1 Cài đặt môi trường

Yêu cầu Python >=3.8.


2 Clone repository về máy


git clone https://github.com/nhuthoas04  
cd csn-da22tta-nguyyennhuthoa 


3 Cài đặt các thư viện cần thiết

Chạy lệnh sau trong terminal:

pip install -r requirements.txt  

Mở tệp settings.py của dự án Django và sửa phần DATABASES:


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'ten_csdl',  # Tên cơ sở dữ liệu

        'USER': 'ten_user',  # Tên user MySQL

        'PASSWORD': 'mat_khau',  # Mật khẩu của user

        'HOST': 'localhost',  # Máy chủ (local)

        'PORT': '3306',  # Cổng mặc định của MySQL

    }

}


4 Tạo tài khoản quản trị (superuser)

Chạy lệnh:


python manage.py createsuperuser  
Sau đó nhập tên đăng nhập, email và mật khẩu của bạn.


5 Thực hiện di chuyển dữ liệu (migrate)

Chạy lệnh:


python manage.py migrate


6 Khởi động server

Chạy lệnh:


python manage.py runserver  


7 Truy cập ứng dụng

Ứng dụng chính: Truy cập http://localhost:8000/
Module quản trị: Truy cập http://localhost:8000/admin và đăng nhập bằng tài khoản quản trị vừa tạo.



#  Liên hệ

 Nguyễn Nhựt Hóa

 Email: nhuthoas04@gmail.com
  
 Số diện thoại: 0912534571

 Trường Đại học Trà Vinh


