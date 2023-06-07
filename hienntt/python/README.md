# Python

## 1. Types and Operators
### 1.1. Data types
- Numeric: int, float, complex
- String: str
- Sequence: list, tuple, range
- Binary: bytes, bytearray, memoryview
- Mapping: dict
- Boolean: bool
- Set: set, frozenset

| Type       | Đặc trưng                    | Mutable                                                                                  | Ordered                                                                     | Indexing/Slicing | Duplicate Elements |
|:-----------|:-----------------------------|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|:-----------------|:-------------------|
| list       | Chứa bất kì kiểu dữ liệu nào | x                                                                                        | x                                                                           | x                | x                  |
| tuple      | Giá trị không thể thay đổi   |                                                                                          | x                                                                           | x                | x                  |
| set        | Giá trị là duy nhất          | (Set items are unchangeable, but you can remove and/or add items whenever you like)      |                                                                             |                  |                    |
| dictionary | Key: Value                   | x                                                                                        | x (since Python 3.7. In Python 3.6 and earlier, dictionaries are unordered) | x                |                    |

### 1.2. Operators
- Arithmetic operators
- Assignment operators 
- Comparison operators 
- Logical operators 
- Identity operators 
- Membership operators 
- Bitwise operators

**Arithmetic operators** (toán tử số học)

| Operator | Name           | Example | Note                |
|:---------|:---------------|:--------|:--------------------|
| +        | Addition       | x + y   |                     |
| -        | Subtraction    | x - y   |                     |
| *        | Multiplication | x * y   |                     |
| /        | Division       | x / y   |                     |
| %        | Modulus        | x % y   |                     |
| **       | Exponentiation | x ** y  |                     |
| //       | Floor division | x // y  | chia làm tròn xuống |

**Assignment operators** (toán tử gán)

| Operator | Example | Same as    | Note |
|:---------|:--------|:-----------|:-----|
| =        | x = 5   | x = 5      |      |
| +=       | x += 3  | x = x + 3  |      |
| -=       | x -= 3  | x = x - 3  |      |
| *=       | x *= 3  | x = x * 3  |      |
| /=       | x /= 3  | x = x / 3  |      |
| %=       | x %= 3  | x = x % 3  |      |
| //=      | x //= 3 | x = x // 3 |      |
| **=      | x **= 3 | x = x ** 3 |      |

**Comparison operators** (toán tử so sánh)

| Operator | Description              | Example | Note |
|:---------|:-------------------------|:--------|:-----|
| ==       | Equal                    | x == y  |      |
| !=       | Not equal                | x != y  |      |
| >        | Greater than             | x > y   |      |
| <        | Less than                | x < y   |      |
| >=       | Greater than or equal to | x >= y  |      |
| <=       | Less than or equal to    | x <= y  |      |

**Logical operators** (toán tử logic)

| Operator | Description                                             | Example               | Note |
|:---------|:--------------------------------------------------------|:----------------------|:-----|
| and      | Returns True if both statements are true                | x < 5 and x < 10      |      |
| or       | Returns True if one of the statements is true           | x < 5 or x < 4        |      |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |      |


**Identity operators** (toán tử xác thực)

| Operator | Description                                            | Example    | Note |
|:---------|:-------------------------------------------------------|:-----------|:-----|
| is       | Returns True if both variables are the same object     | x is y     |      |
| is not   | Returns True if both variables are not the same object | x is not y |      |

**Membership operators** (toán tử khai thác)

| Operator | Description                                                                      | Example    | Note |
|:---------|:---------------------------------------------------------------------------------|:-----------|:-----|
| in       | Returns True if a sequence with the specified value is present in the object     | x in y     |      |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |      |


**Bitwise operators** (toán tử bitwise) - ít sử dụng

| Operator | Name                 | Description                                                                                               | Example| Note |
|:---------|:---------------------|:----------------------------------------------------------------------------------------------------------|:-------|:-----|
| &        | AND                  | Sets each bit to 1 if both bits are 1                                                                     | x & y  |      |
| \|       | OR                   | Sets each bit to 1 if one of two bits is 1                                                                | x \| y |      |
| ^        | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                           | x ^ y  |      |
| ~        | NOT                  | Inverts all the bits                                                                                      | ~x     |      |
| <<       | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                          | x << 2 |      |
| >>       | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off   | x >> 2 |      |

## 2. Basic Statements and Syntax

| Statement                   | Description                            |
|:----------------------------|:---------------------------------------|
| ```print()```               | hiển thị output                        |
| ```input()```               | cho phép nhập vào input                |
| ```type()```                | kiểm tra data type                     |
| ```int()```                 | chuyển sang dạng integer               |
| ```float()```               | chuyển sang dạng float                 |
| ```str()```                 | chuyển sang dạng string                |
| ```len()```                 | đếm độ dài chuỗi                       |
| ```upper()```               | chữ viết hoa                           |
| ```lower()```               | chữ viết thường                        |
| ```strip()```               | xóa khoảng trắng ở đầu hoặc cuối       |
| ```split()```               | chia cắt chuỗi dựa trên ký tự khai báo |
| ```format()``` and ```{}``` | giúp combine strings và numbers        |
| ```list()```                | tạo một list mới                       |
| ```tuple()```               | tạo một tuple mới                      |
| ```set()```                 | tạo một set mới                        |
| ```dict()```                | tạo một dictionary mới                 |

Xem thêm: [String Methods](https://www.w3schools.com/python/python_strings_methods.asp), [List Methods](https://www.w3schools.com/python/python_lists_methods.asp),
[Tuple Methods](https://www.w3schools.com/python/python_tuples_methods.asp), [Set Methods](https://www.w3schools.com/python/python_sets_methods.asp),
[Dictionary Methods](https://www.w3schools.com/python/python_dictionaries_methods.asp)

## 3. Flow Control
Control flow của Python được điều chỉnh bởi các câu lệnh điều kiện, vòng lặp và lệnh gọi hàm.

Python có ba loại control structures: 
- Sequential - chế độ mặc định 
- Selection - được sử dụng cho các decisions và branching
- Repetition - được sử dụng cho looping, tức là lặp lại một đoạn mã nhiều lần

### 3.1. Sequential
Sequential statements là một tập hợp các câu lệnh mà quá trình thực hiện của chúng diễn ra theo một trình tự. Vấn đề với các sequential statements là nếu logic bị hỏng ở bất kỳ dòng nào, thì việc thực thi source code hoàn chỉnh sẽ bị hỏng.
```python
## This is a Sequential statement
     
a=20
b=10
c=a-b
print("Subtraction is : ",c)
```

### 3.2. Selection
Selection statement cho phép kiểm tra một số điều kiện và thực hiện các lệnh dựa trên điều kiện nào là đúng. Một vài Decision Control Statements như: Simple if, if-else, nested if, if-elif-else.

Simple if:
```python
n = 10
if n % 2 == 0:
    print("n is an even number")
```

if-else:
```python
n = 5
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
```

nested if: 
```python
    a = 5
    b = 10
    c = 15
if a > b:
    if a > c:
        print("a value is big")
    else:
        print("c value is big")
elif b > c:
    print("b value is big")
else:
    print("c is big")
```

if-elif-else:
```python
x = 15
y = 12
if x == y:
    print("Both are Equal")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")
```

### 3.3. Repetition
Repetition statement được sử dụng để lặp lại một group (block) lệnh lập trình. Trong Python thường có 2 loại loop statements: for loop, while loop.

For loop:
```python
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    print(lst[i], end = " ")
     
for j in range(0,10):
    print(j, end = " ")
```

While loop:
```python
m = 5
i = 0
while i < m:
    print(i, end = " ")
    i = i + 1
print("End")
```
## 4. Functions and Generators
### 4.1. Functions

**Function** (hay còn gọi là **Hàm**): Là một khối lệnh được đóng gói lại thành một đơn vị độc lập, dùng để thực hiện một tác vụ trong chương trình.

Hàm giúp phân chia chương trình tốt hơn, và cho phép tái sử dụng lại source code.

Python cung cấp nhiều các hàm dựng sẵn (**built-in function**), ngoài ra ta có thể tự định nghĩa các hàm của riêng mình. 
Những hàm này còn được gọi là **user-defined function**.
- Hàm sau khi được định nghĩa sẽ không tự thực thi. 
- Hàm chỉ thực thi khi được gọi đến.

![Built-in function](https://cdn.mcivietnam.com/nhanvien/media/post/uploads/2021/07/ham-trong-python.png)

Function Syntax:
```python
def function_name ( arg1, arg2, ...) : 
    ...... 
    # function body 
    ......
```

Ví dụ gọi hàm:
```python
def say_hello():
    print("Hello World")
```

**Lambda**: Hàm lambda là một hàm ẩn danh. Hàm lambda có thể nhận bất kỳ số lượng đối số nào, nhưng chỉ có thể có một biểu thức.

Lambda Syntax: 
```python    
lambda arguments : expression
```

Ví dụ:
```python 
x = lambda a, b : a * b
print(x(5, 6))
```

### 4.2. Generators
**Iterable**: có nhiều phần tử và cho phép lặp qua
```python 
def list_n_list(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
        return nums
    
sum(list_n_list(1000000000))
```

**Iterator**: iterator là đối tượng có phương thức \_\_next__, và phương thức này sẽ trả về phần tử tiếp theo của đối tượng, nếu đối tượng không còn phần tử nào để lặp qua thì nó sẽ báo lỗi StopIteration.
```python 
class list_n_iterator(object):
    def __init__(self, n):
        # giới hạn là n
        self.n = n
        # bắt đầu từ 0
        self.next = 0
    
    def __iter__(self):
        # list_n vừa là iterable, vừa là iterator
        # vì nó có phương thức __iter__ và __next__
        return self
    
    def __next__(self):
        if self.next < self.n:
            # gán giá trị hiện tại của next
            current = self.next
            # tăng 1 cho next
            self.next = current + 1
            return current
        raise StopIteration

sum(list_n_iterator(100000000))
```

**Generators**: cho phép tạo ra một hàm hoạt động tương tự như một iterator, tức là nó cũng là iterable, và có thể dùng với vòng lặp for.
```python
def list_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum(list_n_generator(1000000000))
```

Chi tiết tham khảo [tại đây](https://viblo.asia/p/iterable-iterator-va-generator-trong-python-E375zrd65GW).

## 5. Modules and Packages
### 5.1. Modules
Modules là cách mà chúng ta phân hóa chương trình ra các nhánh nhỏ cho dễ quản lý và gọi lại chúng khi nào cần, như thế chương trình của chúng ta sẽ có tính tái sử dụng, bảo trì cao.

#### 5.1.1. Sử dụng modules
Danh sách các module mặc định của Python: [Link](https://docs.python.org/3/py-modindex.html)

**Import**: import một module có vào trong file hiện tại
```python
import module1, module2,...
```
```python
import math
a = 3.2
# làm tròn lên 1 số
print(math.ceil(a)) # 4
# làm tròn xuống 1 số
print(math.floor(a)) # 3
```

**From - import**: không muốn sử dụng hết toàn bộ module mà chỉ muốn sử dụng một số thứ trong đó
```python
from modules import something, something2,...
```
```python
from math import ceil, floor
a = 3.2

print(ceil(a)) 
# kết quả: 4

print(floor(a))
# Kết quả: 3
```

**As**: định danh cho modules
```python
import modules as newname
# hoặc đối với from import
from modules import something as newname
```
```python
import mathplus as ma

print(ma.get_sum(4,7))
# Kết quả: 11
```

## 5.1.2. Build module

**Cùng cấp thư mục:**

Tạo 2 file ```main.py``` và ```math_plus.py``` ở cùng cấp thư mục.

Trong file ```math_plus.py```:
```python
def get_sum (a, b):
    return a + b
```
Trong file ```main.py```:
```python
import math_plus

print(math_plus.get_sum(4,7))
# Kết quả: 11
```
_Chú ý:_ 
- Tên file chứa code chúng ta muốn import chính là tên modules.
- Đối với trường hợp các bạn sử dụng from ... import * thì mặc định python nó sẽ không import được các đối tượng có tên được bắt đầu bằng ký tự _ . Trong trường hợp này, nếu như bạn muốn import được các đối tượng đó thì bạn sẽ phải chỉ đích danh các đối tượng đó.

**Import module khác thư mục:**



