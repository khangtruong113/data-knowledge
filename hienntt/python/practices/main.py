# # Cùng thư mục
# import math_plus
# print(math_plus.get_sum(4,7))
# # Kết quả: 11



# # Khác thư mục
import os, sys
# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
lib_path = os.path.abspath(os.path.join('modules'))
# thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)
# import
import math_minus
print(math_minus.get_diff(4,7))
# Kết quả: -3