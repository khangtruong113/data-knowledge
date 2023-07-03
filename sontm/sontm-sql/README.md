# SQL: BASICS

**Structured Query Language (SQL)** - Ngôn ngữ truy vấn có cấu trúc là ngôn ngữ tiêu chuẩn mà bất cứ hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) nào cũng phải đáp ứng, điển hình như Oracle, Sybase, Microsoft SQL Server, Access, Ingres,…

## 0. Installation

**- SQL Server:** https://www.microsoft.com/en-in/sql-server/sql-server-downloads

**- SQL Server Management Studio (SSMS):** https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16

## 1. Components of SQL

![SQL Commands](https://i.pinimg.com/originals/c1/aa/e7/c1aae7accdcb5fd602c882b973414b34.png)

## 1.1. DDL: Data Definition Language

**- ```CREATE```:** tạo database và các đối tượng như table, view, function, sp,...

**- ```DROP```:** xoá đối tượng trong cơ sở dữ liệu

**- ```ALTER```:** thay đổi cấu trúc trong database

**- ```TRUNCATE```:** Xoá các bản ghi trong bảng, giải phóng bộ nhớ và không thể hoàn lại

**- ```COMMENTS```:** Viết các comments cho các SQL queries

**- ```RENAME```:** Đổi tên bảng hoặc các đối tượng trong database

## 1.2. DML: Data Manipulation Language

**- ```INSERT```:** Thêm bản ghi mới cho bảng

**- ```UPDATE```:** Cập nhật hoặc thay đổi dữ liệu trong bảng

**- ```DELETE```:** Xoá một hoặc nhiều dòng dữ liệu trong bảng

## 1.3. DCL: Data Control Language

**- ```GRANT```:** cấp quyền truy cập hoặc các đặc quyền với đối tượng cơ sở dữ liệu cho người dùng.

**- ```REVOKE```:** thu hồi quyền truy cập của người dùng hoặc các đặc quyền với các đối tượng cơ sở dữ liệu.

## 1.4. TCL: Transaction Control Language

**- ```COMMIT```:** để lưu các thay đổi gọi bởi một transaction với cơ sở dữ liệu. Lệnh COMMIT lưu tất cả các transaction vào cơ sở dữ liệu kể từ khi lệnh COMMIT hoặc ROLLBACK cuối cùng.

**- ```ROLLBACK```:** hoàn tác các transaction chưa được lưu vào cơ sở dữ liệu. Lệnh này chỉ có thể được sử dụng để hoàn tác các transaction kể từ khi lệnh COMMIT hoặc ROLLBACK cuối cùng được phát hành.

**- ```SAVEPOINT```:** tạo các điểm (point) bên trong các nhóm Transaction để ROLLBACK, tức là để quay trở lại điểm trạng thái đó.

## 1.5. DQL: Data Query Language

**- ```SELECT```:** trích xuất dữ liệu 

## 2. Basic Commands

| Command  | Description                       |Example     |
| -------- | --------------------------------- |------------|
| `SELECT` | Trích xuất dữ liệu trong database |`SELECT` column1, column2, ...  <br> `FROM` table_name;|
| `SELECT DISTINCT`          |  Trích xuất dữ liệu riêng riêng biệt (khác nhau)                                |`SELECT DISTINCT` column1, column2, ... <br>`FROM` table_name;|
| `WHERE`         |   Lọc records theo các điều kiện                                |`SELECT` column1, column2, ... <br>`FROM` table_name <br>`WHERE` condition;|
| `AND`, `OR`, `NOT`       |  `AND` và `OR` dùng lọc records hơn 1 điều kiện.  `NOT` dùng lọc records khi điều kiện không đúng|`SELECT` column1, column2, ... <br>`FROM` table_name <br>`WHERE` `NOT` (condition1 AND condition2) `OR `condition3 ...;|                                 |
| `ORDER BY`     | Sắp xếp kết quả theo thứ tự tăng dần hoặc giảm dần trên một hoặc nhiều cột khác nhau                                  |`SELECT` column1, column2, ... <br>`FROM` table_name <br>`ORDER BY` column1, column2, ... ASC|DESC;
| `LIKE`         |  So sánh một giá trị với các giá trị tương tự bằng cách sử dụng các toán tử đại diện (wildcard)                              |`SELECT` column1, column2, ... <br>`FROM` table_name <br>`WHERE` columnN `LIKE` pattern;|
|  `IN`        |  chỉ định nhiều giá trị trong mệnh đề WHERE                                 |`SELECT` column_name(s) <br>`FROM` table_name <br>`WHERE` column_name `IN` (value1, value2, ...);|
| `BETWEEN`         | Dùng cùng `WHERE` để chọn các giá trị trong một khoảng nhất định                                  | `SELECT` column_name(s) <br>`FROM` table_name <br>`WHERE` column_name `BETWEEN` value1 `AND` value2; |
| `AS`         |  Gán một tên mới tạm thời cho một cột bảng hoặc thậm chí một bảng                                 | `SELECT` column_name `AS` alias_name <br>`FROM` table_name; |
| `JOIN`         |  kết hợp các data từ hai hoặc nhiều bảng với nhau để thành kết quả mong muốn: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`                                |`SELECT` Orders.OrderID, Customers.CustomerName, Orders.OrderDate  <br>`FROM` Orders   <br>`INNER JOIN` Customers `ON` Orders.CustomerID=Customers.CustomerID;  |
| `UNION`         |  Kết hợp tập hợp kết quả của hai hoặc nhiều câu lệnh SELECT. Hai câu lệnh phải cùng số lượng cột. Các cột phải có cùng kiểu dữ liệu, các cột trong mỗi câu lệnh SELECT phải có cùng trật tự. `UNION ALL` tương tự nhưng loại bỏ dòng trùng                                | `SELECT` column_name(s) `FROM` table1 <br>`UNION` <br>`SELECT` column_name(s) `FROM` table2; |
| `GROUP BY`         | Sắp xếp dữ liệu giống nhau thành các nhóm. Thường dùng với các hàm tính toán `COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()` để nhóm các kết quả giá trị với nhau                                | `SELECT` column_name(s)<br>`FROM` table_name <br>`WHERE` condition <br>`GROUP BY` column_name(s) <br>`ORDER BY` column_name(s); |
|  `HAVING`         | chỉ định điều kiện lọc mà kết quả nhóm xuất hiện trong kết quả. Dùng với đặt các điều kiện vào các nhóm được tạo bởi mệnh đề `GROUP BY`                                | `SELECT` column_name(s) <br>`FROM` table_name <br>`WHERE` condition <br>`GROUP BY` column_name(s) <br>`HAVING` condition <br>`ORDER BY` column_name(s); |


## 3. Data Types

![Data Types](https://www.simplilearn.com/ice9/free_resources_article_thumb/Categories_of_data_types-SQL_Data_Types.PNG)

### 3.1 Numeric

|Data type   |  Description |Storage|
|---|---|---|
| `bit`  |  	Integer that can be 0, 1, or NULL | |
| `tinyint ` | Allows whole numbers from 0 to 255       |  1 byte       |
| `smallint`       | Allows whole numbers between -32,768 and 32,767       |  2 bytes       |
| `int`   |  Allows whole numbers between -2,147,483,648 and 2,147,483,647      |  4 bytes       |
|   `bigint`    | Allows whole numbers between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807       | 8 bytes        |
| `decimal(p,s)`   | Fixed precision and scale numbers. <br> Allows numbers from -10^38 +1 to 10^38 –1. <br> The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. <br>  The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0    | 5-17 bytes        |
| `numeric(p,s)`   |  Fixed precision and scale numbers. <br> Allows numbers from -10^38 +1 to 10^38 –1. <br> The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18. <br> The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0      |  5-17 bytes       |
| `smallmoney`   |  	Monetary data from -214,748.3648 to 214,748.3647      | 4 bytes        |
|  `money`  | Monetary data from -922,337,203,685,477.5808 to 922,337,203,685,477.5807       |  8 bytes       |
| `float(n)`   | Floating precision number data from -1.79E + 308 to 1.79E + 308.<br> The n parameter indicates whether the field should hold 4 or 8 bytes. float(24) holds a 4-byte field and float(53) holds an 8-byte field. Default value of n is 53.       |  4 or 8 bytes       |
| `real`   | Floating precision number data from -3.40E + 38 to 3.40E + 38       |  4 bytes       |

###  3.2. Character and String Data Types

| Data Type  | Description  | Max Size |  Storage|
|---|---|---|---|
| `char(n)`  | Fixed width character string  |  8,000 characters | Defined width   |
|`varchar(n)`   | Variable width character string	  | 8,000 characters  | 2 bytes + number of chars  |
| `varchar(max)`  | Variable width character string  | 1,073,741,824 characters  | 2 bytes + number of chars  |
| `text`  | 	Variable width character string  | 2GB of text data  | 4 bytes + number of chars  |

### 3.3. Unicode Character and String Data Types

| Data Type  | Description  | Max Size |  Storage|
|---|---|---|---|
| `nchar`  | Fixed width Unicode string  | 	4,000 characters  | 	Defined width x 2  |
|`nvarchar`  | Variable width Unicode string  | 4,000 characters  |   |
| `nvarchar(max)`  | Variable width Unicode string  | 536,870,912 characters  |   |
| `ntext`  | Variable width Unicode string  | 2GB of text data  |   |

### 3.4. Binary Data Types

| Data Type  | Description  | Max Size |  Storage|
|---|---|---|---|
| `binary(n)`  | Fixed width binary string  | 8,000 bytes  |   |
| `varbinary`  | Variable width binary string  | 8,000 bytes  |   |
|  `varbinary(max)` | Variable width binary string  | 	2GB  |   |
|  `image` | Variable width binary string  | 	2GB  |   |

### 3.5. Date and Time Data Types

| Data Type  |  Description | Storage   |
|---|---|---|
| `datetime` | From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds  | 8 bytes  |
| `datetime2`  | From January 1, 0001 to December 31, 9999 with an accuracy of 100 nanoseconds  | 	6-8 bytes  |
| `smalldatetime`  | From January 1, 1900 to June 6, 2079 with an accuracy of 1 minute  | 4 bytes  |
| `date`  | Store a date only. From January 1, 0001 to December 31, 9999  | 3 bytes  |
| `time`  | Store a time only to an accuracy of 100 nanoseconds  | 	3-5 bytes  |
|  `datetimeoffset` | The same as datetime2 with the addition of a time zone offset  | 8-10 bytes  |
| `timestamp`  |  Stores a unique number that gets updated every time a row gets created or modified. The timestamp value is based upon an internal clock and does not correspond to real time. <br> Each table may have only one timestamp variable |   |

### 3.6. Other Data Types

| Data Type  |  Description |
|---|---|
| `sql_variant`  | Stores up to 8,000 bytes of data of various data types, except text, ntext, and timestamp  |
| `uniqueidentifier`   | Stores a globally unique identifier (GUID)   |
| `xml`   | Stores XML formatted data. Maximum 2GB   |
| `cursor`   | 	Stores a reference to a cursor used for database operations   |
| `table`   | Stores a result-set for later processing   |

## 4. Window Functions

`Window Functions` thực hiện các phép tính toán các dòng trong bảng mà có liên quan đến dòng hiện tại. 

`Window Functions` cũng tính toán như `Aggregate Functions` tuy nhiên điểm khác biệt chính là khi dùng `Window Function` các row sẽ không bị gộp lại thành một như khi dùng `Aggregate Function`

![Window Functions](data:image/png;base64,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)

## 4.1. Syntax:

>SELECT <column_1>, <column_2>,<br> 
<**window_functions**>(espression) **OVER** (**PARTITION BY**<partition_list> **ORDER BY** <order_list> <frame_clause>)<br>
FROM <table_name>

Trong đó:
- `window_function`: Tên window functions mà ta muốn sử dụng (sum, avg, row_number)
- `expression`: tên column mà ta muốn tính toán. Expression có thể không bắt buộc có tuỳ theo window functions
- `OVER`: dấu hiệu đây là window functions
- `PARTITION BY`: chia nhóm các hàng thành các partitions để có thể tính toán window function
- `partition_list`: Tên một hoặc nhiều cột ta muốn PARTITION BY
- `ORDER BY`: Sắp xếp các hàng trong từng parttion
- `order_list`: Tên một hoặc nhiều cột ta muốn ORDER BY
- `frame_clause`: giới hạn phân vùng bằng cách đặt điểm đầu và điểm cuối các hàng muốn chọn.

***FRAME_CLAUSE***:

Trong `frame_clause` cú pháp chung là:
> frame_unit {<frame_start>|<frame_between>}

Trong đó:
- `PRECEDING`: xác định điểm đầu của partition
  - `UNBOUNDED PRECEDING`: dòng đầu tiên của partition
  - `<value> PRECEDING` (ex: ```2 PRECEDING```): 2 dòng trước tính từ dòng hiện tại
- `CURRENT ROW`: dòng hiện tại
- `FOLLOWING`: xác định điểm cuối của partition
  - `UNBOUNDED FOLLOWING`: dòng cuối cùng của partition
  - `<value> FOLLOWING` (ex: ```2 FOLLOWING```): 2 dòng tiếp sau tính từ dòng hiện tại
- `BETWEEN...AND`: thể hiện khoảng bắt đầu và kết thúc partition để tính toán.

![Window Functions](https://media.techmaster.vn/api/static/c77cd27k0cmou6gu4m20/X4rBuzRw)

Trong cú pháp frame_unit có 2 giá trị để lựa chọn ROWS hoặc RANGE:
- `ROWS` tạo ra frame dựa trên số lượng với hàng hiện tại : n preceding, m following. Khi sử dụng ROWS, duplicate được coi như unique value -> Tính toán window functions theo từng hàng theo chỉ định.
 <br>`ROWS` có thể sử dụng các frame delimiters sau:
  + UNBOUNDED PRECEDING
  + UNBOUNDED FOLLOWING
  + CURRENT ROW
  + N PRECEDING
  + N FOLLOWING

- `RANGE` thì dựa trên tính chất của hàng: unbounded preceding, unbounded following. Khi sử dụng RANGE, đối các giá trị duplicate hàm sẽ được tính toán trước và trả giá trị giống nhau cho các hàng duplicate.
Nếu không khai báo giá trị mặc định cho mệnh đề này là: `range between unbounded preceding and current row`
<br> `RANGE` có thể sử dụng các frame delimiters sau:
  + UNBOUNDED PRECEDING
  + UNBOUNDED FOLLOWING
  + CURRENT ROW

## 4.2. Phân loại Window Functions

### 4.2.1. Aggregate Functions:

- `SUM()`: Tổng các giá trị
- `COUNT()`: Đếm các giá trị
- `AVG()`: Tính trung bình các giá trị
- `MAX()`: Tìm giá trị lớn nhất
- `MIN()`: Tìm giá trị nhỏ nhất

### 4.2.2. Ranking Functions

- `ROW_NUMBER()`: Xếp hạng các giá trị trong từng partition lần lượt mà không quan tâm gía trị trùng nhau
- `RANK()`: giống `row_number()` nhưng `RANK()` khi gặp giá trị duplicate sẽ xếp cùng hạng nhau. Hàm `RANK()` sẽ bỏ qua thứ hạng tiếp theo cho những dòng có cùng hạng trước đó
- `DENSE_RANK()`: giống `RANK()` nhưng Hàm `DENSE_RANK()` không bỏ qua thứ hạng tiếp theo cho những dòng có cùng hạng trước đó
- `CUME_DIST()`: Tính tỷ lệ các giá trị nhỏ hơn hoặc bằng giá trị hiện tại
- `PERCENT_RANK()`: (rank -1)/(row-1)
<br> Trong đó:

  + rank là thứ tự của giá trị đó theo thứ tự tăng dần (các giá trị giống nhau trả về thứ hạng giống nhau)

  + row: tổng số dòng (xét trong 1 partition)

### 4.2.3. Analytics Functions:

- `FIRST_VALUE (expression)`: Lấy giá trị đầu trong từng partition
- `LAST_VALUE (expression)`: Lấy giá trị cuối trong từng partition
- `LAG(expression, offset)`:  trả về giá trị của n hàng trước nó trong bảng kể từ row hiện tại
<br> Trong đó offset: số hàng lệch so với hàng hiện tại (Nếu tham số này bị bỏ qua, mặc định là 1)
- `LEAD(expression, offset)`: trả về giá trị của n hàng tiếp theo nó trong bảng kể từ row hiện tại
<br> Trong đó offset: số hàng lệch so với hàng hiện tại (Nếu tham số này bị bỏ qua, mặc định là 1)

# 5. Server-Side Programming

## 5.1. Biến
`Variable (biến)` là một đối tượng trong CSDL dùng để lưu dữ liệu tạm thời.

- `Biến toàn cục:` Nó có sẵn và hệ thống quản lý và trong SQL server được đặt tên bắt đầu bởi 2 ký hiệu @.
Ví dụ: `@@VERSION` - Thông tin phiên bản Microsoft SQL Server;<br>`@@ERROR` - Mã lỗi của câu lệnh thực thi gần nhất;<br>`@@ROWCOUNT` - Số dòng bị tác động bởi câu lệnh gần nhất;...

- `Biến cục bộ:` Nó dùng để lưu trữ do người dùng tạo ra và để lưu trữ những giá trị tạm thời. Ở đây chúng ta chủ yếu quan tâm đến biến cục bộ.

**Khai báo biến**:

`DECLARE @var_name data_type;`

**Gán giá trị cho biến:**

`SET @var_name = value;`

**Khai báo biến với giá trị mặc định**
`DECLARE @var_name data_type = value;`


## 5.2. Function:
`Function` Là một đối tượng trong cơ sở dữ liệu (CSDL) sử dụng trong các câu lệnh SQL, được biên dịch sẵn và lưu trong CSDL nhằm mục đích thực hiện xử lý nào đó như tính toán phức tạp và trả về kết quả là giá trị nào đó.
- Hàm đơn trị (Scalar Function)
- Hàm đọc bảng (Inline Table-Valued Function).
- Hàm tạo bảng (Multi-Statement Table-Valued Function).

**Hàm đơn trị (Scalar Function)**
```
CREATE FUNCTION func_name(param_list)
RETURNS data_type
AS
BEGIN
    <statement>
    RETURN value
END
GO
```

**Hàm đọc bảng (Inline Table-Valued Function)**
```
CREATE FUNCTION func_name(param_list)
RETURNS TABLE
AS
RETURN
(
    Query
)
GO
```

**Hàm tạo bảng (Multi-Statement Table-Valued Function)**
```
CREATE FUNCTION func_name(param_list)
RETURNS Tên_biến TABLE(table_type_definition)
AS
BEGIN
    INSERT | UPDATE | DELETE
    RETURN
END
GO
```

***Thay đổi function***: Cú pháp tương tự như tạo mới Function, chỉ thay từ khóa `CREATE` bằng từ khóa `ALTER`

***Xóa Function***: `DROP FUNCTION`
`DROP FUNCTION [schema_name.] <func_name>`

***Xem nội dung Function***: Để xem nội dung function ta sử dụng Store Procedure (Thủ tục) có sẵn của SQL là `sp_helptext` (Transact-SQL)

`EXEC sp_helptext 'func_name'`

## 5.3. Store Procedure

`Stored procedure` là tập hợp một hoặc nhiều câu lệnh T-SQL thành một nhóm đơn vị xử lý logic và được lưu trữ trên Database Server. Khi một câu lệnh gọi chạy stored procedure lần đầu tiên thì SQL Server sẽ chạy nó và lưu trữ vào bộ nhớ đệm, gọi là plan cache, những lần tiếp theo SQL Server sẽ sử dụng lại plan cache nên sẽ cho tốc độ xử lý tối ưu.

```
CREATE [OR ALTER] {PROC | PROCEDURE} [schema_name.] procedure_name([@parameter data_type [ OUT | OUTPUT | [READONLY]] 
[ WITH <procedure_option> ]
[ FOR REPLICATION ]
    AS
    BEGIN
        sql_statements 
    END
```

***Thay đổi Store Procedure***: Cú pháp tương tự như tạo mới Store Procedure, chỉ thay từ khóa `CREATE` bằng từ khóa `ALTER`

***Xoá Store Procedure***: `DROP PROCEDURE`

`DROP PROCEDURE sp_name`

***Thực thi Store Procedure***: `EXEC`

`EXEC sp_name`

## 5.4. Function vs Store Procedure

- Giống: Cả stored procedure và function đều là các đối tượng cơ sở dữ liệu chứa một tập các câu lệnh SQL để hoàn thành một tác vụ.
- Khác: 
  - Store Procedure có thể trả về giá trị zero, một hoặc nhiều giá trị. Trong khi Function phải trả về một giá trị duy nhất (có thể là bảng).
  - Các Function chỉ có thể có các tham số đầu vào cho nó trong khi Store Procedure có thể có các tham số đầu vào hoặc đầu ra.
  - Function có thể được gọi từ Store Procedure trong khi Store Procedure không thể được gọi từ Function.

## 5.5. View:

Một `view` là không gì khác ngoài môt lệnh SQL mà được lưu giữ trong Database với một tên liên kết. Một `view` thực sự là một thành phần của một bảng trong form của một truy vấn SQL đã được định nghĩa trước.

Một `view` trong SQL có thể chứa tất cả các hàng của một bảng hoặc các hàng đã được chọn từ một bảng. Một `view` có thể được tạo từ một hoặc nhiều bảng, phụ thuộc vào truy vấn SQL đã viết để tạo một view.

`View` rất hữu dụng khi bạn muốn cho nhiều người người truy cập ở các permission khác nhau.

***Cú pháp***
```
CREATE VIEW ViewName AS
SELECT ...
```
***Mở view***
```
SELECT * FROM ViewName
```

***Chỉnh sửa view***: Cú pháp tương tự như tạo mới View, chỉ thay từ khóa `CREATE` bằng từ khóa `ALTER`

***Xoá View***: `DROP VIEW`

`DROP VIEW ViewName`


## 5.6. IF...ELSE

`IF...ELSE` dùng để thực thi các lệnh có điều kiện, nếu lệnh đúng thì thực thi lệnh đó, nếu sai sẽ thực thi một lệnh khác.

***Cú pháp***:

```
IF <boolean_expression>
BEGIN
<Statement block executes when Boolean expressions is TRUE>
END
ELSE
BEGIN
<Statement block executes when Boolean expressions is FALSE>
END
```

## 5.7. WHILE

Vòng lặp `WHILE (WHILE LOOP)` được sử dụng nếu bạn muốn chạy lặp đi lặp lại một đoạn mã khi điều kiện cho trước trả về giá trị là TRUE.

***Cú pháp:***
```
WHILE condition
BEGIN
   <statements>

   [BREAK] [CONTINUE]
END;
```

**Lưu ý:** Trong vòng lặp WHILE bạn có thể sử dụng BREAK để thoát ra khỏi vòng lặp. Sử dụng lệnh CONTINUE để bỏ qua các dòng lệnh trong khối WHILE và ở bên dưới nó, để tiếp tục một vòng lặp mới.

# 6. Triggers and Rules

`Trigger` trong SQL là stored procedure đặc biệt (không có tham số) được thực thi (execute) một cách tự động khi có một sự kiện thay đổi dữ liệu (data modification) như Insert, Delete, hay Update.

**Phân loại:**

- `DDL (Data Definition Language) trigger:` Loại trigger này kích hoạt khi các sự kiện thay đổi cấu trúc (như tạo, sửa đổi hay loại bỏ bảng). Hoặc trong các sự kiện liên quan đến server như thay đổi bảo mật hoặc sự kiện cập nhật thống kê.

- `DML (Data Modification Language) trigger:` Đây là loại trigger được sử dụng nhiều nhất. Trong trường hợp này, sự kiện kích hoạt là một câu lệnh sửa đổi dữ liệu. Nó có thể là một câu lệnh chèn, cập nhật hoặc xoá trên một bản. 

Ở đây ta chú trọng xem `DML (Data Modification Language) trigger`

**Cú pháp:**

```
CREATE TRIGGER trigger_name  
ON { table_name }   
[ WITH <Options> ]  
{ FOR | AFTER | INSTEAD OF }   
{ [INSERT], [UPDATE] , [DELETE] }
```
- `FOR hoặc AFTER [[INSERT, UPDATE, DELETE]:` Các loại trigger này được thực thi sau khi câu lệnh kích hoạt kết thúc.
- `INSTEAD OF [INSERT, UPDATE, DELETE]:` Trái ngược với FOR (AFTER), trigger INSTEAD OF thực thi thay vì thay cho câu lệnh kích hoạt. 

***Xoá Triggers***:

```
DROP TRIGGER trigger_name
```

***Enable/Disable Triggers***
```
ENABLE/DISABLE trigger_name
{ON table_name | ON DATABASE | ON ALL SERVER}
```

# 7. Indexing

## 7.1. Định nghĩa
`INDEX (hay chỉ mục)` là một cấu trúc dữ liệu để tăng hiệu suất truy vấn của cơ sở dữ liệu. Index cho phép cơ sở dữ liệu thực hiện một số câu truy vấn có điều kiện nhanh hơn so với thông thường. Nhưng index cũng được lưu trên bộ nhớ và tiêu tốn không gian bộ nhớ và thời gian để tạo, cập nhật index nên khi sử dụng index cần phải suy xét kĩ.

-> `INDEX` hiểu cơ bản như trang mục lục trong một cuốn sách. Nếu ta muốn tìm nội dung thay vì xem từng trang sách thì ta có thể trỏ đến mục lục có nội dung cần tìm

`INDEX` giúp tăng tốc các truy vấn SELECT và các mệnh đề WHERE, nhưng nó làm chậm dữ liệu nhập vào, với các câu lệnh UPDATE và INSERT. Users không thể nhìn thấy `INDEX` do chỉ tồn tại trong cột và bảng và giúp tốc độ câu query nhanh hơn.

-> Tạo `INDEX` thuờng ưu tiên cho các column có tần suất search nhiều

## 7.2. Các loại Index
Chia làm 2 loại chính:

- ***Clustered Index***: là một loại chỉ mục sắp xếp các hàng dữ liệu trong bảng trên các giá trị chính của chúng. Trong cơ sở dữ liệu, **chỉ có một Clustered Index** trên mỗi bảng vì bản thân các dòng dữ liệu được lưu trữ và sắp xếp theo thứ tự vật lý dựa trên các cột trong loại Index này.

```
CREATE CLUSTERED INDEX index_name ON dbo.Tblname(Colname1, Colname2...)
```

- ***Non-Clustered Index***: Khác với clustered Index, non-Clustered Index không sắp xếp dữ liệu theo một trật tự vật lý như clustered Index. Mặc định thì primary key là clustered index còn foreign key là non-clustered index, do đó non-clustered index không mang tính duy nhất dữ liệu.

```
CREATE NONCLUSTERED INDEX index_name ON dbo.Tablename(ColumnName1, ColumnName2...)
```

Dựa vào phân loại chính trên ta có các loại Index:

- ***Single-Column Index***: tạo cho duy nhất 1 cột trong bảng

```
CREATE INDEX ten_index
ON ten_bang (ten_cot);
```

- ***Unique Index***: chỉ mục duy nhất, được sử dụng để tăng hiệu suất và đảm bảo tính toàn vẹn dữ liệu. Một chỉ mục duy nhất không cho phép chèn bất kỳ giá trị trùng lặp nào được chèn vào bảng.

```
CREATE UNIQUE INDEX ten_index
ON ten_bang (ten_cot);
```

- ***Composite Index***: chỉ mục kết hợp dành cho hai hoặc nhiều cột trong một bảng

```
CREATE INDEX ten_index
ON ten_bang (cot1, cot2);
```
- ***Implicit Index***: chỉ mục mà được tạo tự động bởi Database Server khi một bảng được tạo. Các Index ngầm định được tạo tự động cho các ràng buộc Primary key và các ràng buộc Unique.

## 7.3. Một số chú ý:

- Không nên sử dụng trong các bảng nhỏ, ít bản ghi.
- Không nên sử dụng Index trong bảng mà các hoạt động UPDATE, INSERT xảy ra thường xuyên với tần suất lớn.
- Tiêu chí chọn trường Index:
  - Kích thước nhỏ: với clustered index tốt nhất là một trường kiểu số nguyên (INT hoặc BIGINT), lý tưởng nhất là tạo Clustered Index trên cột có thuộc tính Unique và khác Null.
  - Trường luôn tăng: Khi giá trị mới của trường clustered index luôn tăng lên, bản ghi mới luôn được thêm vào cuối hạn chế tình trạng phân mảnh dữ liệu.
  - Trường tĩnh: Clustered index không nên bị cập nhật thường xuyên, giá trị của nó nên được giữ nguyên. Khi nó bị cập nhật, cả clustered index và nonclustered index cần được cập nhật để sắp xếp vào vị trí mới cho đúng thứ tự dẫn đến tình trạng Index bị phân mảnh
  - Tính duy nhất : Các giá trị trong một cột có tác động đến hiệu suất của Index, càng nhiều giá trị trùng lặp việc đọc từng bản ghi trở nên tốn kém hơn là quét bảng (table scan). Vì thế khi thấy độ selectivity thấp, bộ Optimizer sẽ tự động bỏ qua không dùng Index.

# 8. Partitioning

## 8.1. Định nghĩa
`Table partitioning` là kỹ thuật phân chia bảng thành từng đoạn nhằm quản lý hiệu quả cơ sở dữ liệu với dung lượng lớn, cung cấp 1 phương pháp khác để chia dữ liệu những bảng lớn và trỏ tới những vùng nhỏ hơn. 

Bằng phương pháp đó, nó tạo ra một phiên bản quản trị cơ sở dữ liệu dễ dàng hơn khi back up (sao lưu), loading (nạp dữ liệu), phục hồi (recovery) và truy vấn dữ liệu (query data)

![Partitioning](https://images.viblo.asia/f5be0c42-9baf-4dfb-b24d-78fed3b73264.gif)

Với những bảng dữ liệu chứa vài trăm triệu bản ghi thường xuyên được cập nhật, các tác vụ như backup/restore, hoặc create/rebuild index đều rất tốn kém thời gian:

-> Mỗi lần truy vấn DB engine phải duyệt qua toàn bộ bảng để lấy data 

-> Tạo ra vấn đề về performance khi bản ghi trong table quá lớn 

-> Sử dụng Table Partitioning lấy data tại vùng nhất định thay vì toàn bộ table như trước đây.

## 8.2. Vertical Partitioning and Horizontal Partitioning

- ***Vertical Partitioning (Phân vùng dọc):***  Chia table theo các row - bản ghi. các bản ghi matching theo điều kiện partition function mà được assign vào các partition tương ứng khác nhau.

- ***Horizontal Partitioning (Phân vùng dọc):***  Chia table theo các column.

## 8.3. Syntax

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
(create_definition,...)
[table_options]
[partition_options]
```

## 8.4. Type of Table Partitioning

### 8.4.1. Range Partition

 `Range Partition` phân vùng theo khoảng mà bạn muốn sử dụng, tức là chia table ra thành nhiều khoảng giá trị, các khoảng giá trị này phải liên tiếp và không chồng chéo lên nhau. Ví dụ trong 1 năm bạn có 12 tháng, chúng ta có thể chia thành 12 khoảng liên tiếp nhau.

 `Range partition` sử dụng **VALUE LESS THAN**. Các value phải được liền kề nhau và không được chồng chéo lên nhau và phải mang giá trị **integer** hoặc **NULL**

```
 CREATE TABLE members (
    firstname VARCHAR(25) NOT NULL,
    lastname VARCHAR(25) NOT NULL,
    username VARCHAR(16) NOT NULL,
    email VARCHAR(35),
    joined DATE NOT NULL
)
PARTITION BY RANGE( YEAR(joined) ) (
    PARTITION p0 VALUES LESS THAN (1990),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN (2010),
    PARTITION p3 VALUES LESS THAN (2020),
    PARTITION p4 VALUES LESS THAN MAXVALUE
);
```

**Chú ý**: `Range Partition` còn có thể sử dụng cùng lúc nhiều column

### 8.4.2. List Partition

`List Partition` tương tự như `Range partition` nhưng value để phân vùng đã được defined sẵn với **VALUES IN**.

Value các partition function không được có sự chồng chéo, trường hợp insert với store_id không thuộc bất kì value nào trong tập values thì sẽ báo lỗi.

```
CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    store_id INT
)
PARTITION BY LIST(store_id) (
    PARTITION pNorth VALUES IN (3,5,6,9,17),
    PARTITION pEast VALUES IN (1,2,10,11,19,20),
    PARTITION pWest VALUES IN (4,12,13,14,18),
    PARTITION pCentral VALUES IN (7,8,15,16)
);
```

### 8.4.3. Các loại Table Partitioning khác

- `Columns partitioning`: Phân vùng theo các columns trong bảng

- `Hash partitioning`: Phân vùng một cách tự động dựa vào biếu thức hoặc giá trị **INTEGER** của cột đã đc chọn. Các bản ghi sẽ đc chia đều cho các **Partition** vs số lượng **Partition** đc quyết định bới keyword **Partition** nếu k định nghĩa số lượng **Partition**. thì sẽ default là 1

- `Key partitioning`: Tương tự `Hash Partitioning` nhưng có thể sử dụng 0 hoặc n column để **partition**, các column không nhất thiết phải là **INTEGER**. Trường hợp không truyền column để partition thì ***primary key*** hoặc ***unique key*** sẽ auto được chọn.

- `Subpartitioning` - hay còn được gọi là `Composite Partitioning` là kết hợp các loại partitioning khác nhau đã nói ở trên

## 8.5. Một số lưu ý

- `Table Partitioning` giúp ta tăng performance đáng kế với dữ liệu lớn do thay vì cần tìm kiếm dữ liệu ở toàn bộ table, thì mình chỉ cần tìm kiếm data ở một số partition nhất định dựa trên "quy tắc" đặt ra ban đầu hay còn gọi là **Partition Function**.
- `Partition` nên là lựa chọn cuối cùng khi muốn tối ưu hóa, tức là sau khi đã optimize câu query, sử dụng Index.

- `Partition` sẽ đem lại nhiều ý nghĩa nhất khi dữ liệu của bảng quá to hàng triệu bản ghi. Cụ thể, Table có dung lượng từ 2GB trở lên nên cân nhắc được `Partition`.

- Khi áp dụng `Partition` lên bất kỳ bảng nào thì nên nhớ đến một số hạn chế như: không thể sử dụng khóa ngoại, cẩn thận với khóa chính hay unique.
# 9. Connectors and APIs





