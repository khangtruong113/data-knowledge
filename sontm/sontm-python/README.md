# Core Python: Basics

**Python** - ngôn ngữ lập trình máy tính bậc cao thường được sử dụng để xây dựng trang web và phần mềm, tự động hóa các tác vụ và tiến hành phân tích dữ liệu. 

## 0. Installation

**- Python**: https://www.python.org/downloads/

**- IDE - Integrated Development Environment (môi trường phát triển tích hợp)**: Tuỳ mục đích sử dụng Python khác nhau, ta có thể lựa chọn IDE phù hợp như PyCharm, Visual Studio Code, Jupyter Notebook,...

## 1. Types and Operations
### 1.1. Data Types
**- Text Type**: `str`

**- Numeric Types:** `int, float, complex`

**- Mapping Type:** `dict`

**- Set Types:** `set, frozenset`

**- Boolean Type:** `bool`

**- Binary Types:** `bytes, bytearray, memoryview`

![DataType](https://th.bing.com/th/id/OIP.VjE8LEwBsZAF98QKkbdGtwHaDY?pid=ImgDet&rs=1)

***Check Data Types:*** `type(var)`

**List vs. tuple vs. set vs. dictionary in Python**

|                         | Lists                                        | Tuples                                        | Sets                                                | Dictionaries                                                                                                                         |
| ----------------------- | -------------------------------------------- | --------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Ordered**             | A list is a collection of *ordered* data     | A tuple is an *ordered* collection of data    | A set is an *unordered* collection                  | A dictionary is an *unordered* collection of data that stores data in key-value pairs (*but  it is ordered in Python 3.7 and above*) |
| **Mutable - Changable** | Lists are *mutable*                          | Tuples are *immutable*                        | Sets are *mutable* and have *no duplicate elements* | Dictionaries are *mutable* and keys *do not allow duplicates*                                                                        |
| **Punctuation**         | Lists are declared with *square braces* `[]` | Tuples are enclosed within *parenthesis*	`()` | Sets are represented in *curly brackets* `{}`       | Dictionaries are enclosed in *curly brackets* in the form of key-value pairs `{}`                                                    |
| **Function**            | List can be created using list() function    | Tuple can be created using tuple() function   | Set can be created using set() function             | Dictionary can be created using dict() function                                                                                      |
| **Example**             | [1, 2, 3, 4, 5]                              | (1, 2, 3, 4, 5)                               | {1, 2, 3, 4, 5}                                     | {1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}                                                                                             |
**Create**

***List***
```
list1 = [1,4,"Minh",6,"Son"]
list2 = []  # creates an empty list
list3 = list((1,2,3))
print(list1)
print(list2)
print(list3)
```

***Tuple***
```
tuple1 = (1,2,"MinhSon",9)
tuple2 = () # creates an empty tuple
tuple3 = tuple((1,3,5,9,"Data"))
print(tuple1)
print(tuple2)
print(tuple3)
```

***Set***
```
set1 = {1,2,3,4,5,"Analytics","Engineer"}
set2 = {(1,8,"python",7)}
print(set1)
print(set2)
```

***Dictionary***
```
dict1 = {"key1":"value1","key2":"value2"}
dict2 = {}   # empty dictionary
dict3 = dict({1:"Son",2:"Analytics",3:"Engineer"})
print(dict1)
print(dict2)
print(dict3)
```

**Index, Immutable, Concantenate**

***List***
```
list1 = ["hello",1,4,8,"good"]
print(list1)
list1[0] = "morning"  # assigning values ("hello" is replaced with "morning")
print(list1)
print(list1[4])
print(list1[-1]) # list also allow negative indexing
print(list1[1:4]) # slicing
list2 = ["apple","mango","banana"]
print(list1+list2) # list concatenation
```

***Tuple***
```
tuple1 = ("good",1,2,3,"morning")
print(tuple1)
print(tuple1[0])  # accessing values using indexing
#tuple1[1]="change"  # a value cannot be changed as they are immutable
tuple2 = ("orange","grapes")
print(tuple1+tuple2)  # tuples can be concatenated
tuple3 = (1,2,3)
print(type(tuple3))
```

***Set***
```
set1 = {1,2,3,4,5}
print(set1)
# set1[0]   sets are unordered, so it doesnot support indexing
set2 = {3,7,1,6,1} # sets doesnot allow duplicate values
print(set2)
```

***Dictionary***
```
dict1 = {"key1":1,"key2":"value2",3:"value3"}
print(dict1.keys())  # all the keys are printed
dict1.values() # all the values are printed
dict1["key1"] = "replace_one"  # value assigned to key1 is replaced
print(dict1)
print(dict1["key2"])
```

**Add, remove**

***List***
```
list1 = ["apple","banana","grapes"]
list1.append("strawberry")   # strawberry is added to the list
print(list1)
list1.pop()  # removes the last element from the list
print(list1)
list1.pop()
print(list1)
```

***Tuple***
```
tuple1 = (1,2,3,4)
# tuple1.pop()    tuple cannot be modified
# tuple1.append()  tuple cannot be modified
print(tuple1)
```

***Set***
```
set1 = {"water","air","food"}
set1.add("shelter")   # adds an element to the set at random position
print(set1)
set1.add("clothes")
print(set1)
set1.pop()  # removes random element from the set
print(set1)
```

***Dictionary***
```
dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
dict1.update({"veg2":"brinjal"})
print(dict1)
dict1.update({"veg3":"chilli"})  # updates the dictionary at the end
print(dict1)
dict1.pop("veg2")
print(dict1)
```

**Duplicate, Mutable, Ordered**

***List***

```
list1 = [1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2 = [2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,2)) # returns the index value of the element from the particular start position given
print(list1.count())
print(list1.reverse())
```

***Tuple***
```
tuple1 = (1,3,6,7,9,10)
print(tuple1.index(6))
print(tuple1.index(9))
print(tuple1.count()) 
# print(tuple1.reverse())    The reverse() method is not defined in tuples, as they are unchangeable

```

***Set***
```
set1 = {1,5,6,3,9}
# set1.index()  will throw an error as they are unordered

# print(tuple1.count())    There are no count() methods in sets as they do not allow any duplicates.
# print(tuple1.reverse())    The sets are unordered, which refrains from applying the reverse() method
```

***Dictionary***
```
dict1 = {"key1":"value1","key2":"value2"}
# dict1.index("key1") will throw an error
print(dict1.get("key1"))

# print(tuple1.count())    The count() method is not defined in the dictionary.
# print(tuple1.reverse())      The elements cannot be reversed, as the items in the dictionary are in the form of key-value pairs
```

## 1.2. Operators
### 1.2.1. Toán tử số học - Arithmetic Operators

Ta có `a = 8` và `b = 10`

| Toán tử  | Mô tả  | Kết quả
|---|---|---|
| **+**  |  Cộng  |  	a + b = 18  |
| **-**  |  Trừ  |  	a - b = -2  |
| *  |  Nhân  |  	a * b = 80  |
| **/**  |  Chia  |  	a / b = 0.8  |
| **%**  |  Chia lấy phần dư  |  	a % b = 8  |
| ******  |  Mũ  |  	a ** b = 1073741824  |
| **//**  |  Toán tử chia làm tròn xuống  |  	a + b = 0  |

### 1.2.2. Toán tử quan hệ - Comparison (Relational) Operators

Ta có `a = 8` và `b = 10`

| Toán tử  | Chú thích  | Kết quả
|---|---|---|
| **==** | Giá trị bằng nhau trả về True |  	a == b  <br>// False  |
| **!=**  |  Giá trị không bằng nhau trả về True |  	a != b <br>//True  |
| **<**	  |  Giá trị 1 nhỏ hơn giá trị 2 trả về True  |  	a != b <br>//True  |
| **>**  |  Giá trị 1 lớn hơn giá trị 2 trả về True  |  	a != b <br>//False  |
| **<=**	  |  Giá trị 1 nhỏ hơn hoặc bằng giá trị 2 trả về True  |  	a != b <br>//True  |
| **>=**  |  Giá trị 1 lớn hơn hoặc bằng giá trị 2 trả về True  |  	a != b <br>//False  |

### 1.2.3. Toán tử gán - Assignment Operators

| Toán tử  | Chú thích  | Kết quả | Tương đương
|---|---|---|---|
|  **=**  | Gán giá trị của một đối tượng cho một giá trị   |  a = b  | a = b|
| **+=**   | Cộng rồi gắn giá trị cho đối tượng   | a += b   |  a + b |
| **-=**   | Trừ rồi gắn giá trị cho đối tượng   | a -= b   |  a - b |
| ***=**   | Nhân rồi gắn giá trị cho đối tượng   | a *= b   |  a * b |
| **/=**   | Chia rồi gắn giá trị cho đối tượng   | a /= b   |  a / b |
| **%=**   | Chia lấy phần dư rồi gắn giá trị cho đối tượng   | a %= b   |  a % b |
| ****=**   | Mũ rồi gắn giá trị cho đối tượng   | a **= b   |  a ** b |
| **//=**   | Chia làm tròn xuống rồi gắn giá trị cho đối tượng   | a //= b   |  a // b |

### 1.2.4. Toán tử logic - Logical Operators

|  Toán Tử | Chú Thích  |
|---|---|
| **and**  |  Cả 2 giá trị True -> trả kết quả True<br> 1 trong 2 giá trị là False -> False |
| **or**  |  1 trong 2 giá trị là True  -> True <br> 2 giá trị là False -> False |
| **not**  |  Biểu thức là True thì nó sẽ trả về là False và ngược lại|


### 1.2.5. Toán tử Biwter - Bitwise Operators

Toán tử này thực hiện trên các bit của các giá trị -> Ít được sử dụng

`a = 12` -> `a = 00001100`

`b = 15` -> `b = 00001111`

|  Toán Tử | Ví dụ  |
|---|---|
| **&**  | (a & b) = 12 (00001100) |
| **|**  |  (a | b) = 14 (00001111) |
| **^**  |  	(a ^ b) = 2 (00000010) |
| **~**  |  	(~a) = -13 (00001101) |
| **<<**  |  		a<<a = 49152|
| **>>**  |  	a>>a = 0 |

### 1.2.6. Toán tử khai thác - Membership Operators


|  Toán Tử | Chú Thích  |
|---|---|
| **in**  |  1 đối số thuộc 1 tập -> True |
| **not in**  |  1 đối số không thuộc 1 tập -> True |

### 1.2.7. Toán tử xác thực - Indentity Operators

|  Toán Tử | Chú Thích  |
|---|---|
| **is**  |  2 giá trị bằng nhau (a == b) -> True |
| **not is**  |  2 giá trị bằng nhau (a != b) -> True |

## 2. Basic Statements and Syntax

