# venv - sanal çalışma ortamı nedir?
# farklı python projeleri için, proje dosyaları ve projede kullanılan paketler için oluşturulan izole çalışma ortamlarıdır.
# global kullandığımız paket sayısını artırmak yerine her bir proje için paketler kurmak gibi düşünebiliriz.


# pip3 install virtualenv
# virtaulenv 05.venv
# 05.venv\Scripts\activate      -> windows
# source 05.venv/bin/activate   -> linux

# deactivate


# projedeki aktif modül listesini yazdırmak
# pip3 freeze --local > requirements.txt


# sanal çalışma ortamını spesifik bir python versiyonunda çalıştırmak:
# virtualenv testvenv --python="path.../python3.exe"


# bir projedeki paketleri diğerine yüklemek için:
# pip3 install -r requirements.txt


# dosya yapısı
# vproject1 -> venv
# project1  -> scriptlerimizin olduğu yer