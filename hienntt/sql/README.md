# SQL
SQL viết tắt của Structured Query Language - ngôn ngữ truy vấn cơ sở dữ liệu. Có thể coi SQL là ngôn ngữ chung mà bất cứ hệ thống cơ sở dữ liệu quan hệ (RDBMS) nào cũng phải đáp ứng.
Trong tài liệu này sẽ chủ yếu đề cập MSSQL.

## 1. Installation
Tải về và cài đặt:
- [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)

(Tham khảo [SQL Server installation guide](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16))

## 2. Basic Statements
![5 Types of SQL Commands](https://cdn.hackr.io/uploads/posts/attachments/16793290212HNSqhy8tE.webp)

### 2.1. Data Definition Language (DDL)
- ```CREATE```: tạo mới database, schema, table, view, function, stored procedure, etc.
- ```DROP```: xóa một đối tượng khỏi cơ sở dữ liệu
- ```ALTER```: thêm, sửa đổi hoặc xóa các cột hoặc các ràng buộc trong một bảng hiện có
- ```TRUNCATE```: xóa tất cả các bản ghi khỏi một bảng, nhưng không xóa chính bảng đó

*```SP_RENAME```: là stored procedure có sẵn trong SQL Server để thay đổi tên cột và tên bảng.

### 2.2. Data Manipulation Language (DML)
- ```INSERT```: thêm một bản ghi mới trong bảng
- ```UPDATE```: sửa đổi các bản ghi hiện có trong một bảng
- ```DELETE```: xóa một hoặc nhiều bản ghi hiện có khỏi một bảng.

### 2.3. Data Control Language (DCL)
- ```GRANT```: cấp quyền truy cập của người dùng hoặc các quyền khác vào cơ sở dữ liệu
- ```REVOKE```: rút hoặc lấy lại một số hoặc tất cả các quyền truy cập của người dùng vào cơ sở dữ liệu được cung cấp bằng cách sử dụng lệnh GRANT.

### 2.4. Transaction Control Language (TCL)
- ```COMMIT```: lưu vĩnh viễn tất cả các thay đổi hoặc transactions vào cơ sở dữ liệu. Sau khi lưu tất cả các thay đổi, COMMIT kết thúc transaction hiện tại và giải phóng các transaction locks
- ```ROLLBACK```: hoàn tác hoặc khôi phục cơ sở dữ liệu về trạng thái đã commit cuối cùng trong trường hợp có lỗi. Sau khi rollback, nó giải phóng các transaction locks
- ```SAVEPOINT```: lưu một giao dịch tạm thời để ta có thể rollback đến một trạng thái hoặc điểm nhất định bất cứ khi nào cần thiết.

### 2.5. Data Query Language (DQL)
- ```SELECT```: trích xuất dữ liệu từ CSDL

### Một số câu lệnh SQL cơ bản
| Command                     | Mô tả, ví dụ                                                                                                               |                                              
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| ```SELECT```                | trích xuất dữ liệu: ```SELECT *```, ```SELECT DISTINCT```, ```SELECT INTO```, ```SELECT TOP```                             |
| ```AS```                    | gán tên cho bảng hoặc cột                                                                                                  |
| ```FROM```                  | chỉ ra bảng lấy data                                                                                                       |
| ```WHERE```                 | lọc truy vấn để chỉ trả kết quả phù hợp với điều kiện đã set                                                               |
| ```AND```                   | kết hợp hai hoặc nhiều điều kiện trong một truy vấn, tất cả các điều kiện phải được đáp ứng để trả về kết quả              |
| ```OR```                    | kết hợp hai hoặc nhiều điều kiện trong một truy vấn, chỉ một trong các điều kiện phải được đáp ứng để trả về kết quả       |
| ```BETWEEN```               | lọc truy vấn để chỉ trả lại kết quả phù hợp với một phạm vi đã chỉ định                                                    |
| ```LIKE```                  | tìm kiếm một mẫu cụ thể trong một cột: ```%x```, ```%x%```, ```x%```, ```x%y```, ```_x%```, ```x_%```                      |
| ```IN```                    | chỉ định nhiều giá trị muốn chọn khi sử dụng lệnh WHERE                                                                    |
| ```IS NULL```               | chỉ trả về các hàng có giá trị NULL                                                                                        |
| ```IS NOT NULL```           | chỉ trả về các hàng không có giá trị NULL                                                                                  |
| ```COUNT```,```SUM```, etc. | aggregate functions                                                                                                        |
| ```GROUP BY```              | nhóm các rows có cùng giá trị thành các summary rows                                                                       |
| ```HAVING```                | giống ```WHERE``` nhưng áp dụng với aggregate functions                                                                    |
| ```ORDER BY```              | set thứ tự của kết quả trả về: ```ASC``` - tăng dần, ```DESC```: giảm dần                                                  |
| ```JOIN```                  | kết hợp các data từ hai hoặc nhiều bảng: ```INNER JOIN```, ```LEFT JOIN```, ```RIGHT JOIN```, ```FULL JOIN```              |
| ```UNION```                 | kết hợp 2 bộ kết quả từ 2 hoặc nhiều lệnh ```SELECT``` và loại bỏ dòng trùng lặp, ```UNION ALL``` không loại bỏ dòng trùng |

## 3. Data Types
![Data Types in SQL Server](https://whatisdbms.com/wp-content/uploads/2020/10/SQL-Server-Data-Types.jpg)

### 3.1. Numeric
![SQL Numeric Data Type](https://learnsql.com/blog/ms-sql-server-data-types/1.png)

| Data type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                               | Storage      |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| bit          | Integer that can be 0, 1, or NULL                                                                                                                                                                                                                                                                                                                                                                                                         |              |	 
| tinyint      | Allows whole numbers from 0 to 255                                                                                                                                                                                                                                                                                                                                                                                                        | 1 byte       |
| smallint     | Allows whole numbers between -32,768 and 32,767                                                                                                                                                                                                                                                                                                                                                                                           | 2 bytes      |
| int          | Allows whole numbers between -2,147,483,648 and 2,147,483,647                                                                                                                                                                                                                                                                                                                                                                             | 4 bytes      |
| bigint       | Allows whole numbers between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807                                                                                                                                                                                                                                                                                                                                                     | 8 bytes      |
| decimal(p,s) | Fixed precision and scale numbers. Allows numbers from -10^38 +1 to 10^38 –1.<br/>The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18.<br/>The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0         | 5-17 bytes   |
| numeric(p,s) | Fixed precision and scale numbers. Allows numbers from -10^38 +1 to 10^38 –1.<br/>The p parameter indicates the maximum total number of digits that can be stored (both to the left and to the right of the decimal point). p must be a value from 1 to 38. Default is 18.<br/>The s parameter indicates the maximum number of digits stored to the right of the decimal point. s must be a value from 0 to p. Default value is 0         | 5-17 bytes   |
| smallmoney   | Monetary data from -214,748.3648 to 214,748.3647                                                                                                                                                                                                                                                                                                                                                                                          | 4 bytes      |
| money        | Monetary data from -922,337,203,685,477.5808 to 922,337,203,685,477.5807                                                                                                                                                                                                                                                                                                                                                                  | 8 bytes      |
| float(n)     | Floating precision number data from -1.79E + 308 to 1.79E + 308.<br/>The n parameter indicates whether the field should hold 4 or 8 bytes. float(24) holds a 4-byte field and float(53) holds an 8-byte field. Default value of n is 53.                                                                                                                                                                                                       | 4 or 8 bytes |
| real         | Floating precision number data from -3.40E + 38 to 3.40E + 38                                                                                                                                                                                                                                                                                                                                                                             | 4 bytes      |

### 3.2. String
| Data type      | Description                     | Max size                 | Storage                   |
|:---------------|:--------------------------------|:-------------------------|:--------------------------|
| char(n)        | Fixed width character string    | 8,000 characters         | Defined width             |
| varchar(n)     | Variable width character string | 8,000 characters         | 2 bytes + number of chars |
| varchar(max)   | Variable width character string | 1,073,741,824 characters | 2 bytes + number of chars |
| text           | Variable width character string | 2GB of text data         | 4 bytes + number of chars |
| nchar          | Fixed width Unicode string      | 4,000 characters         | Defined width x 2         |
| nvarchar       | Variable width Unicode string   | 4,000 characters         |                           |	 
| nvarchar(max)  | Variable width Unicode string   | 536,870,912 characters   |                           | 
| ntext          | Variable width Unicode string   | 2GB of text data         |                           |	 
| binary(n)      | Fixed width binary string       | 8,000 bytes              |                           |
| varbinary      | Variable width binary string    | 8,000 bytes              |                           |
| varbinary(max) | Variable width binary string    | 2GB                      |                           |
| image          | Variable width binary string    | 2GB                      |                           |

### 3.3. Date and Time
| Data type      | Description                                                                                                                                                                                                                   | Storage    |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| datetime       | From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds                                                                                                                                               | 8 bytes    |
| datetime2      | From January 1, 0001 to December 31, 9999 with an accuracy of 100 nanoseconds                                                                                                                                                 | 6-8 bytes  |
| smalldatetime  | From January 1, 1900 to June 6, 2079 with an accuracy of 1 minute                                                                                                                                                             | 4 bytes    |
| date           | Store a date only. From January 1, 0001 to December 31, 9999                                                                                                                                                                  | 3 bytes    |
| time           | Store a time only to an accuracy of 100 nanoseconds                                                                                                                                                                           | 3-5 bytes  |
| datetimeoffset | The same as datetime2 with the addition of a time zone offset                                                                                                                                                                 | 8-10 bytes |
| timestamp      | Stores a unique number that gets updated every time a row gets created or modified. The timestamp value is based upon an internal clock and does not correspond to real time. Each table may have only one timestamp variable |            |	 

### 3.4. Others
| Data type       | Description                                                                               |
|:----------------|:------------------------------------------------------------------------------------------|
| sql_variant     | Stores up to 8,000 bytes of data of various data types, except text, ntext, and timestamp |
| uniqueidentifier| Stores a globally unique identifier (GUID)                                                |
| xml             | Stores XML formatted data. Maximum 2GB                                                    |
| cursor          | Stores a reference to a cursor used for database operations                               |
| table           | Stores a result-set for later processing                                                  |

Tham khảo tại [w3schools.com](https://www.w3schools.com/sql/sql_datatypes.asp)

## 4. Indexing
__Chỉ mục (INDEX)__ trong SQL là bảng tra cứu đặc biệt mà công cụ tìm kiếm cơ sở dữ liệu có thể sử dụng để tăng nhanh thời gian và hiệu suất truy xuất dữ liệu.

Hiểu đơn giản, một chỉ mục là một con trỏ chỉ tới từng giá trị xuất hiện trong bảng/cột được đánh chỉ mục. Chỉ mục trong database có ý nghĩa tương tự như các mục trong xuất hiện trong Mục lục của một cuốn sách.

INDEX chứa các keys được tạo từ một hoặc nhiều cột trong table hoặc view. Các keys này được lưu trữ trong cấu trúc (B-tree) cho phép SQL tìm hàng hoặc các hàng được liên kết với các giá trị key một cách nhanh chóng và hiệu quả.

INDEX giúp tăng tốc các truy vấn SELECT chứa các mệnh đề WHERE hoặc ORDER, nhưng nó làm chậm việc dữ liệu nhập vào với các lệnh UPDATE và INSERT. Các chỉ mục có thể được tạo hoặc xóa mà không ảnh hưởng tới dữ liệu.



## 5. Window Functions
__Window Functions__ trong SQL được sử dụng để thực hiện các phép tính các dòng có liên quan đến dòng hiện tại. Khác với __Aggregate Functions__ tính toán tất cả các hàng, Windows Functions được sử dụng để tính toán theo từng hàng.

### 5.1. Cú pháp của Window Functions
    Window Functions () OVER([PARTITION BY clause] [ORDER BY clause] [frame clause])

Trong đó:
- PARTITION BY clause: dùng để nhóm các hàng có liên quan đến nhau thành 1 partition để thực hiện việc tính toán 
- ORDER BY clause: giống như ORDER BY nhưng  sẽ sắp xếp các hàng có trong từng partition đó
- frame clause:  giới hạn các hàng trong phân vùng bằng cách điểm bắt đầu và điểm kết thúc trong phân vùng. Frame_clause cần được sử dụng đi kèm với ORDER BY với giá trị mặc định là từ đầu phân vùng đến phần tử hiện tại.

Trong thành phần _frame clause_ cần chú ý đến một số câu lệnh sau:
- PRECEDING: xác định điểm đầu tiên của partition để thực hiện tính toán
  - UNBOUNDED PRECEDING: dòng đầu tiên của partition
  - _value_ PRECEDING (ex: 2 preceding): bắt đầu từ 2 dòng trước đó tính từ dòng hiện tại
- CURRENT ROW: dòng hiện tại đang được xét đến
- FOLLOWING: xác định điểm cuối của partition để thực hiện tính toán
  - UNBOUNDED FOLLOWING: dòng cuối cùng của partition
  - _value_ FOLLOWING (ex: 2 FOLLOWING): tính toán kết thúc 2 dòng sau đó tính từ dòng hiện tại
- BETWEEN...AND: thể hiện khoảng bắt đầu và kết thúc partition để tính toán.

### 5.2. Các loại Window Functions
- __Aggregate Functions__

| Function Name | Mô tả                                                                                                                                                                                         |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AVG()         | Trả về giá trị trung bình                                                                                                                                                                     |
| COUNT()       | Đếm các giá trị                                                                                                                                                                               |
| MAX()         | Trả về giá trị lớn nhất                                                                                                                                                                       |
| MIN()         | Trả về giá trị nhỏ nhất                                                                                                                                                                       |
| SUM()         | Tính tổng các giá trị                                                                                                                                                                         |

- __Ranking Functions__

| Function Name  | Mô tả                                                                                                                                                                                         |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RANK()         | Xếp hạng các giá trị theo thứ tự tăng dần nhưng sẽ trả về thứ hạng giống nhau với các giá trị giống nhau và bỏ qua thứ hạng đó.<br/>Ví dụ: rank(): 1,1,3,4,5                                  |
| DENSE_RANK()   | Xếp hạng các giá trị theo thứ tự tăng dần nhưng sẽ trả về thứ hạng giống nhau với các giá trị giống nhau và không bỏ qua thứ hạng đó.<br/>Ví dụ: dense_rank (): 1,1,2,3,4                     |
| ROW_NUMBER()   | Xếp hạng các giá trị trong từng partition theo thứ tự tăng dần mà không quan tâm đến giá trị giống nhau.<br/>Ví dụ: row_number (): 1,2,3,4,5                                                  |
| CUME_DIST()    | Tinh tỷ lệ các giá trị nhỏ hơn hoặc bằng giá trị hiện tại                                                                                                                                     |
| PERCENT_RANK() | (rank -1)/ (row-1)<br/>Trong đó:<br/>+ rank là thứ tự của giá trị đó theo thứ tự tăng dần (các giá trị giống nhau trả về thứ hạng giống nhau)<br/>+ row: tổng số dòng (xét trong 1 partition) |

- __Analytic Functions__

| Function Name             | Mô tả                                                                                                                                                                                 |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIRST_VALUE (expression)  | Lấy giá trị đầu trong từng partition                                                                                                                                                  |
| LAST_VALUE (expression)   | Lấy giá trị cuối trong từng partition                                                                                                                                                 |
| LAG (expression, offset)  | Sắp xếp các giá trị theo thứ tự tăng dần và trả về các giá trị không bị bỏ qua.<br/>Trong đó: offset: số giá trị bỏ qua tính từ trên xuống (Nếu tham số này bị bỏ qua, mặc định là 1) |
| LEAD (expression, offset) | Sắp xếp các giá trị theo thứ tự giảm dần và trả về các giá trị không bị bỏ qua.<br/>Trong đó: offset: số giá trị bỏ qua tính từ trên xuống (Nếu tham số này bị bỏ qua, mặc định là 1) |

## 6. Server-Side Programming

## 7. Triggers and Rules

## 8. Partitioning

## 9. Connectors and APIs

## 10. Assignment
