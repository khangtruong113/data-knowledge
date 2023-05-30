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

|Data type   |  Description |Storage
|---|---|
|   |   |
