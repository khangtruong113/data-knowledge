# SQL
SQL viết tắt của Structured Query Language - ngôn ngữ truy vấn cơ sở dữ liệu. Có thể coi SQL là ngôn ngữ chung mà bất cứ hệ thống cơ sở dữ liệu quan hệ (RDBMS) nào cũng phải đáp ứng.
Trong tài liệu này sẽ chủ yếu đề cập MSSQL.

## 1. Installation
Tải về và cài đặt:
- [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)

(Tham khảo [SQL Server installation guide](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16))

## 2. Data Types
![Data Types in SQL Server](https://whatisdbms.com/wp-content/uploads/2020/10/SQL-Server-Data-Types.jpg)

### 2.1. Numeric
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

### 2.2. String
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

### 2.3. Date and Time
| Data type      | Description                                                                                                                                                                                                                   | Storage    |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| datetime       | From January 1, 1753 to December 31, 9999 with an accuracy of 3.33 milliseconds                                                                                                                                               | 8 bytes    |
| datetime2      | From January 1, 0001 to December 31, 9999 with an accuracy of 100 nanoseconds                                                                                                                                                 | 6-8 bytes  |
| smalldatetime  | From January 1, 1900 to June 6, 2079 with an accuracy of 1 minute                                                                                                                                                             | 4 bytes    |
| date           | Store a date only. From January 1, 0001 to December 31, 9999                                                                                                                                                                  | 3 bytes    |
| time           | Store a time only to an accuracy of 100 nanoseconds                                                                                                                                                                           | 3-5 bytes  |
| datetimeoffset | The same as datetime2 with the addition of a time zone offset                                                                                                                                                                 | 8-10 bytes |
| timestamp      | Stores a unique number that gets updated every time a row gets created or modified. The timestamp value is based upon an internal clock and does not correspond to real time. Each table may have only one timestamp variable |            |	 

### 2.4. Others
| Data type       | Description                                                                               |
|:----------------|:------------------------------------------------------------------------------------------|
| sql_variant     | Stores up to 8,000 bytes of data of various data types, except text, ntext, and timestamp |
| uniqueidentifier| Stores a globally unique identifier (GUID)                                                |
| xml             | Stores XML formatted data. Maximum 2GB                                                    |
| cursor          | Stores a reference to a cursor used for database operations                               |
| table           | Stores a result-set for later processing                                                  |

Tham khảo tại [w3schools.com](https://www.w3schools.com/sql/sql_datatypes.asp)

## 3. Basic Statements
![5 Types of SQL Commands](https://cdn.hackr.io/uploads/posts/attachments/16793290212HNSqhy8tE.webp)

### 3.1. Data Definition Language (DDL)
- ```CREATE```: tạo mới database, schema, table, view, function, stored procedure, etc.
- ```DROP```: xóa một đối tượng khỏi cơ sở dữ liệu
- ```ALTER```: thêm, sửa đổi hoặc xóa các cột hoặc các ràng buộc trong một bảng hiện có
- ```TRUNCATE```: xóa tất cả các bản ghi khỏi một bảng, nhưng không xóa chính bảng đó

*```SP_RENAME```: là stored procedure có sẵn trong SQL Server để thay đổi tên cột và tên bảng.

### 3.2. Data Manipulation Language (DML)
- ```INSERT```: thêm một bản ghi mới trong bảng
- ```UPDATE```: sửa đổi các bản ghi hiện có trong một bảng
- ```DELETE```: xóa một hoặc nhiều bản ghi hiện có khỏi một bảng.

### 3.3. Data Control Language (DCL)
- ```GRANT```: cấp quyền truy cập của người dùng hoặc các quyền khác vào cơ sở dữ liệu
- ```REVOKE```: rút hoặc lấy lại một số hoặc tất cả các quyền truy cập của người dùng vào cơ sở dữ liệu được cung cấp bằng cách sử dụng lệnh GRANT.

### 3.4. Transaction Control Language (TCL)
- ```COMMIT```: lưu vĩnh viễn tất cả các thay đổi hoặc transactions vào cơ sở dữ liệu. Sau khi lưu tất cả các thay đổi, COMMIT kết thúc transaction hiện tại và giải phóng các transaction locks
- ```ROLLBACK```: hoàn tác hoặc khôi phục cơ sở dữ liệu về trạng thái đã commit cuối cùng trong trường hợp có lỗi. Sau khi rollback, nó giải phóng các transaction locks
- ```SAVEPOINT```: lưu một giao dịch tạm thời để ta có thể rollback đến một trạng thái hoặc điểm nhất định bất cứ khi nào cần thiết.

### 3.5. Data Query Language (DQL)
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

## 4. Window Functions
__Window Functions__ trong SQL được sử dụng để thực hiện các phép tính các dòng có liên quan đến dòng hiện tại. Khác với __Aggregate Functions__ tính toán tất cả các hàng, Windows Functions được sử dụng để tính toán theo từng hàng.

### 4.1. Cú pháp của Window Functions
    Window Functions () OVER([PARTITION BY clause] [ORDER BY clause] [frame clause])

Trong đó:
- ```PARTITION BY``` clause: dùng để nhóm các hàng có liên quan đến nhau thành 1 partition để thực hiện việc tính toán 
- ```ORDER BY``` clause: giống như ORDER BY nhưng  sẽ sắp xếp các hàng có trong từng partition đó
- frame clause:  giới hạn các hàng trong phân vùng bằng cách điểm bắt đầu và điểm kết thúc trong phân vùng. Frame clause cần được sử dụng đi kèm với ```ORDER BY``` với giá trị mặc định là từ đầu phân vùng đến phần tử hiện tại.

Trong thành phần _frame clause_ cần chú ý đến một số câu lệnh sau:
- ```PRECEDING```: xác định điểm đầu tiên của partition để thực hiện tính toán
  - ```UNBOUNDED PRECEDING```: dòng đầu tiên của partition
  - ```_value_ PRECEDING``` (ex: ```2 PRECEDING```): bắt đầu từ 2 dòng trước đó tính từ dòng hiện tại
- ```CURRENT ROW```: dòng hiện tại đang được xét đến
- ```FOLLOWING```: xác định điểm cuối của partition để thực hiện tính toán
  - ```UNBOUNDED FOLLOWING```: dòng cuối cùng của partition
  - ```_value_ FOLLOWING``` (ex: ```2 FOLLOWING```): tính toán kết thúc 2 dòng sau đó tính từ dòng hiện tại
- ```BETWEEN...AND```: thể hiện khoảng bắt đầu và kết thúc partition để tính toán.

### 4.2. Các loại Window Functions
- __Aggregate Functions__

| Function Name | Mô tả                      |
|:--------------|:---------------------------|
| ```AVG()```   | Trả về giá trị trung bình  |
| ```COUNT()``` | Đếm các giá trị            |
| ```MAX()```   | Trả về giá trị lớn nhất    |
| ```MIN()```   | Trả về giá trị nhỏ nhất    |
| ```SUM()```   | Tính tổng các giá trị      |

- __Ranking Functions__

| Function Name        | Mô tả                                                                                                                                                                                         |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```RANK()```         | Xếp hạng các giá trị theo thứ tự tăng dần nhưng sẽ trả về thứ hạng giống nhau với các giá trị giống nhau và bỏ qua thứ hạng đó.<br/>Ví dụ: rank(): 1,1,3,4,5                                  |
| ```DENSE_RANK()```   | Xếp hạng các giá trị theo thứ tự tăng dần nhưng sẽ trả về thứ hạng giống nhau với các giá trị giống nhau và không bỏ qua thứ hạng đó.<br/>Ví dụ: dense_rank (): 1,1,2,3,4                     |
| ```ROW_NUMBER()```   | Xếp hạng các giá trị trong từng partition theo thứ tự tăng dần mà không quan tâm đến giá trị giống nhau.<br/>Ví dụ: row_number (): 1,2,3,4,5                                                  |
| ```CUME_DIST()```    | Tinh tỷ lệ các giá trị nhỏ hơn hoặc bằng giá trị hiện tại                                                                                                                                     |
| ```PERCENT_RANK()``` | (rank -1)/ (row-1)<br/>Trong đó:<br/>+ rank là thứ tự của giá trị đó theo thứ tự tăng dần (các giá trị giống nhau trả về thứ hạng giống nhau)<br/>+ row: tổng số dòng (xét trong 1 partition) |

- __Analytic Functions__

| Function Name                    | Mô tả                                                                                                                                                                                 |
|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```FIRST_VALUE (expression)```   | Lấy giá trị đầu trong từng partition                                                                                                                                                  |
| ```LAST_VALUE (expression)```    | Lấy giá trị cuối trong từng partition                                                                                                                                                 |
| ```LAG (expression, offset)```   | Sắp xếp các giá trị theo thứ tự tăng dần và trả về các giá trị không bị bỏ qua.<br/>Trong đó: offset: số giá trị bỏ qua tính từ trên xuống (Nếu tham số này bị bỏ qua, mặc định là 1) |
| ```LEAD (expression, offset)```  | Sắp xếp các giá trị theo thứ tự giảm dần và trả về các giá trị không bị bỏ qua.<br/>Trong đó: offset: số giá trị bỏ qua tính từ trên xuống (Nếu tham số này bị bỏ qua, mặc định là 1) |

## 5. Indexing
__Chỉ mục (INDEX)__ trong SQL là bảng tra cứu đặc biệt mà công cụ tìm kiếm cơ sở dữ liệu có thể sử dụng để tăng nhanh thời gian và hiệu suất truy xuất dữ liệu. Hiểu đơn giản, một chỉ mục là một con trỏ chỉ tới từng giá trị xuất hiện trong bảng/cột được đánh chỉ mục. Chỉ mục trong database có ý nghĩa tương tự như các mục trong xuất hiện trong Mục lục của một cuốn sách.

INDEX chứa các keys được tạo từ một hoặc nhiều cột trong table hoặc view. Các keys này được lưu trữ trong cấu trúc (B-tree) cho phép SQL tìm hàng hoặc các hàng được liên kết với các giá trị key một cách nhanh chóng và hiệu quả.

INDEX giúp tăng tốc các truy vấn SELECT chứa các mệnh đề WHERE hoặc ORDER, nhưng nó làm chậm việc dữ liệu nhập vào với các lệnh UPDATE và INSERT. Các chỉ mục có thể được tạo hoặc xóa mà không ảnh hưởng tới dữ liệu.

### 5.1. B-Tree
B-Tree indexes (sau đây gọi là index) là một object có cấu trúc, gồm root - branch - leaf. Tuy nhiên chúng được sắp xếp theo dạng B-Tree (cây nhị phân) để phục vụ cho việc **TÌM KIẾM NHANH**. Nó bao gồm các thông tin sau:

– Index key: chứa các trường dữ liệu làm key khi tạo index<br>
– RowID: là ROWID tương ứng với dòng dữ liệu chứa index key.

- Dữ liệu index được tổ chức và lưu trữ theo dạng tree, tức là có root, branch, leaf.
- B-Tree chia nhỏ DB thành các page với kích thước bằng nhau.
- Truy vấn tìm kiếm trong B-Tree:

![Tìm kiếm 1 key sử dụng B-Tree index](https://b2012345.smushcdn.com/2012345/wp-content/uploads/2020/10/Designing_Data-Intensive_Applications_The_Big_Ideas_Behind_Reliable__Scalable__and_Maintainable_Systems_by_Martin_Kleppmann__z-lib_org__pdf__page_102_of_613_-1024x567.png?lossy=1&strip=1&webp=1)
1 page sẽ được chỉ định làm gốc của B-Tree; bất kể khi nào bạn cần tìm kiếm 1 key trong index, ta đều cần phải bắt đầu từ page này. Mỗi page sẽ chứa nhiều key và cũng có thể chứa cả tham chiếu tới các page con. Mỗi page con sẽ chịu trách nhiệm cho 1 dải key nhất định, được bao ngoài bởi key đứng cạnh nó trong page cha.

Ví dụ với hình minh họa trên, ta đang tìm kiếm key 251, vì vậy ta cần tìm tới tham chiếu nằm giữa key 200 và 300. Từ tham chiếu thu được ta tiếp tục nhảy sang page con đó, và thực hiện lặp lại cho tới khi tìm được tới page lá (page chỉ chứa key, không có page con). Cuối cùng ta sẽ kết luận key 251 có tồn tại trong DB hay không, và nếu có thì giá trị của nó là gì.

Số lượng tham chiếu ở trong mỗi page được coi là 1 tham số cần điều chỉnh tùy vào nhu cầu của ứng dụng và kích thước của ổ đĩa, nó được gọi là branching factor. Ở hình bên trên branching factor là 6, còn thực tế thì nó lên tới con số hàng trăm.

### 5.2. Các kiểu index
- Clustered: Những dòng dữ liệu trong bảng được gom nhóm lại với nhau tạo thành page, một page có kích thước tùy thuộc vào kích thước của mỗi dòng mà chứa được số lượng tương ứng. Các page này __thể hiện đầy đủ dữ liệu__ của bảng và liên kết hai chiều với nhau theo từng cặp nằm cạnh nhau hoặc có thể bất kì khoảng cách nào. Chỉ cần có liên kết là thể hiện được thứ tự của dữ liệu.
  - Trên một bảng chỉ có duy nhất một clustered index
  - Dữ liệu của bảng sẽ được sắp xếp theo thứ tự clustered key
  - Sử dụng cấu trúc B-Tree để tạo ra các cấp độ lưu trữ key hỗ trợ tìm kiếm
  - Index có level càng cao thì việc tìm kiếm càng tốn thời gian hơn
  - Level của index phụ thuộc vào độ lớn dữ liệu trong bảng và kích thước của index key
  
Nhu cầu tìm kiếm dữ liệu của một ứng dụng là đa dạng, vậy nên ta cần nhiều hơn một index để có thể tìm kiếm trên nhiều cột khác nhau. Điều này có thể đạt được bằng cách sử dụng nonclustered index.
- Nonclustered: SQL Server sẽ nhân bản dữ liệu của bảng thành một tập khác gồm các cột đã được tạo nonclustered index rồi thực hiện sắp xếp và tổ chức index theo các cột index cho tập dữ liệu mới này.
  - Dữ liệu trong nonclustered index này được sắp xếp theo thứ tự của cột đã được tạo index, và kích thước chỉ gói gọn trong 1 page. Nếu bạn mang thêm càng nhiều cột khác vào nonclustered index thì kích thước sẽ càng lớn.
  - Mỗi một nonclustered index tạo ra sẽ tốn thêm một vùng không gian đĩa để lưu trữ ngoài kích thước của bảng. Kích thước key và số lượng cột thêm vào index sẽ ảnh hưởng đến kích thước của index và đặc biệt tốn chi phí bảo trì index cho mỗi hành động insert/update/delete.

Ví dụ Clustered & Nonclustered Index:
![Clustered & Nonclustered Index](https://quantricsdulieu.com/wp-content/uploads/2021/10/index_ondisk7-1024x617.png)

### 5.3. Syntax
Tạo clustered index:

    CREATE CLUSTERED INDEX index1 ON database1.schema1.table1 (column1);

Tạo nonclustered index:
    
    CREATE INDEX index1 ON schema1.table1 (column1);

Tạo nonclustered index với unique constraint và chỉ định thứ tự sắp xếp:

    CREATE UNIQUE INDEX index1 ON schema1.table1 (column1 DESC, column2 ASC, column3 DESC);

Đổi tên index:
    
    --Renames the IX_ProductVendor_VendorID index on the Purchasing.ProductVendor table to IX_VendorID.
    
    EXEC sp_rename N'Purchasing.ProductVendor.IX_ProductVendor_VendorID', N'IX_VendorID', N'INDEX';

Xóa index:

    DROP INDEX 
        IX_PurchaseOrderHeader_EmployeeID ON Purchasing.PurchaseOrderHeader,  
        IX_Address_StateProvinceID ON Person.Address;

### 5.4. Một số tips giúp tạo index hiệu quả hơn
- Nên index những cột được dùng trong WHERE, JOIN và ORDER BY
- Dùng thuộc tính NOT NULL cho những cột được index 
- Không dùng index cho các bảng thường xuyên có UPDATE, INSERT 
- Không dùng index cho các cột mà giá trị thường xuyên bị thay đổi
- Dùng câu lệnh EXPLAIN (SQL Server, MySQL), EXPLAIN ANALYZE (Postgres) giúp ta biết được SQL sẽ chạy truy vấn ra sao. Nó thể hiện thứ tự join, các bảng được join như thế nào, thời gian chạy truy vấn. Giúp việc xem xét để viết truy vấn tối ưu, chọn cột để Index dễ dàng hơn.

## 6. Partitioning
Một table bình thường giống như 1 khối dữ liệu khi lưu trên ổ đĩa cứng. Table càng lớn, thì khối dữ liệu cũng càng lớn, khiến cho các truy vấn trên khối dữ liệu đó cũng khó khăn và chậm chạp hơn. Với bài toán này, có 2 cách xử lý chính để tối ưu hóa thời gian truy vấn:
- Đánh index cho bảng dựa trên các cột: Cách này rất hiệu quả nếu dữ liệu cần lấy là nhỏ so với tổng dữ liệu trong bảng. Tuy nhiên, dữ liệu tăng trưởng đến 1 mức độ nào đó, cách xử lý này cũng sẽ giảm dần hiệu quả. (do bản thân index cũng sẽ lớn theo dữ liệu thực sự)
- Chia để trị (hay partitioning): Với cách này, từ 1 khối dữ liệu to ban đầu, chúng ta sẽ chia nhỏ nó ra thành các khối nhỏ hơn, để tiện cho việc quản lý. Hay nói 1 cách khác, chúng ta đã partition bảng ban đầu!

**Partition Table** là 1 bảng đã được chia nhỏ thành các phần (hay các partition) theo 1 cột nào đó trong bảng. Cột được lựa chọn là tiêu chí để chia nhỏ bảng, ta gọi đó là **partition key**.

### 6.1. Khi nào bảng nên được partition?
Trong một số trường hợp, điều kiện lọc dữ liệu không có đủ thông tin để RDBMS lựa chọn partition nào cần quét qua, do đó, partition table trong tình huống này không có tác dụng. 

Dưới đây là 1 số hướng dẫn khi nào nên cân nhắc 1 bảng nên được partition (theo [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/18/vldbg/partition-concepts.html#GUID-E849DE8A-547D-4A2E-9324-706CAF574754)):
- Table có dung lượng từ 2GB trở lên nên cân nhắc được partition. 
- Table có chứa dữ liệu lịch sử. Dữ liệu cũ, ít được sử dụng sẽ đưa vào các partition cũ, những dữ liệu mới sẽ được đưa vào partition mới. 
- Table có nội dung có thể được chia thành các khu vực có mức độ ưu tiên khác nhau (VD: khu vực dành cho dữ liệu thường xuyên được truy vấn,hoặc ít được truy vấn,…)

### 6.2. Tạo partition trong SQL Server
Việc phân đoạn bảng dựa trên hai khái niệm sau đây:
- Partition function: Qui định giá trị biên cho các đoạn. Hệ thống dựa vào hàm này để xác định đoạn mà mỗi bản ghi thuộc vào.
- Partition scheme: Ánh xạ các đoạn khai báo trong partition function vào các filegroup (mỗi đoạn được lưu trữ tại một filegroup).

**PARTITION FUNCTION SYNTAX**

    CREATE PARTITION FUNCTION partition_function_name ( input_parameter_type )  
    AS RANGE [ LEFT | RIGHT ]   
    FOR VALUES ( [ boundary_value [ ,...n ] ] )   
    [ ; ]

**PARTITION FUNCTION SYNTAX**

    CREATE PARTITION SCHEME partition_scheme_name  
    AS PARTITION partition_function_name  
    [ ALL ] TO ( { file_group_name | [ PRIMARY ] } [ ,...n ] )  
    [ ; ]  

_Ví dụ:_

    CREATE PARTITION FUNCTION myRangePF1 (INT)  
    AS RANGE LEFT FOR VALUES (1, 100, 1000);  
    GO  
    CREATE PARTITION SCHEME myRangePS1  
    AS PARTITION myRangePF1  
    TO (test1fg, test2fg, test3fg, test4fg); 

| Filegroup     | Partition | Values                                  |
|:--------------|:----------|:----------------------------------------|
| ```test1fg``` | 1         | col1 <= ```1```                         |
| ```test2fg``` | 2         | col1 > ```1``` AND col1 <= ```100```    |
| ```test3fg``` | 3         | col1 > ```100``` AND col1 <= ```1000``` |
| ```test4fg``` | 4         | col1 > ```1000```                       |

Tham khảo thêm về:
- Cách tạo filegroup và add file vào [filegroup](https://quantrinet.com/forum/showthread.php?t=9931)
- Tạo partition table ở [SQL Server](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-partition-function-transact-sql?view=sql-server-ver16), [MySQL](https://indaacademy.vn/performance-tunning/partition-sql-la-gi/#4_RANGE_PARTITIONING), [PostgreSQL](https://www.postgresql.org/docs/current/ddl-partitioning.html)

## 7. Server-Side Programming


## 8. Triggers and Rules


## 9. Connectors and APIs


## 10. Assignment
