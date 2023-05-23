# Datatypes

*Kiểm tra kiểu dữ liệu của biến*: type(var)

*Ép kiểu dữ liệu*: int(var), float(var), complex(var)

## Numeric:

- Integer (int): không giới hạn về độ dài

- Float (float): số thực vói dấu chấm động, độ chính xác *15 chữ số thập phân*

*Mong muốn hiển thị n chữ số sau dấu phẩy*:

    import decimal
    decimal.getcontext().prec= n

- Complex (complex): số phức x+jy

## Boolean

True(1)/False(0)

## String (str)

|Ký hiệu|Ý nghĩa|
|---|-----------|
|\n|Xuống dòng|
|\t|Tab|
|\b|Bỏ khoảng trắng đằng trước|

Exp:

```name=[Tran van A]```

//name[0]='T'

//name[-1]=A

---character---

## List

- Cho phép lưu trữ nhiều kiểu dữ liệu khác nhau, truy xuất đến các phần tử thông qua vị trí của phần tử đó

Exp:

```name=['Tran van a', 'Nguyen thi B']```

//name[0]='Tran van a'

//name[1]='Nguyen thi B'

- Sửa các phần từ trong list

```name[1]='Nguyen thi C'```

//name=['Tran van a','Nguyen thi C']

- Xóa các phần từ trong list

```del name[1]```

//name=['Tran van a']

- List lồng nhau

Exp:

    DOB=[26,03,1998]
    Info=['TTH',DOB]

Khi đó:

    DateOfBirth=Info[1]
    Date=DateOfBirth[0]

//Date=26

hoặc

```Date=Info[1][0]```

## Tuple

Exp:
```day=('M','T','W','Th','F','Sa','Su')```

Thao tác tương tự như list

## Dictionary

Chứa các cặp key-value

- Các phần tử đều phải có key

- Key chỉ có thể là số hoặc chuỗi

- Key phải là duy nhất (nếu không nó sẽ nhận giá trị của phần tử có key được xuất hiện cuối cùng)

- Key khi đã được khai báo thì không thể đổi được tên

- Key có phân biệt hoa thường

Exp:

    person = {
     'name': 'Vũ Thanh Tài',
     'age': 22,
     'male': True,
     'status': 'single'        
     }

- Truy cập phần tử của Dictionary

```person[''name'']```

//Vũ Thanh Tài

# Operation

## Toán tử số học

|Toán tử|Ý nghĩa|
|---|---------|
|+|Cộng|
|-|Trừ|
|*|Nhân|
|/|Chia, kết quả luôn là số thực|
|%|Trả về phần dư|
|//|Trả về phần nguyên|
|**|Lũy thừa|

## Toán tử so sánh

|Toán tử|Ý nghĩa|
|---|---------|
|>|Bên trái lớn hơn trả về true|
|<|Bên trái nhỏ hơn trả về true|
|==|Hai bên bằng nhau trả về true|
|!=|Hai bên khác nhau trả về true|
|>=|Bên trái lớn hơn hoặc bằng trả về true|
|<=|Bên trái nhỏ hơn hoặc bằng trả về true|

## Toán tử logic

|Toán tử|Ý nghĩa|
|---|---------|
|and|Cả hai đều true, trả về true|
|or|Ít nhất một toán hạng true, trả về true|
|not|Toán hạng false, trả về true và ngược lại|


## Toán tử khác

|Toán tử|Ý nghĩa|
|---|---------|
|is|Trả về True nếu các toán hạng có giá trị được lưu trong cùng một vùng nhớ (tham chiếu đến cùng một object)|
|isnot|Trả về True nếu các toán hạng có giá trị không được lưu trong cùng một vùng nhớ (không tham chiếu đến cùng một object)|

# Statement & Syntax

 + If-else

    if condition: 
      #command
    else:
      #command

 + If-elif-else
   
    if condition:
       # command
    elif condition2:
       # command
    elif condition3:
       # command
    else:
       # command

Exp:

    a = 9
    if (a >= 4 and a <= 10):
        print('Qua mon')
    elif (a >= 0 and a <4):
        print('Hoc lai')
    else:
        print('Diem khong hop le')

 + For - in
    for variable in data:
        #command```
 
 For example:
    for letter in "Python" :
      Print 'Current Letter: ', letter

+ While   
    while condition:
      # command```

> break chấm dứt vòng lặp tại thời điểm nó xuất hiện, các code cùng cấp phía sau nó sẽ không được thực thi nữa.

> continue: nhảy qua lần lặp hiện tại và chuyển đến lần lặp tiếp theo, các code cùng cấp phía sau nó cũng sẽ không được thực hiện.

# Hàm

## Khai báo hàm

    def ten_ham(param...):
       #commands

Trong đó:

- ten_ham: tên của hàm mà bạn muốn đặt. Lưu ý: **Tên hàm không được bắt đầu bằng số** và **không được chứa các ký tự đặc biệt** (trừ ký tự _)

- param...: các tham số bạn muốn truyền vào hàm, nếu không có tham số thì để trống.

Exp:

//hàm tính tổng hai số a,b

    def sum(a, b):
        print("sum = " + str(a + b))

## Gọi hàm

ten_ham() hoặc ten_ham(param...)

Exp:

sum(2,3)
//Gọi hàm sum vừa viết, kết quả hiển thị 5

## Phạm vi của biến trong hàm

- Một biến được khai báo ở trong hàm thì nó chỉ có thể được sử dụng ở trong hàm đó, không thể thay đổi giá trị của biến đã khai báo trong hàm mà tác động ra ngoài hàm (đối với các biến bình thường)

*Với biến có kiểu dữ liệu là list thì có thể tác động tới biến ở ngoài hàm

**Biến global**: có thể gọi là tác động tới nó từ bất kỳ đâu trong chương trình

Khai báo biến global:

```global [ten bien]```

## Truyền vô số tham số vào hàm

Khi chưa biết được chính xác số lượng biến truyền vào trong hàm, ta khai báo một param đại diện cho các biến truyền vào hàm bằng cách thêm * vào trước param

Exp: hàm tính tổng dãy số truyền vào 
    def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp

    result = get_sum(1, 2, 3, 4, 5)

    print(result)

    //kết quả tổng của dãy số trên là 15

# Module trong Python

- Modules là cách phân hóa chương trình ra các nhánh nhỏ cho dễ quản lý và gọi lại chúng khi nào cần

**Import**

- Để import một module sẵn có vào file hiện tại 

```import [ten module]```

- Khi không muốn import toàn bộ module mà chỉ import một số thứ

```from [ten module] import [các thứ muốn import]```

**Định danh module**

- Trường hợp modules của chúng ta rất khó nhớ hay dài hay vì một lý do nào khác mà bạn không muốn gọi module như thế

    import [tên module] as [ten module theo cách mà bạn muốn gọi]

hoặc đối với from import

    from [tên module] import something as [ten module theo cách mà bạn muốn gọi]

> from .... import *: 

mặc định python nó sẽ không import được các đối tượng có tên được bắt đầu bằng ký tự

> import module nằm trong thư mục khác: Mặc định thì python nó sẽ chỉ load các module hệ thống của nó và các module ở cùng cấp với file hiện tại

     import os, sys
    // lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
     lib_path = os.path.abspath(os.path.join('modules'))
    // thêm thư mục cần load vào trong hệ thống
     sys.path.append(lib_path)
    // import
     from mathplus import get_sum

     print(get_sum(1,4));
// kết quả: 5


# Package

- Package: một thư mục chứa một hoặc nhiều modules hay các package khác nhau, nhằm mục đích phân bố các modules có cùng chức năng hay một cái gì đó, để dễ quản lý source code

## Buil package

Tạo thư mục với tên thư mục chính là tên package, trong thư mục có fu
# Datatypes

*Kiểm tra kiểu dữ liệu của biến*: type(var)

*Ép kiểu dữ liệu*: int(var), float(var), complex(var)

## Numeric:

- Integer (int): không giới hạn về độ dài

- Float (float): số thực vói dấu chấm động, độ chính xác *15 chữ số thập phân*

*Mong muốn hiển thị n chữ số sau dấu phẩy*:

    import decimal
    decimal.getcontext().prec= n

- Complex (complex): số phức x+jy

## Boolean

True(1)/False(0)

## String (str)

|Ký hiệu|Ý nghĩa|
|---|-----------|
|\n|Xuống dòng|
|\t|Tab|
|\b|Bỏ khoảng trắng đằng trước|

Exp:

```name=[Tran van A]```

//name[0]='T'

//name[-1]=A

---character---

## List

- Cho phép lưu trữ nhiều kiểu dữ liệu khác nhau, truy xuất đến các phần tử thông qua vị trí của phần tử đó

Exp:

```name=['Tran van a', 'Nguyen thi B']```

//name[0]='Tran van a'

//name[1]='Nguyen thi B'

- Sửa các phần từ trong list

```name[1]='Nguyen thi C'```

//name=['Tran van a','Nguyen thi C']

- Xóa các phần từ trong list

```del name[1]```

//name=['Tran van a']

- List lồng nhau

Exp:

    DOB=[26,03,1998]
    Info=['TTH',DOB]

Khi đó:

    DateOfBirth=Info[1]
    Date=DateOfBirth[0]

//Date=26

hoặc

```Date=Info[1][0]```

## Tuple

Exp:
```day=('M','T','W','Th','F','Sa','Su')```

Thao tác tương tự như list

## Dictionary

Chứa các cặp key-value

- Các phần tử đều phải có key

- Key chỉ có thể là số hoặc chuỗi

- Key phải là duy nhất (nếu không nó sẽ nhận giá trị của phần tử có key được xuất hiện cuối cùng)

- Key khi đã được khai báo thì không thể đổi được tên

- Key có phân biệt hoa thường

Exp:

    person = {
     'name': 'Vũ Thanh Tài',
     'age': 22,
     'male': True,
     'status': 'single'        
     }

- Truy cập phần tử của Dictionary

```person[''name'']```

//Vũ Thanh Tài

# Operation

## Toán tử số học

|Toán tử|Ý nghĩa|
|---|---------|
|+|Cộng|
|-|Trừ|
|*|Nhân|
|/|Chia, kết quả luôn là số thực|
|%|Trả về phần dư|
|//|Trả về phần nguyên|
|**|Lũy thừa|

## Toán tử so sánh

|Toán tử|Ý nghĩa|
|---|---------|
|>|Bên trái lớn hơn trả về true|
|<|Bên trái nhỏ hơn trả về true|
|==|Hai bên bằng nhau trả về true|
|!=|Hai bên khác nhau trả về true|
|>=|Bên trái lớn hơn hoặc bằng trả về true|
|<=|Bên trái nhỏ hơn hoặc bằng trả về true|

## Toán tử logic

|Toán tử|Ý nghĩa|
|---|---------|
|and|Cả hai đều true, trả về true|
|or|Ít nhất một toán hạng true, trả về true|
|not|Toán hạng false, trả về true và ngược lại|


## Toán tử khác

|Toán tử|Ý nghĩa|
|---|---------|
|is|Trả về True nếu các toán hạng có giá trị được lưu trong cùng một vùng nhớ (tham chiếu đến cùng một object)|
|isnot|Trả về True nếu các toán hạng có giá trị không được lưu trong cùng một vùng nhớ (không tham chiếu đến cùng một object)|

# Statement & Syntax

 + If-else

    if condition: 
      #command
    else:
      #command

 + If-elif-else
   
    if condition:
       # command
    elif condition2:
       # command
    elif condition3:
       # command
    else:
       # command

Exp:

    a = 9
    if (a >= 4 and a <= 10):
        print('Qua mon')
    elif (a >= 0 and a <4):
        print('Hoc lai')
    else:
        print('Diem khong hop le')

 + For - in
    for variable in data:
        #command```
 
 For example:
    for letter in "Python" :
      Print 'Current Letter: ', letter

+ While   
    while condition:
      # command```

> break chấm dứt vòng lặp tại thời điểm nó xuất hiện, các code cùng cấp phía sau nó sẽ không được thực thi nữa.

> continue: nhảy qua lần lặp hiện tại và chuyển đến lần lặp tiếp theo, các code cùng cấp phía sau nó cũng sẽ không được thực hiện.

# Hàm

## Khai báo hàm

    def ten_ham(param...):
       #commands

Trong đó:

- ten_ham: tên của hàm mà bạn muốn đặt. Lưu ý: **Tên hàm không được bắt đầu bằng số** và **không được chứa các ký tự đặc biệt** (trừ ký tự _)

- param...: các tham số bạn muốn truyền vào hàm, nếu không có tham số thì để trống.

Exp:

//hàm tính tổng hai số a,b

    def sum(a, b):
        print("sum = " + str(a + b))

## Gọi hàm

ten_ham() hoặc ten_ham(param...)

Exp:

sum(2,3)
//Gọi hàm sum vừa viết, kết quả hiển thị 5

## Phạm vi của biến trong hàm

- Một biến được khai báo ở trong hàm thì nó chỉ có thể được sử dụng ở trong hàm đó, không thể thay đổi giá trị của biến đã khai báo trong hàm mà tác động ra ngoài hàm (đối với các biến bình thường)

*Với biến có kiểu dữ liệu là list thì có thể tác động tới biến ở ngoài hàm*

**Biến global**: có thể gọi là tác động tới nó từ bất kỳ đâu trong chương trình

Khai báo biến global:

```global [ten bien]```

## Truyền vô số tham số vào hàm

Khi chưa biết được chính xác số lượng biến truyền vào trong hàm, ta khai báo một param đại diện cho các biến truyền vào hàm bằng cách thêm * vào trước param

Exp: hàm tính tổng dãy số truyền vào 
    def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp

    result = get_sum(1, 2, 3, 4, 5)

    print(result)

    //kết quả tổng của dãy số trên là 15

# Module trong Python

- Modules là cách phân hóa chương trình ra các nhánh nhỏ cho dễ quản lý và gọi lại chúng khi nào cần

**Import**

- Để import một module sẵn có vào file hiện tại 

```import [ten module]```

- Khi không muốn import toàn bộ module mà chỉ import một số thứ

```from [ten module] import [các thứ muốn import]```

**Định danh module**

- Trường hợp modules của chúng ta rất khó nhớ hay dài hay vì một lý do nào khác mà bạn không muốn gọi module như thế

    import [tên module] as [ten module theo cách mà bạn muốn gọi]

hoặc đối với from import

    from [tên module] import something as [ten module theo cách mà bạn muốn gọi]

> from .... import *: 

mặc định python nó sẽ không import được các đối tượng có tên được bắt đầu bằng ký tự

> import module nằm trong thư mục khác: Mặc định thì python nó sẽ chỉ load các module hệ thống của nó và các module ở cùng cấp với file hiện tại

     import os, sys
    // lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
     lib_path = os.path.abspath(os.path.join('modules'))
    // thêm thư mục cần load vào trong hệ thống
     sys.path.append(lib_path)
    // import
     from mathplus import get_sum

     print(get_sum(1,4));
// kết quả: 5


# Package

- Package: một thư mục chứa một hoặc nhiều modules hay các package khác nhau, nhằm mục đích phân bố các modules có cùng chức năng hay một cái gì đó, để dễ quản lý source code

## Buil package

Tạo thư mục với tên thư mục chính là tên package, trong thư mục phải có một file \__init__.py (giống như các constructor, được gọi ra đầu tiên khi import package đó)

## Import package

Tương tự như import module

## Package chứa package

Một package có thể chứa 1 hoặc nhiều package khác trong nó, không dưới hạn số lần chứa, nhưng vẫn phải luôn tuân thủ quy tắc của 1 package (phải có file \__init__.py). 

*Ví dụ*: package a chứa package b và package b lại chưa package c,...

# Generators

##  Iterator

Có rất nhiều đối tượng có thể sử dụng vòng lặp for (như list, tuple, string, ...). Những đối tượng đó gọi là những đối tượng ***"iterable"***. Thao tác duyệt qua những đối tượng này gọi là ***iteration***.

## Giao thức interation

Những đối tượng "iterable" có thể được duyệt qua các phần tử, bởi vì chúng được cài đặt phương thức \__iter__. Phương thức này sẽ trả về một đối tượng ***iterator***. Nếu một đối tượng "iterable" có nhiều kiểu duyệt phần tử khác nhau, có thể chúng ta sẽ cần thêm các xử lý để xác định iterator. 

*Ví dụ một đồ thị có thể duyệt theo chiều rộng và theo chiều sâu*

Iterator của Python chỉ có thể được duyệt qua 1 lần. Nên nếu đã duyệt qua phần tử nào rồi thì không thể duyệt qua nó thêm lần nào nữa

## Generator

Generator là một hàm trả kết quả về là một chuỗi kết quả thay vì một giá trị duy nhất

    def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

Mỗi lần lệnh yield được chạy, nó sẽ sinh ra một giá trị mới. (Vì thế nó mới được gọi là generator)

# OOP (Object Oriented Programming)

Python là một ngôn ngữ hướng đối tượng.

## Khái niệm 

- **OOP**: kĩ thuật lập trình cho phép tạo ra các đối tượng để trừu tượng hóa 1 thực thể (mô tả các đối tượng trong thực tế vào code) và tương tác với các đối tượng này.

- Một đối tượng bao gồm: *thuộc tính* (attributes) và *phương thức* (methods).

  + Thuộc tính (attributes): những thông tin, đặc điểm của đối tượng. 
  
  *VD: Con mèo có các thuộc tính: màu sắc, có đuôi, 2 tai, bốn chân, ...*

  + Phương thức (methods) là những thao tác, hành động mà đối tượng đó có thể thực hiện. 
  
  *VD: Con mèo có các phương thức: ăn, chạy nhảy, cắn, gào, rên, ....*

- *Lớp*:  là một kiểu dữ liệu đặc biệt do người dùng định nghĩa, tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó.

- *Đối tượng* là một thực thể của 1 lớp, được tạo ra từ lớp đó. 
VD: Mèo mun (tên là mèo mun, màu đen, có đuôi dài, 2 tai, 4 chân, ....) là đối tượng thuộc lớp mèo.

## Các nguyên lý cơ bản của OOP

- **Tính đóng gói** (Encapsulation): Các dữ liệu và phương thức có liên quan với nhau được đóng gói thành 1 lớp. Tức là *mỗi lớp được xây dựng để thực hiện một nhóm chức năng đặc trưng riêng*. Che giấu các thông tin của lớp đó đối với bên ngoài thể hiện ở *public, protected, private* đối với từng thuộc tính và phương thức.
- **Tính kế thừa** (Inheritance): *Lớp con có thể sử dụng lại các thuộc tính và phương thức của lớp cha mà không cần khai báo lại*. Trong Python, một class con có thể kế thừa nhiều class cha.
- **Tính trừu tượng** (Abstraction): Tổng quát hóa phương thức của đối tượng không quan tâm phương thức thực hiện như thế nào, được thể hiện bởi interface (có các tên phương thức nhưng ko có body của phương thức, khi class nào impliment interface thì thực hiện nó).
- **Tính đa hình** (Polymorphism): Tính đa hình được thể hiện bởi một phương thức, hành động có thể thực hiện theo nhiều cách khác nhau. 

*VD: chó mèo cùng là động vật nhưng khi thực hiện phương thức 'sủa' thì chó sủa 'gogo', mèo sủa 'méo mèo'*

## Class

- Tạo class:

Khi bạn tạo một class mà không có khai triển gì, nó sẽ gây ra lỗi. (Để tránh lỗi này, sử dụng từ khóa *pass*)

    class MyClass:
    pass

Theo qui ước, tên của class trong Python được đặt theo *ThePascalCase* (từ đầu tiên của tất cả các từ phải được viết Hoa, ví dụ: MyClass, UserAcount,...)

- Tạo đối tượng từ class:

```[đối tượng] = [class]()```

Ví dụ:

    // Tạo class
    class MyClass:
       pass
    // Tạo đối tượng từ class MyClass
    a = MyClass()
    print(a)

- Lấy ra kiểu dữ liệu của đối tượng (xem thuộc class nào)

```type(đối tượng)```

hoặc

```[đối tượng].__class__```

Ví dụ:

    type(a)
    \\<class '__main__.MyClass'>
    a.__class__
    \\ <class '__main__.MyClass'>

- Phương thức trong class:

Phương thức trong class tương tự như hàm.
Tuy nhiên, mỗi phương thức phải có ít nhất một tham số. Theo quy ước, trong Python, tham số này được gọi là self.

Phương thức **.\__init__()**: được gọi sau khi một thể hiện của class được tạo.
Nó khởi tạo các thành viên trong class.

# Exception

- **Exception** (Ngoại lệ): bất kỳ điều kiện bất thường nào trong chương trình phá vỡ luồng thực thi chương trình đó. Bất cứ khi nào một ngoại lệ xuất hiện, chương trình sẽ ngừng thực thi, chuyển qua quá trình gọi và in ra lỗi đến khi nó được xử lý.

- **Handling Exceptions**:

       try:
        // code
      except exceptionName:
        // code

*Ví dụ:*

    def sum(a, b):
    return a / b
    try :
       print(sum(6, 0))
    except ZeroDivisionError:
       print('Co loi xay ra!')
//ket qua: Co loi xay ra!

>Nếu như trong khối lệnh *try except* có 1 đoạn lệnh chắc chắn sẽ được thực thi cho dù try đúng hay sai, thì phải khai báo thêm khối lệnh finally vào cuối khối lệnh try except 

    try:
       # code
    except:
       # code
    finally:
       # code

- Xây dựng Exeption riêng:

Để tạo một exception trong Python thì bắt buộc exception này phải kế thừa lớp Exception trong Python

VD: Một Exception có tên exceptionDemo.

    class ExceptionDemo(Exception):
        def __init__(self, value):
            print("Loi: " + value)

Để gọi exception vừa tạo (exceptionName là tên của exception bạn muốn gọi):

```raise exceptionName```

# Multithread/Multiprocess

## Đa luồng (Multithreading) là gì:
Một chương trình đa luồng chứa hai hoặc nhiều phần có thể chạy đồng thời và mỗi phần có thể xử lý tác vụ khác nhau tại cùng một thời điểm, để sử dụng tốt nhất các nguồn có sẵn.

*Ví dụ:*
- Đoạn code tính diện tích và thể tích bình thường:

      import time

      def cal_square(numbers):
	    print("calculate square number")
	  for n in numbers:
		time.sleep(0.2)
		print ('square:', n*n)

      def cal_cube(numbers):
	  print("calculate cube number")
	  for n in numbers:
		time.sleep(0.2)
		print ('square:', n*n*n)

      arr = [2,3,7,9]
      t = time.time()
      cal_square(arr)
      cal_cube(arr)
      print ("done in ", time.time()- t)

Chương trình chạy đa luồng

    from threading import Thread
    import threading
    import time

    def cal_square(numbers):
	    print("calculate square number")
	    for n in numbers:
		  time.sleep(0.2)
		  print ('square:', n*n)


    def cal_cube(numbers):
	    print("calculate cube number \n")
	    for n in numbers:
		  time.sleep(0.2)
		  print ('cube:', n*n*n)

     arr = [2,3,7,9]

    try:
	    t = time.time()
	    t1 = threading.Thread(target=cal_square, args=(arr,))
	    t2 = threading.Thread(target=cal_cube, args=(arr,))
	    t1.start()
	    t2.start()
	    t1.join()
	    t2.join()
	print ("done in ", time.time()- t)
    except:
	    print ("error")

## thread module

Để chạy thread, ta dùng method start(). Target sẽ là function myThread, là nhiệm vụ mà thread phải hoàn thành

(Ví dụ bên trên)

Hiệu quả với đa luồng tầm thấp
## threading module

Ngoài các phương thức có trong thread Module, threading Module còn bổ sung thêm một số phương thức khác:

- threading.activeCount(): Trả về số đối tượng thread mà là active.
- threading.currentThread(): Trả về số đối tượng thread trong Thread control của Caller.
- threading.enumerate(): Trả về một danh sách tất cả đối tượng thread mà hiện tại là active.

Threading Module có lớp Thread để triển khai đa luồng. Lớp này có các phương thức sau:

- run(): Là entry point cho một Thread.
- start(): Bắt đầu một thread bởi gọi phương thức run().
- join([time]): Đợi cho các thread kết thúc.
- isAlive(): Kiểm tra xem một thread có đang thực thi hay không.
- getName(): Trả về tên của một thread.
- setName(): Thiết lập tên của một thread.

>Dừng các thread lại: ```setDaemon(True)```

## Đồng bộ hóa các thread

Trong lập trình đa luồng, các threads chia sẻ chung tài nguyên của tiến trình, vì vậy có những thời điểm **nhiều luồng sẽ đồng thời thay đổi dữ liệu chung**. 

=> Cần cơ chể để đảm bảo **tại một thời điểm chỉ có duy nhất một luồng được phép truy cập vào dữ liệu chung**, nếu các luồng khác muốn truy cập vào đoạn dữ liệu này thì cần phải đợi cho thread trước đó hoàn thành công việc của mình.

Trong threading Module, **kỹ thuật locking** cho phép bạn đồng bộ hóa các Thread. Một lock mới được tạo bởi gọi phương thức *Lock()*.

Phương thức *acquire(blocking)* của đối tượng lock mới này được sử dụng để ép các Thread chạy một cách đồng bộ. Tham số blocking tùy ý cho bạn khả năng điều khiển để xem một Thread có cần đợi để đạt được lock hay không.

+ Nếu tham số blocking được thiết lập là 0, tức là Thread ngay lập tức trả về một giá trị 0 nếu không thu được lock và trả về giá trị 1 nếu thu được lock. 
+ Nếu blocking được thiết lập là 1, thì Thread cần đợi cho đến khi lock được giải phóng.

Phương thức *release()* của đối tượng lock được sử dụng để giải phóng lock khi nó không cần nữa.
