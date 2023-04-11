# Table of Contents
1. [Database Normalization](#DatabaseNormalization)
2. [ACID/BASE](#ACID/BASE)
3. [OLTP và OLAP](#third-example)
4. [CAP](#CAP)
5. [Basic Statements](#Statements)
6. [Cách SQL server hoạt động](#SQLWork)
7. [SQL server on Linux](#SQLLinux)
9. [KEY](#Key)
10. [Truy Van](#TruyVan)
11. [SQL Server Configuration](#Config)
12. [Instance database](#Instance)
13. [Cấu trúc lưu trữ dữ liệu](#Files)
14. [Concurrency](#concurrency)
8. [Function](#Function)
8. [Stored PRocedure](#StoredProcedure)
8. [VIEW](#View)
8. [Trigger](#Trigger)
8. [Index](#index)
8. [Partition](#partition)
8. [Logs](#logs)
8. [SQL Server Agent & Schedule a job](#Agent)

## **Database Normalization** <a name="DatabaseNormalization"></a>

Chuẩn hóa DB nhắm **giảm** thiểu sự **dư thừa dữ liệu** và loại **bỏ** các **bất thường** khi cập nhật DB

### Chuẩn 1 (1NF – First Normal Form): 
 
- **Giá trị** được lưu trữ trong các **ô** phải là các giá trị đơn (không phải là một danh sách) **(scalar value)**
- trong bảng **không có cột nào lặp lại**.

### Chuẩn 2 (2NF – Second Normal Form): 

- Mọi **trường không phải khóa** phải **phụ thuộc vào khóa chính**.

### Chuẩn 3 (3NF – Third Normal Form): 

- Mọi *trường không phải khóa* **_chỉ_** *phụ thuộc vào khóa chính*.

### Các bước chuẩn hóa:

1. Đưa bảng về chuẩn 1:

- Chia dữ liệu thành đơn vị nhỏ nhất

- Loại bỏ các trường lặp lại

2. Đưa bảng về chuẩn 2:

- Đưa bảng về chuẩn 1

- Tách các trường không phụ thuộc vào khóa chính ra bảng riêng

3. Đưa bảng về chuẩn 3:

- Đưa bảng về chuẩn 2

- Tách các trường không phụ thuộc hoàn toàn khóa chính ra bảng riêng

## **ACID/BASE** <a name="ACID/BASE"></a>

**ACID** (*Atomicity, Consistency, Isolation, Durability): tập hợp các thuộc tính mà 1 transaction thao tác với database phải đạt được nhằm bảo đảm tính toàn vẹn, hợp lệ, an toàn, bền vững của dữ liệu ở database

- Atomicity (Tính nguyên tử): Một giao dịch có nhiều thao tác khác biệt thì hoặc là toàn bộ các thao tác hoặc là không một thao tác nào được hoàn thành.

- Consistency (Tính nhất quán): Một giao dịch hoặc là sẽ tạo ra một trạng thái mới và hợp lệ cho dữ liệu, hoặc trong trường hợp có lỗi sẽ chuyển toàn bộ dữ liệu về trạng thái trước khi thực thi giao dịch 

- Isolation (Tính cô lập): Một giao dịch đang thực thi và chưa được xác nhận phải bảo đảm tách biệt khỏi các giao dịch khác.

- Durability (Tính bền bỉ): Dữ liệu được xác nhận sẽ được hệ thống lưu lại sao cho ngay cả trong trường hợp hỏng hóc hoặc có lỗi hệ thống, dữ liệu vẫn đảm bảo trong trạng thái chuẩn xác

**BASE**

Mô hình BASE được xây dựng để tạo ra tính linh hoạt tối đa

- Basic Availability – Tính sẵn sàng ở mức cơ bản: Trong khi cơ sở dữ liệu đảm bảo tính khả dụng cho dữ liệu, cơ sở dữ liệu có thể không nhận được dữ liệu được yêu cầu, dữ liệu có thể ở trạng thái thay đổi hoặc không nhất quán.

- Soft state – Trạng thái mềm: Trạng thái của cơ sở dữ liệu có thể thay đổi theo thời gian.

- Eventual consistency – Tính nhất quán: Cơ sở dữ liệu sẽ trở nên nhất quán và dữ liệu sẽ được lan truyền khắp mọi nơi tại một thời điểm nào đó trong tương lai.

## **OLTP và OLAP** <a name="OLTP&OLAP"></a>

|OLTP - Online transaction processing| OLAP - Online analytical processing|
|------------------------------------|-------------------------------------|
|Sử dụng cho lưu trữ thông tin thông thường|Sử dụng cho Big data|
|Lưu trữ bằng các bảng theo mô hình quan hệ|Lưu trữ bằng các bảng nhiều chiều (rubic)|
|Phục vụ lưu trữ, giao dịch và cập nhật định kỳ cho OLAP|Phục vụ cho phân tích, khai thác nhằm phát triển các tiềm năng kinh doanh|

## **CAP Theorem** <a name="CAP"></a>

**CAP** (consistency, availability, partition tolerance): hệ thống phân tán *chỉ có thể cung cấp hai trong ba* đặc tính mong muốn

- Consistency (tính nhất quán): tại cùng một thời điểm, dữ liệu mà tất cả các máy khách nhìn thấy phải là giống nhau, bất kể nó kết nối với node nào. Để điều này xảy ra, bất cứ khi nào dữ liệu được ghi vào một node, nó phải được chuyển tiếp hoặc sao chép ngay lập tức tới tất cả các node khác trong hệ thống trước khi việc ghi được coi là "thành công".

- Availability (tính khả dụng): bất kỳ máy khách nào đưa ra yêu cầu dữ liệu đều nhận được phản hồi, ngay cả khi một hoặc nhiều node bị ngừng hoạt động

- Partition tolerance (tính dung sai phân vùng): Phân vùng là sự đứt gãy liên lạc trong hệ thống phân tán, hay cụ thể hơn, là việc kết nối giữa hai node bị mất hoặc tạm thời bị trì hoãn. Dung sai phân vùng có nghĩa là cluster phải duy trì được trạng thái hoạt động dù cho có bất kỳ sự cố giao tiếp nào giữa các node trong hệ thống

## **Horizonal scaling & vertical scaling** <a name="Scaling"></a>

- **_Scaling_**: khả năng một tài nguyên CNTT có thể xử lý các demands khi tăng/giảm

- **Vertical scaling**: cách mở rộng server hiện tại bằng cách nâng cấp độ mạnh (power) (nâng cấp CPU, Ram, Storage, v.V…), thường bị giới hạn bởi vượt quá khả năng về cấu hình vật lý hiện đại hay độ trễ khi “chẳng may” Server bị downtime để nâng cấp hay deploy hệ thống
![Vertical scaling] (https://images.viblo.asia/6d815dd4-9f85-4bc3-a124-5b72943354ce.png)

- **Horizonal scaling**: cách mở rộng bằng cách thêm nhiều Node/Server vào một mạng lưới đang có, làm tăng khả năng chịu tải có hệ thống. Cách làm này rẻ và dễ làm hơn so với Vertical-scaling, đặc biệt là rất dễ dàng downsize cũng như upsize hệ thống
![Horizonal scaling] (https://images.viblo.asia/a9d75909-56d1-4ccc-a564-9c2f8afba120.png)

*So sánh Vertical scaling và Horizonal scaling 
![Vertical & Horizonal scaling] (https://topdev.vn/blog/wp-content/uploads/2020/12/scaling-1.png)

## **MSSQL: Basic Statements** <a name="Statements"></a>
### Trên cơ sở dữ liệu:

*Mỗi Database chỉ tồn tại với một **TÊN DUY NHẤT**, không trùng lặp với tên các Database sẳn có (không phân biệt chữ viết hoa và viết thường)*

- Tạo cơ sở dữ liệu: 

```create database [ten database]```

- Xóa cơ sở dữ liệu:

```drop database [ten data muon xoa]```

- Sửa các thông tin của cơ sở dữ liệu:

```alter database [ten DB muốn sửa] [nội dung sửa]```

- Đổi tên Database:

```RENAME DATABASE ten_cu TO ten_moi```

hoặc:

```ALTER DATABASE ten_cu MODIFY NAME = ten_moi  ``` 
### Trên table:

*Mỗi table chỉ có một tên duy nhất trong Database*

*Mỗi column chỉ có một tên duy nhất trong table*
- Tạo table:

      CREATE TABLE <Tên Table>
        (
            <Tên trường 1> <Kiểu dữ liệu>,
            <Tên trường 2> <Kiểu dữ liệu>,
            <Tên trường n> <Kiểu dữ liệu>
        )
 - Chỉnh sửa table:

``` ALTER TABLE [noi dung chinh sua]```

 --Thêm column NGAYSINH có kiểu dữ liệu DATE vào Table dbo.GiangVien

    ALTER TABLE dbo.GiangVien ADD NGAYSINH DATE
    GO

--Chỉnh sửa kiểu dữ liệu của column MASV trong Table dbo.GiangVien:

    ALTER TABLE dbo.GiangVien
            ALTER COLUMN  MASV CHAR(5)
    GO  

- Xóa table:

```DROP TABLE [ten table]```

- Cập nhật dữ liệu trên table:

       UPDATE <Tên Table>
       SET <thuộc tính 1 = giá trị 1>, <thuộc tính 2 = giá trị 2>,…,<thuộc tính n = giá trị n>,
       WHERE <điều kiện cập nhập>  

- Đổi tên table:

      ALTER TABLE [tên cũ]
      RENAME TO [tên mới]

hoặc:

```RENAME [tên cũ] TO [tên mới]```

### Trên record

- Thêm record:

      INSERT INTO <Tên Table>
        ( column1, column2, column3, … , columnn, )
      VALUES  (
        Gợi ký nhập dữ liệu, -- Tên column1 – kiểu dữ liệu tương ứng column1
        Gợi ký nhập dữ liệu, -- Tên column2 – kiểu dữ liệu tương ứng column2
        Gợi ký nhập dữ liệu, -- Tên column3 – kiểu dữ liệu tương ứng column3
        …        
          )

- Xóa toàn bộ record trên table:

```TRUNCATE TABLE <Tên TABLE>```

//Không hỗ trợ mệnh đề where 
hoặc:

```DELETE <Tên TABLE>```

//Có hỗ trợ mệnh đề where

## **DATA TYPE** <a name="DataType"></a>

|Kiểu dữ liệu| Mô tả|Minh họa|
|---|---|---|
|Bit|Nhận giá trị 0 hoặc 1|  |
|Int|Kiểu số nguyên| 1, 0, -9, 8, ....|
|Money|Kiểu giá trị tiền tệ|
|Float|Kiểu số thực|-0.5, 1.23, ...|
|Datetime| Kiểu ngày giờ|23/10/2006|
|Time|Lưu trữ giờ, phút, giây|  |
|Char(n)| Kiểu ký tự, không chứa ký tự UNICODE, bộ nhớ cấp phát tĩnh|   |
|Nchar(n)|Kiểu ký tự, có chứa unicode, bộ nhớ cấp phát tĩnh (bao gồm cả ký tự unicode)|   |
|Varchar(n)|Kiểu ký tự,không chứa ký tự UNICODE, bộ nhớ cấp phát động (không vượt quá n)||
|Navarchar(n)|Kiểu ký tự, chứa ký tự UNICODE, bộ nhớ cấp phát động (không vượt quá n)||                     
|Text|Kiểu chuỗi ký tự, không chứa unicode, bộ nhớ cấp phát động theo chiều dài ký tự nhập vào||
|Ntext|Kiểu chuỗi ký tự, chứa unicode, bộ nhớ cấp phát động theo chiều dài ký tự nhập vào||

### Toán tử điều kiện
 - Toán tử logic:

 |Toán tử|Mô tả|
 |---|---|
 |AND|Lọc các dữ liệu thỏa mãn tất cả các vế điều kiện|
 |OR|Lọc dữ liệu thỏa một trong các vế điều kiện|
 |NOT|Lọc dữ liệu khác với dữ liệu thỏa mãn|
 |BETWEEN|Lọc dữ liệu thỏa tập giá trị định sẵn|
 |IN|So sánh một giá trị với một danh sách định sẵn|
 - Toán tử so sánh: <,>,<=,>=,=, <> hoặc != (không bằng, không dùng để so sánh kiểu dữ liệu chuỗi ký tự)

## **Cách SQL server hoạt động** (<a name="SQLWork"></a>)

SQL (Structured Query Language - ngôn ngữ truy vấn dữ liệu). SQL gồm 2 thành phần: biên dịch và thực thi. Trình biên dịch giúp chuyển các câu lệnh thành các thủ tục và máy chạy các thủ tục đó. 


### Cấu trúc của SQL Server
SQL Server bao gồm **5 cơ sở dữ liệu hệ thống** (system databases) và **một hay nhiều user database**. 

Các cơ sở dữ liệu hệ thống bao gồm:

- **Cơ sở dữ liệu Master**: Chứa tất cả những thông tin cấp hệ thống (**system-level information**) bao gồm thông tin về các database khác trong hệ thống như *vị trí của các data files*, các *login account* và các thiết đặt cấu hình hệ thống của SQL Server (*system configuration settings*).
- **Cơ sở dữ liệu Tempdb**: Chứa tất cả những **table** hay **stored procedure** được tạm thời tạo ra trong quá trình làm việc bởi user hay do bản thân SQL Server engine. Các table hay stored procedure này sẽ biến mất khi khởi động lại SQL Server hay khi ta disconnect.
- **Cơ sở dữ liệu Model**: Database này đóng vai trò như một **bảng mẫu (template) cho các database khác**. Nghĩa là khi một user database được tạo ra thì SQL Server sẽ copy toàn bộ các system objects (tables, stored procedures…) từ Model database sang database mới vừa tạo.
- **Cơ sở dữ liệu Msdb**: được sử dụng cho SQL Server Agent để lập lịch các công việc và các cảnh báo (**schedule alerts and jobs**).
- **Cơ sở dữ liệu Resource**: là một CSDL chỉ đọc chứa các object hệ thống  mà được sử dụng trong SQL Server. Các Object hệ thống về mặt vật lý tồn tại trong Resource Database nhưng về mặt logic nó lại xuất lược đồ hệ thống (sys schema) của mỗi cơ sở dữ liệu.

## **SQL server on Linux** (<a name="SQLLinux"></a>)

SQL Server yêu cầu cấu hình tối thiểu 3250 MB Ram.

### Cài đặt SQL Server trên Ubuntu

- Nhập public repository GPG keys
```curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -```
- Đăng ký Microsoft SQL Server Ubuntu repository
```curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-server.list > /etc/apt/sources.list.d/mssql-server.list```
- Cài đặt SQL Server:

      sudo apt-get update
      sudo apt-get install -y mssql-server
- Cấu hình SQL Server:

    ```sudo /opt/mssql/bin/sqlservr-setup```
- Cài đặt xong, kiểm tra nếu SQL Server service đang chạy:

    ```systemctl status mssql-server```

### Kết nối và sử dụng SQL Server với MsSql Tool

Sau khi cài đặt thành công, có thể kết nối SQL Server vNext CTP1 trên Linux thông qua MsSql Tool, bao gồm tiện ích Sqlcmd, Transact-SQL queries để tạo, truy vấn database và bcp để import-export dữ liệu số lượng lớn.

*Lưu ý:*
Sqlcmd chỉ là 1 tool để kết nối SQL server nhằm quản lý và truy vấn dữ liệu. Ngoài ra, có thể sử dụng SQL Server Management và Visual Studio Code.

- Cài đặt MsSql Tool với Ubutun:
   + Nhập GPG keys repository

```curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -```
  + Đăng kí Microsoft Ubuntu repository

```curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list```

  + Cập nhật hệ thống và cài đặt MsSql Tool
     
         sudo apt-get update 
         sudo apt-get install mssql-tools unixodbc-dev

### Kết nối và truy cập dữ liệu SQL Server

Để kết nối SQL Server trên Linux, cần sử dụng SQL Authentication. Với việc kết nối từ xa, cần mở port SQL Server (mặc định là port 1433 qua tcp) trên Firewall.

Nếu thiết lập tường lửa bằng Iptables:

```iptables -A INPUT -p tcp -m tcp --dport 1433 -j ACCEPT```

Nếu thiết lập tường lửa bằng FirewallD:

       sudo firewall-cmd --zone=public --add-port=1433/tcp --permanent
       sudo firewall-cmd --reload

Kết nối SQL Server qua sqlcmd với các thông số về SQL Server name (-S), username (-U) và password (-P):

```sqlcmd -S localhost -U SA -P 'YourPassword'```

Để kết nối từ xa, chỉ định tên máy hoặc IP cho thông số -S, ví dụ

```sqlcmd -S localhost -U SA -P 'YourPassword'```
 
## **KEY** (<a name="Key"></a>)

 ### Khóa chính (primary key)

 - Là một/ một nhóm trường thuộc tính định danh cho Table: 

    + Chứa các giá trị không rỗng (NOT NULL)
    
    + Chỉ tồn tại dữ liệu duy nhất, không trùng lặp.

- Thông qua khóa chính của Table, các Table khác có thể tham chiếu tới bằng Khóa ngoại (foreign key)

- Các ràng buộc:

|Ràng buộc|Công dụng|
|--------|----|
|Unique|Dữ liệu nhập vào là duy nhất, không trùng lặp|
|Not Null|Column không để trống (không nhận giá trị rỗng)|
|Default|Đặt giá trị mặc định trong trường hợp không có giá trị chỉ định được nhập vào|
|Check|Đảm bảo dữ liệu nhập vào thỏa điều kiện cụ thể|
|Identify|Tạo dãy tăng liên tục cho column|

- Tạo khóa chính trong quá trình khai báo column:

      CREATE TABLE <Tên Table>
        (
           <column1> <kiểu dữ liệu> PRIMARY KEY,
           <column2> <kiểu dữ liệu>,
            …
           <columnn> <kiểu dữ liệu>
        )

- Tạo khóa chính sau khi khai báo tất cả các column:

      CREATE TABLE <Tên Table>
       (
            <column1> <kiểu dữ liệu>,
            <column2> <kiểu dữ liệu>,
            ...
            <columnn> <kiểu dữ liệu>
            PRIMARY KEY (columnKey1, columnKey2…, columnKeyn)
        )

- Tạo khóa chính cho table có sẵn:

```ALTER TABLE <Tên Table> ADD PRIMARY KEY(column1,column2,…columnn)```

- Đặt tên cho khóa chính:

```CONSTRAINT PK_<Tên Table> PRIMARY KEY (ColumnKey1, ColumnKey2,…, ColumnKeyn)```

- Xóa khóa chính có đặt tên:

```ALTER TABLE <Tên Table> DROP CONSTRAINT <Tên Khóa chính>```

### Khóa ngoại

- Các table trong một database không tồn tại độc lập mà còn có mối quan hệ mật thiết với nhau về mặt dữ liệu. Mối quan hệ này được thể hiện thông qua ràng buộc giá trị dữ liệu xuất hiện ở bảng này phải có xuất hiện trước trong một bảng khác. Khóa ngoại khi tham chiếu đến khóa chính của table khác cần có các ràng buộc sau:

  +  UNIQUE, NOT NULL
  + Khóa ngoại phải có cùng kiểu dữ liệu, cùng số lượng trường có sắp xếp tương ứng khóa chính

- Tạo khóa ngoại khi tạo bảng:

      CREATE TABLE <Table Foreign>
          (          
           …
           FOREIGN KEY (<ColumnF, ColumnF1, ColumnF2,…>)
           REFERENCES <Table Key> (<ColumnK, ColumnK1, ColumnK2,…>)
          )


- Tạo khóa ngoại sau khi tạo bảng:

      ALTER TABLE <Table Foreign>
      ADD FOREIGN KEY(<ColumnF, ColumnF1, ColumnF2,…>) 
      REFERENCES <Table Key> (<ColumnK, ColumnK1, ColumnK2,…>)

- Đặt tên cho khóa ngoại:

      ALTER TABLE <Table Foreign>
      ADD CONSTRAINT <Tên khóa ngoại>
      FOREIGN KEY(<ColumnF, ColumnF1, ColumnF2,…>) 
      REFERENCES <Table Key> (<ColumnK, ColumnK1, ColumnK2,…>)

- Hủy khóa ngoại:

```ALTER TABLE <Table Foreign> DROP CONSTRAINT <Tên khóa ngoại>```

## **TRUY VẤN** (<a name="TruyVan"></a>)

- Truy vấn cơ bản:

      SELECT [tính chất] <danh sách column>
      FROM <danh sách Table/Query>

Trong đó:

   [tính chất] có thể là một trong các từ khóa:

     + * (Lấy tất cả dữ liệu), 
     + DISTINCT(lấy dữ liệu không trùng lặp), 
     + TOP<n> (lấy dữ liệu thứ n đầu tiên)

   <danh sách column> tên các bảng cột cần hiển thị ở kết quả truy vấn

- Truy vấn có điều kiện:

      SELECT [tính chất] <danh sách column>
      FROM <danh sách Table/Query>
      WHERE <điều kiện>

- Truy vấn thời gian:

```YEAR(<date>)```

-- để lấy ra năm của ngày <date>

```GETDATE()```

-- lấy ra ngày hiện tại

- Đếm số lượng:

      SELECT COUNT(<Tên column>)
      FROM <Tên table>
      WHERE <Điều kiện>

- Tính trung bình:

      SELECT AVG (<Tên column>)
      FROM <Tên table>
      WHERE <Điều kiện>
    
- Tính tổng:

      SELECT SUM (<Tên column>)
      FROM <Tên table>
      WHERE <Điều kiện>

- Tìm kiếm gần đúng bằng hàm LIKE:

      SELECT [tính chất] <danh sách column>
      FROM <danh sách Table/Query>
      WHERE <column> LIKE <dữ liệu mẫu>

Một số dạng tìm kiếm gần đúng:
|Dạng tìm kiếm|Mệnh đề where|
|---|---|
|Tìm kiếm dữ liệu bắt đầu bằng ký tự K|…WHERE <column> LIKE ‘K%’|
| Tìm kiếm dữ liệu kết thúc bằng ký tự K|…WHERE <column> LIKE ‘%K’|
| Tìm kiếm dữ liệu có chứa ký tự K ở vị trí bất kỳ|	
…WHERE <column> LIKE ‘%K%’|
| Tìm kiếm dữ liêu có ký tự K ở vị trí thứ hai|…WHERE <column> LIKE ‘_K%’|
|Tìm kiếm dữ liệu bắt đầu bằng ký tự K, và có ít nhất có chiều dài là 3 ký tự|…WHERE <column> LIKE ‘K_%_%’|
|Tìm kiếm dữ liệu bắt đầu bằng ký tự K, kết thúc bằng ký tự m|…WHERE <column> LIKE ‘K%m’|

### INNER JOIN

- Kết quả phép toán giao các tập hợp: kết quả trả về là tập hợp tất cả dữ liệu chung thông qua điều kiện kết hợp hai bảng

      SELECT <Danh sách column>
      FROM <Table A>
      INNER JOIN <Table B> ON <điều kiện join B>
      INNER JOIN <Table C> ON <điều kiện join C>….

### FULL OUTER JOIN

- Kết quả phép toán hợp các tập hợp: kết quả trả về là tập hợp tất cả dữ liệu chung và riêng giữa thông qua điều kiện kết hợp hai bảng

      SELECT <Danh sách column>
      FROM <Table A> FULL OUTER JOIN <Table B>
      ON <Điều kiện kết hợp AB>

### LEFT - RIGHT JOIN

- A LEFT JOIN B:
  + Các dữ liệu chung chính là truy vấn INNER JOIN trên hai bảng.
  + Các dữ liệu riêng của bảng A mà không có giá trị trùng khớp ở bảng B, thì các trường thuộc tính của bảng B trong kết quả trả về mặc định là NULL.
  + Không hiển thị các dữ liệu riêng chỉ tồn tại ở bảng B mà không tồn tại ở bảng A.

        SELECT <Danh sách column>
        FROM <Table A>  LEFT | RIGHT  JOIN <Table B>
        ON <Điều kiện kết hợp AB>

### UNION
- kết hợp tập hợp kết quả của hai hoặc nhiều câu lệnh SELECT. Mỗi câu lệnh SELECT với UNION phải có cùng số lượng cột, các cột phải có cùng kiểu dữ liệu, các cột trong mỗi câu lệnh SELECT phải có cùng trật tự.

      SELECT tên cột FROM bảng1
      UNION
      SELECT tên cột FROM bảng2
      --Trả về kết quả kết hợp 2 câu lệnh select (các giá trị trùng nhau chỉ được trả về 1 lần)

      SELECT tên cột FROM bảng1
      UNION
      SELECT tên cột FROM bảng2
      --Trả về kết quả kết hợp 2 câu lệnh select (trả về cả các giá trị trùng nhau)

### SELECT INTO

để tạo bảng từ 1 bảng sẵn có bằng cách sao chép các cột từ bảng ban đầu

      SELECT 
         select_list
      INTO 
         destination
      FROM 
         source
      [WHERE condition]

### GROUP BY
sắp xếp các hàng của truy vấn theo nhóm

      SELECT [column]
      FROM [table]
      WHERE [ dieu_kien ]
      GROUP BY [column]

### AUTO_INCREMENT
Tăng giá trị tự động, mặc định bắt đầu từ 1

## **SQL Server Configuration** (<a name="Config"></a>)

Bạn có thể quản lý và tối ưu hóa tài nguyên SQL Server thông qua các tùy chọn cấu hình bằng cách sử dụng SQL Server Management Studio hoặc sp_configure system stored procedure. 

Các tùy chọn **cấu hình** máy chủ được **sử dụng phổ biến nhất** có sẵn thông qua ***SQL Server Management Studio***; **Tất cả** các tùy chọn **cấu hình** có thể truy cập được thông qua ***sp_configure***

**Các loại tùy chọn cấu hình**

Nếu bạn không thấy hiệu ứng của thay đổi cấu hình, có thể nó chưa được cài đặt. Hãy kiểm tra xem Run_Value của tùy chọn cấu hình đã thay đổi.

- Self-configuring là các tùy chọn mà SQL Server điều chỉnh theo nhu cầu của hệ thống. Trong hầu hết các trường hợp, điều này giúp loại bỏ nhu cầu thiết lập các giá trị theo cách thủ công.

Câu lệnh xác định xem cấu hình đã được install chưa:

      SELECT *
      FROM sys.configurations
      WHERE [value] <> [value_in_use];

Nếu giá trị là thay đổi cho tùy chọn cấu hình bạn đã thực hiện nhưng value_in_use không giống nhau, thì lệnh RECONFIGURE không được chạy hoặc đã thất bại hoặc công cụ cơ sở dữ liệu phải được khởi động lại.

Có hai option cấu hình mà value và value_in_use không giống nhau:

- max server memory (MB) - Giá trị được định cấu hình mặc định là 0  sẽ là 2147483647 trong cột value_in_use.

- min server memory (MB) - Giá trị được định cấu hình là 0 có thể được hiển thị là 8 (32-bit systems), hoặc 16 (64-bit systems) trong cột value_in_use. Trong một vài trường hợp, nếu cột value_in_use shows hiển thị 0, giá trị thật của value_in_use là 8 (32-bit) hoặc 16 (64-bit).

Cột is_dynamic được sử dụng để xác định xem configuration option có cần restart. 

+ Nếu giá trị là 1: khi lệnh RECONFIGURE chạy, giá trị mới sẽ ảnh hưởng ngay lập tức. Trong một vài trường hợp Database Engine có thể không đánh giá giá trị mới ngay lập tức nhưng sẽ làm như vậy trong quá trình thực hiện bình thường của nó. 
+ Nếu giá trị là 0: Giá trị cấu hình đã thay đổi sẽ không có hiệu lực cho đến khi
Database Engine được restarted, kể cả khi RECONFIGURE đã được chạy.

Đối với tùy chọn cấu hình không động, không có cách nào để biết liệu lệnh Reconfigure có được chạy để áp dụng thay đổi cấu hình hay không. Trước khi bạn khởi động lại SQL Server để áp dụng thay đổi cấu hình, hãy chạy lệnhReconfigure để đảm bảo tất cả các thay đổi cấu hình sẽ có hiệu lực khi SQL Server khởi động lại tiếp theo.

### **Tùy chọn cấu hình**

Bảng sau liệt kê tất cả các tùy chọn cấu hình có sẵn, phạm vi của các cài đặt có thể và các giá trị mặc định. Tùy chọn cấu hình được đánh dấu bằng mã chữ cái như sau:

- A (Advance option): Tùy chọn nâng cao, chỉ được thay đổi bởi quản trị viên cơ sở dữ liệu có kinh nghiệm hoặc SQL Server Professional được chứng nhận và yêu cầu thiết lập *show advanced options* hiển thị thành 1.

- RR: Tùy chọn yêu cầu khởi động lại Database Engine.

- RP: Tùy chọn yêu cầu khởi động lại Database EnginePolyBase Engine.

- SC: Self-configuring options.

### **Xem hoặc thay đổi Thuộc tính Server (SQL Server)**

Khi sử dụng *sp_configure*, bạn cũng phải chạy RECONFIGURE hoặc RECONFIGURE WITH OVERRIDE sau khi cài đặt một configuration option. ECONFIGURE WITH OVERRIDE thường được dành riêng cho các tùy chọn cấu hình nên được sử dụng một cách thận trọng. Tuy nhiên, RECONFIGURE WITH OVERRIDE hoạt động với configuration options, có thể sử dụng để thay thế RECONFIGURE.

*Server-Level roles*

Thực hiện các quyền trên sp_configure không có tham số hoặc chỉ có tham số đầu tiên được cấp cho tất cả người dùng theo mặc định. Để thực thi sp_configure với cả hai tham số để thay đổi tùy chọn cấu hình hoặc để chạy câu lệnh Reconfigure, người dùng phải được cấp quyền ALTER SETTINGS server-level. Quyền ALTER SETTINGS server-level được giữ hoàn toàn bởi các vai trò máy chủ cố định của Sysadmin và ServerAdmin.

Để xem hoặc thay đổi thuộc tính Server:

**SQL Server Management Studio**

1. Trong Object Explorer, click phải server, sau đó click Properties.

2. Trong hộp thoại Server Properties, click a page để xem hoặc thay đổi thông tin về page. Một vài thuộc tính ở chế độ read-only.

**Transact-SQL**

Để xem server properties bằng cách sử dụng SERVERPROPERTY built-in function

1. Connect to the Database Engine.

2. Từ Standard bar, click New Query.

Ví dụ: Sử dụng SERVERPROPERTY built-in function trong câu lệnh SELECT để trả về thông tin server hiện tại. Cách này được sử dụng khi có nhiều instances của SQL Server được cài đặt trên Windows-based server, và client phải mở một kết nối khác đến cùng một instance được sử dụng bởi kết nối hiện tại.

      SELECT CONVERT( sysname, SERVERPROPERTY('servername'));  
      GO  

**sys.servers catalog view**

1. Connect to the Database Engine.

2. From the Standard bar, click New Query.

3. Copy và paste ví dụ dưới đây vào query window và click Execute. Sử dụng sys.servers catalog view để trả về tên (name) và ID (server_id) của server hiện tại, và tên của OLE DB provider (provider) để kết nối với một máy chủ được liên kết.

      USE AdventureWorks2012;   
      GO  
      SELECT name, server_id, provider  
      FROM sys.servers ;   
      GO  

**sys.configurations catalog view**

1. Connect to the Database Engine.

2. From the Standard bar, select New Query.

3. Copy và paste ví dụ dưới đây vào query window và click Execute. Sử dụng các truy vấn the sys.configurations catalog view để trả về thông tin tùy chọn server configuration trên server hiệ tại. Ví dụ trả về tên (name) và mô tả (description) của tùy chọn, its value (value), và thông tin xem đó có phải tùy chọn nâng cao (A) (is_advanced).

      SELECT name, description, value, is_advanced  
      FROM sys.configurations;   
      GO  

**sp_configure change a server property**

1. Connect to the Database Engine.

2. From the Standard bar, select New Query.

3. Copy và paste ví dụ dưới đây vào query window và click Execute. Ví dụ dưới đây cho thấy các sử dụng sp_configure để thay đổi server property. Ví dụ thay đổi giá trị của fill factor option thành 100. Server cần phải được restart trước khi những thay đổi có hiệu lực.

      sp_configure 'show advanced options', 1;  
      GO  
      RECONFIGURE;  
      GO  
      sp_configure 'fill factor', 100;  
      GO  
      RECONFIGURE;  
      GO  

**SQL Server Configuration Manager**

Một số propertise của server có thể được xem hoặc thay đổi bằng cách sử dụng TSQL Server Configuration Manager. Ví dụ: bạn có thể xem version và edition của instance của SQL Server hoặc thay đổi vị trí nơi lưu trữ các log file. Các propertise này cũng có thể được xem bằng cách truy vấn Server-Related Dynamic Management Views và function.

1. On the Start menu, point to All Programs, point to Microsoft SQL Server, point to Configuration Tools, and then click SQL Server Configuration Manager.

2. In SQL Server Configuration Manager, select SQL Server Services.

3. In the details pane, right-click SQL Server (<instancename>), and then select Properties.

4. In the SQL Server (<instancename>) Properties dialog box, change the server properties on the Service tab or the Advanced tab, and then select OK.

### **Server memories**

- Việc sử dụng bộ nhớ cho SQL Server Database Engine được giới hạn bởi một cặp cài đặt cấu hình, min server memory (MB) và max server memory (MB).

Bất cứ lúc nào cũng có thể cấu hình lại giới hạn bộ nhớ (tính bằng megabytes) cho một quy trình SQL Server được sử dụng bởi một instance thông qua tùy chọn min server memory (MB) và max server memory (MB).

Cài đặt mặc định và các giá trị cho phép tối thiểu cho các tùy chọn này:

Option	|Mặc định	|Giá trị nhỏ nhất cho phép | khuyến cáo|
|----|----|----|---|
|min server memory (MB)|	0|	0|	0|
|max server memory (MB)|	2,147,483,647 megabytes (MB)|	128 MB|75% bộ nhớ hệ thống có sẵn không được tiêu thụ bởi các quy trình khác, bao gồm các instance khác. |

Trong các giới hạn này, SQL Server có thể thay đổi các yêu cầu bộ nhớ của mình dựa trên các tài nguyên hệ thống có sẵn:

- Cài đặt giá trị bộ nhớ Max Server (MB) quá cao có thể khiến một single instance của SQL Server cạnh tranh về bộ nhớ với các instance khác được lưu trữ trên cùng một máy chủ.

- Cài đặt bộ nhớ Max (MB) quá thấp có thể khiến hiệu suất bị mất, gây ra các vấn đề về bộ nhớ và hiệu suất trong instance.

- Cài đặt Bộ nhớ Max Server (MB) đến giá trị tối thiểu thậm chí có thể ngăn SQL Server khởi động. Nếu bạn không thể start SQL Server sau khi thay đổi tùy chọn này, hãy khởi động nó bằng tùy chọn start -f và đặt lại Bộ nhớ Max Server (MB) thành giá trị trước đó của nó.

- Không nên đặt bộ nhớ Max Server (MB) và Bộ nhớ Min Server (MB) cùng một giá trị hoặc gần cùng một giá trị.

**Min Server Memory:** để đảm bảo bộ nhớ tối thiểu có sắn cho SQL Server Memory Manager.

**Max server memory:** Để đảm bảo HĐH và các ứng dụng khác không gặp phải áp lực bộ nhớ bất lợi đến từ SQL Server.

**Thông tin giá trị đang được cấu hình:**

    SELECT [name], [value], [value_in_use]
    FROM sys.configurations
    WHERE [name] = 'max server memory (MB)' OR [name] = 'min server memory (MB)';

**Cài đặt tùy chọn thủ công**

- Sử dụng Transact-SQL:

Tùy chọn Min server memory (MB) và max server memory (MB) đề là tùy chọn nâng cao. Khi sử dụng stored procedure hệ thống: sp_configure system  để thay đổi những cài đặt trên, cần phải thiết lập giá trị tùy chọn advanced thành 1, sau đó restart server

      sp_configure 'show advanced options', 1;
      GO
      RECONFIGURE;
      GO
      sp_configure 'max server memory', [Max_server_memory_value];
      GO
      RECONFIGURE;
      GO

- Sử dụng SQL Server Management Studio:

1. In Object Explorer, right-click a server and select Properties.

2. Select the Memory page of the Server Properties window. The current values of Minimum server memory and Maximum server memory are displayed.

3. In Server memory options, enter desired numbers for Minimum server memory and Maximum server memory.

### **Configure a Server to Listen on a Specific TCP Port**

Sử dụng SQL Server Configuration Manager

Nếu được bật, instance mặc định của SQL Server Database Engine lắng nghe trên cổng TCP 1433

Để gán số cổng TCP/IP cho  SQL Server Database Engine:

1. In **SQL Server Configuration Manager**, in the console pane, expand **SQL Server Network Configuration**, select Protocols for <instance name>, and then in the right pane double-click **TCP/IP**.

2. In the **TCP/IP Properties dialog box**, on the **IP Addresses** tab, several IP addresses appear in the format IP1, IP2, up to IPAll. One of these is for the IP address of the loopback adapter, 127.0.0.1. Additional IP addresses appear for each IP Address on the computer. (You will probably see both IP version 4 and IP version 6 addresses.) Right-click each address, and then click **Properties** to identify the IP address that you want to configure.

3. If the TCP Dynamic Ports dialog box contains 0, indicating the Database Engine is listening on dynamic ports, delete the 0.

4. In the IPn Properties area box, in the **TCP Port box**, **type the port number** you want this IP address to listen on, and then click **OK**. Multiple ports may be specified by separating them with a comma. Select OK.

5.In the console pane, click **SQL Server Services**.

6. In the details pane, **right-click SQL Server** (<instance name>) and then click **Restart**, to stop and restart SQL Server.

**Connecting**

Sau khi cấu hình SQL Server để lắng nghe một port cụt thể, có 3 cách để kết nối với port đó:

1. Run the SQL Server Browser service on the server để kết nối tới the Database Engine instance bằng tên.
2. Tạo alias trên client, cụ thể port number.
3. Program the client để kết nối sử dụng custom connection string.

### **Start/stop the Database Engine**

**Using SQL Server Configuration Manager**

1. Click Start, point to All Programs, point to Microsoft SQL Server, point to Configuration Tools, and then click **SQL Server Configuration Manager**.

2. In SQL Server Configuration Manager, on the **left pane**, click **SQL Server Services**. The right pane lists several services that are related to SQL Server. If the Database Engine is installed, the Database Engine service is listed as SQL Server (MSSQLSERVER) if it is the default instance; or SQL Server (<instance_name>), if the Database Engine is installed as a named instance. Unless the instance name is changed, SQL Server Express installs as a named instance with the name SQLEXPRESS. A green triangle icon indicates that the Database Engine is running. A red square icon indicates that the Database Engine is stopped.

3. To start/stop the Database Engine, in the **right pane**, **right-click** the **Database Engine**, and then click **Start/Stop**.

**Using command promt**

- Start the default instance of the Database Engine: 

```net start "SQL Server (MSSQLSERVER)"```

hoặc:

```net start MSSQLSERVER```

- Start a named instance of the Database Engine:

```net start "SQL Server (instancename)"```

hoặc:

```net start MSSQL$instancename```

- With startup options:

```net start "SQL Server (MSSQLSERVER)" /f /m```

hoặc:

```net start MSSQLSERVER /f /m```

List of Startup Options

*Default*
|Option|Mô tả|
|-----|----|
|-d <br> master_file_path|	Path for the master database file (typically, C:\Program Files\Microsoft SQL Server\MSSQL.n\MSSQL\Data\master.mdf)|
|-e <br> error_log_path|	Path for the error log file (typically, C:\Program Files\Microsoft SQL Server\MSSQL.n\MSSQL\LOG\ERRORLOG)|
|-l <br> master_log_path|	Path for the master database log file (typically C:\Program Files\Microsoft SQL Server\MSSQL.n\MSSQL\Data\mastlog.ldf)|

*Others*

|Option|Mô tả|
|-----|----|
|-c|	Shortens startup time when starting SQL Server from the command prompt. Because the SQL Server Database Engine does not start as a service when starting from the command prompt, use -c to skip this step.|
|-f|	Starts an instance of SQL Server with minimal configuration. Starting SQL Server in minimal configuration mode places SQL Server in single-user mode|
|-m|	Starts an instance of SQL Server in single-user mode. When you start an instance of SQL Server in single-user mode, only a single user can connect, and the CHECKPOINT process is not started|
|-s|	Start a named instance of SQL Server. Without the -s parameter set, the default instance will try to start|
|-E|	Increases the number of extents that are allocated for each file in a filegroup.This option is not supported in 32-bit releases of SQL Server|
|[See more](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/database-engine-service-startup-options?view=sql-server-ver16)||

- Stop the Database Engine using Transact-SQL:

  + Đợi các câu lệnh Transact-SQL hiện đang chạy và các quy trình được lưu trữ để hoàn thành, sau đó dừng Database Engine, thực hiện câu lệnh sau:

  ```SHUTDOWN;```

  + Dừng Database Engine ngay lập tức:

  ```SHUTDOWN WITH NOWAIT;```

### **Tạo user mới với quyền được chỉ định**

Thêm user mới vào database hiện tại:

**1. Users based on logins in master (kiểu user phổ biến nhất)**

User based on a login using SQL Server authentication

```CREATE USER [user_name];```

    CREATE USER user_name   
    [   
        { FOR | FROM } LOGIN login_name   
    ]  
    [ WITH <limited_options_list> [ ,... ] ]   
    [ ; ]

**2. Users that authenticate at the database (giúp database portable hơn)**

Always allowed in SQL Database. Only allowed in a contained database in SQL Server.

- User based on a Windows user that has no login

```CREATE USER [Contoso\Fritz];```

     CREATE USER   
    {  
      windows_principal [ WITH <options_list> [ ,... ] ]  
    | user_name WITH PASSWORD = 'password' [ , <options_list> [ ,... ]   
    | Azure_Active_Directory_principal FROM EXTERNAL PROVIDER
    }  
    [ ; ] 

- User based on a Windows group that has no login. 

```CREATE USER [Contoso\Sales];```

    CREATE USER   
    {   
          windows_principal [ { FOR | FROM } LOGIN windows_principal ]  
        | user_name { FOR | FROM } LOGIN windows_principal  
    }  
    [ WITH <limited_options_list> [ ,... ] ]   
    [ ; ]  

- Contained database user with password. 

 ```CREATE USER [user_name] WITH PASSWORD = '********';```

***Thông số***

**user_name**: Specifies the name by which the user is identified inside this database. 

-  a **sysname**. 
- can be up to **128 characters** long. 

*When creating a user based on a Windows principal, the Windows principal name becomes the user name unless another user name is specified.*

**LOGIN login_name**
Specifies the login for which the database user is being created. 

- must be **a valid login in the server**. 

- Can be a login based on a **Windows principal** (user or group), a login using **SQL Server authentication**, or a login using an Azure AD principal (user, group, or application). 

When this SQL Server login enters the database, it acquires the name and ID of the database user that is being created. When creating a login mapped from a Windows principal, use the format [<domainName>\<loginName>]. 

**PASSWORD = 'password'**: Specifies the password for the user that is being created

- only be used in a **contained database**. 

**3. Users that cannot authenticate (Những user này không thể đăng nhập vào SQL Server hoặc SQL Database)**

- User without a login. Cannot login but can be granted permissions. 

```CREATE USER [user_name] WITHOUT LOGIN;```

- User based on a certificate. Cannot login but can be granted permissions and can sign modules. 

```CREATE USER [user_name] FOR CERTIFICATE CarnationProduction50;```

- User based on an asymmetric key. Cannot login but can be granted permissions and can sign modules. 

```CREATE User [user_name] FROM ASYMMETRIC KEY PacificSales09;```

## **Instance database** (<a name="Instance"></a>)

Một instance của Database Engine là một **copy** của **SQLServr.exe** thực thi chạy như một **operating system service**. Mỗi instance quản lý một số system database và một hoặc nhiều user database. Mỗi máy tính có thể chạy nhiều instance của Database Engine. Các application kết nối với instance để thực hiện công việc trong cơ sở dữ liệu được quản lý bởi instance.

![instance](https://dangvinhcuong.files.wordpress.com/2015/04/mc3a1y-che1bba7-pc1.jpeg?w=676&h=532&zoom=2)

Một instance của Database Engine hoạt động như một service **xử lý** tất cả các **application request** để làm việc với dữ liệu trong bất kỳ cơ sở dữ liệu nào được quản lý bởi instance đó. Đây là mục tiêu của các yêu cầu kết nối (login) từ applications. Kết nối chạy qua network connection nếu application và instance nằm trên các máy tính riêng biệt. Nếu application và instance nằm trên cùng một máy tính, kết nối SQL Server có thể chạy dưới dạng network connection hoặc in-memory connection. Khi một kết nối đã được hoàn thành, một application sẽ gửi các câu lệnh Transact-SQL qua kết nối với instance. Instance giải quyết các câu lệnh Transact-SQL thành các hoạt động đối với dữ liệu và đối tượng trong cơ sở dữ liệu và nếu các quyền bắt buộc đã được cấp cho thông tin đăng nhập, thực hiện công việc. Bất kỳ dữ liệu nào được truy xuất đều được trả lại cho application, cùng với bất kỳ tin nhắn nào như lỗi.

Bạn có thể chạy nhiều instance của Database Engine trên máy tính. Một instance có thể là instance mặc định. Instance mặc định không có tên. Nếu một yêu cầu kết nối chỉ định tên của máy tính, kết nối được thực hiện theo instance mặc định. Một instance được đặt tên là một instance mà bạn chỉ định tên instance khi cài đặt instance. Yêu cầu kết nối phải chỉ định cả tên máy tính và tên instance để kết nối với instance. Không có yêu cầu để cài đặt một instance mặc định; Tất cả các instance chạy trên máy tính có thể được đặt tên là các instances.

### Cấu hình Database Engine Instances

Mỗi instance của Database Engine phải được cấu hình để đáp ứng các yêu cầu về hiệu suất và tính khả dụng được xác định cho cơ sở dữ liệu được lưu trữ bởi instance. Database Engine bao gồm các tùy chọn cấu hình kiểm soát các hành vi như resource usage và tính khả dụng của các tính năng như auditing hoặc trigger recursion.

![instance](https://virtual-dba.com/wp-content/uploads/Instances_of_SQL_Server.jpg)
Khi cơ sở dữ liệu được deploy, thường có Thỏa thuận cấp dịch vụ (service level agreement -SLA) xác định các khu vực như mức hiệu suất cần thiết từ cơ sở dữ liệu và mức độ sẵn có của cơ sở dữ liệu. Các điều khoản của SLA thường thúc đẩy các yêu cầu cấu hình cho instance.

Một instance thường được cấu hình ngay sau khi nó được cài đặt. Cấu hình ban đầu thường được xác định bởi các yêu cầu SLA của các loại cơ sở dữ liệu được lên kế hoạch để được triển khai theo instance. Sau khi cơ sở dữ liệu đã được triển khai, các quản trị viên cơ sở dữ liệu giám sát hiệu suất của instance và điều chỉnh cài đặt cấu hình khi cần thiết nếu số liệu hiệu suất hiển thị instance không đáp ứng các yêu cầu SLA.

### Log In to an Instance of SQL Server (Command Prompt)

- log in to the default instance of SQL Server, From Command Promt:

```sqlcmd [ /E ] [ /S servername ]```

- log in to a named instance of SQL Server:

```sqlcmd [ /E ] /S servername\instancename  ```

### Configure Database Engine Instances (SQL Server)

- Xem hoặc thay đổi vị trí mặc định cho các tệp cơ sở dữ liệu (databse files):

1. In Object Explorer, right-click on your server and click Properties.

2. In the left panel on that Properties page, click the Database settings tab.

3. In Database default locations, view the current default locations for new data files and new log files. To change a default location, enter a new default pathname in the Data or Log field, or click the browse button to find and select a pathname.

*Lưu ý:* Sau khi thay đổi các vị trí mặc định, bạn phải dừng và restart SQL Server để hoàn thành thay đổi.

## **Cấu trúc lưu trữ dữ liệu** (<a name="Files"></a>)

### Cấu trúc vật lý của một CSDL SQL Server

Mỗi một database trong SQL Server đều chứa ít nhất một **data file chính** (primary), có thể có thêm một hay nhiều **data file phụ**(Secondary) và một **transaction log file**.

- Primary data file (.mdf) : chứa data và những system tables.

- Secondary data file (.ndf) : chỉ sử dụng khi database được phân chia để chứa trên nhiều dĩa.

- Transaction log file (.ldf) : file ghi lại tất cả những thay đổi diễn ra trong một database và chứa đầy đủ thông tin để có thể roll back hay roll forward khi cần.

Data trong SQL Server được chứa thành từng Page 8KB và 8 page liên tục tạo thành một Extent.

![database](https://timoday.edu.vn/wp-content/uploads/2016/12/ViTriLuuTruCSDL.gif)

Trước khi lưu data vào một table, cần phải dành riêng một khoảng trống trong data file cho table đó. Những khoảng trống đó chính là các extents. Có 2 loại Extents: 
- Mixed Extents (loại hỗn hợp) dùng để chứa data của nhiều tables trong cùng một Extent 
- Uniform Extent (loại thuần nhất) dùng để chứa data của một table. 

Ðầu tiên SQL Server dành các Page trong Mixed Extent để chứa data cho một table sau đó khi data tăng trưởng thì SQL dành hẳn một Uniform Extent cho table đó.

**Hoạt động của Transaction Log**:

Đầu tiên *khi có một sự thay đổi dữ liệu* như Insert, Update, Delete được yêu cầu từ các ứng dụng, SQL Server sẽ tải *(load) data page* tương ứng  vào  bộ nhớ (vùng bộ nhớ này gọi là *data cache*), sau đó dữ liệu trong data cache được thay đổi (những trang bị thay đổi còn gọi là *dirty-page*). 

Tiếp theo mọi sự *thay đổi* đều được *ghi* vào *transaction log file* cho nên người ta gọi là write-ahead log. Cuối cùng thì một quá trình gọi là *Check Point Process* sẽ kiểm tra và viết tất cả những transaction đã được hoàn tất (commited) vào đĩa cứng (*flushing the page*).

![transction log](https://timoday.edu.vn/wp-content/uploads/2016/12/CachLuuTransactionLog.gif)

### Cấu trúc lưu trữ dữ liệu

**Database** gồm nhiều **filegroup**, mỗi filegroup sẽ có một hoặc nhiều **data files**, mỗi data file gồm nhiều **data pages**, mỗi data page sẽ có một hoặc nhiều **rows** tùy theo kích thước của mỗi row.

Cơ sở dữ liệu quan hệ (relational database) lưu trữ dữ liệu của người dùng dưới dạng hàng cột (bảng). Mỗi **bảng** có thể có **một hoặc nhiều cột** và mỗi cột phải thuộc về một kiểu dữ liệu nào đó. Mỗi dòng (**row**) sẽ có giá trị cho từng cột. Kích thước của một row chính là tổng kích thước các kiểu dữ liệu của các cột cộng với một số bytes phát sinh của việc tổ chức lưu trữ trong SQL Server.

Những rows này sẽ được gom lại thành các đơn vị lớn hơn gọi là page. Mỗi **page** có kích thước cố định là **8KB** ( 8192 bytes) và các page này nằm liên tiếp trên các data files. Nhằm mục đích hỗ trợ việc cấp phát không gian lưu trữ cho các bảng hiệu quả hơn SQL Server sử dụng đơn vị extent – một **extent** gồm **8 data pages** nằm kế nhau hình thành một khối 64KB. Vậy có thể hình dung các cấp trong việc tổ lưu trữ SQL Server gồm ***database -> filegroups -> files -> extents -> pages -> rows***
![extent](https://quantricsdulieu.com/wp-content/uploads/2021/04/data_page_data_row_01.png)

 ### Data page

 Mỗi page được định vị bằng địa chỉ **FileID:PageID**. Mỗi page hoặc là thuộc về một bảng nào đó (có thể là user hoặc system tables) hoặc là page của hệ thống, như dùng để quản lý việc cấp phát không gian lưu trữ. 
 ![data page](https://quantricsdulieu.com/wp-content/uploads/2021/04/data_pages_2.png)

 **Page header** là **nơi chứa thông tin quản lý** như đề cập ở trên, vùng này chiếm cố định *96 bytes*. Tiếp đến là **payload** – vùng chứa **data rows** và phía dưới cùng là **slot array** – *mảng các phần tử 2 bytes* **chỉ vị trí bắt đầu các rows trong page**. Số lượng phần tử này tương ứng với số lượng rows và thứ tự của chúng phản ánh thứ tự các rows trong index theo key. Vị trí các data rows trong payload không quan trọng, thứ tự của slot quyết định vị trí của chúng trong index.

Để lấy danh sách các pages mà một bảng (clustered/heap table) hoặc một index có thể có

```DBCC IND(<database_name>,<table_name>,<index_id>)```

### File
Cơ sở dữ liệu có 3 loại file:
+ Primary (file dữ liệu chính): điểm bắt đầu của cơ sở dữ liệu và trỏ đến các file khác trong cơ sở dữ liệu. Mỗi cơ sở dữ liệu có một Primary
+ Secondary (file dữ liệu phụ): Một cơ sở dữ liệu có thể có nhiều hoặc chỉ có một file dữ liệu phụ
+ Log (file nhật ký): giữ tất cả thông tin được sử dụng để phục hồi cơ sở dữ liệu. Cơ sở dữ liệu phải có ít nhất một file log. Chúng ta có thể có nhiều file log cho một cơ sở dữ liệu.

Vị trí của tất cả các file trong cơ sở dữ liệu được ghi lại trong cả cơ sở dữ liệu tổng thể và file Primary của cơ sở dữ liệu. Trong hầu hết trường hợp, công cụ cơ sở dữ liệu sử dụng vị trí file từ cơ sở dữ liệu tổng thể.

File có 2 tên là Logical và Physical. Logical được sử dụng để tham chiếu đến file trong tất cả các lệnh T-SQL. Tên Physical là OS_file_name, nó phải tuân theo quy tắc của hệ điều hành. File dữ liệu và file log có thể được đặt trên hệ thống file FAT hoặc NTFS, nhưng không thể đặt trên các hệ thống file nén. Có thể có tối đa 32.767 file trong một cơ sở dữ liệu.

### File Group

Các file cơ sở dữ liệu có thể nhóm lại với nhau thành các file group để phân bổ và quản lý theo mục đích. Một file chỉ có thể là thành viên của một file group. Các file log không thể nhóm vào File Group vì dung lượng file log được quản lý riêng biệt với dung lượng dữ liệu.

Có hai loại File Group trong SQL Server là:
+ Primary: chứa các file dữ liệu chính và bất kỳ file nào không được gán cụ thể cho File Group khác. Tất cả các trang cho bảng hệ thống được cấp phát trong Primary
+ User-defined: các nhóm file do người dùng định nghĩa, nó được chỉ định bằng cách sử dụng từ khóa file group trong lệnh tạo cơ sở dữ liệu hoặc xóa cơ sở dữ liệu.

Một File Group trong mỗi cơ sở dữ liệu hoạt động như nhóm file mặc định. Khi SQL Server chỉ định một trang cho bảng hoặc chỉ mục (không nằm trong File Group nào khi tạo) thì trang đó sẽ nằm trong file group mặc định. Để chuyển đổi file group mặc định từ File Group này sang File Group khác, cần có db_owner fixed database role.

## **Concurrency** (<a name="concurrency"></a>)

Concurrency là khả năng của hai transaction sử dụng cùng một dữ liệu cùng một lúc, đề cập đến các kỹ thuật khác nhau được sử dụng để **duy trì tính toàn vẹn của database** khi **nhiều người dùng cập nhật các rows cùng một lúc**.

Ví dụ: 

Giả sử một ứng dụng thực thi câu lệnh SELECT * FROM Orders. SQLFetchSroll để sroll tập kết quả và cho phép user cập nhật, xóa hoặc thêm orders. Sau khi user cập nhật, xóa hoặc thêm một order, application commit giao dịch.

Nếu mức độ cô lập là Repeatable Read, transaction có thể - tùy thuộc vào cách thực hiện - khóa mỗi hàng được trả về bởi sqlfetchscroll. Nếu mức độ cô lập là Serializable, transaction có thể khóa toàn bộ bảng Orders. Trong cả hai trường hợp, transaction chỉ release khóa của nó khi nó được commit hoặc rolled back. Vì vậy, nếu user dành nhiều thời gian để đọc đơn order và rất ít thời gian cập nhật, xóa hoặc chèn chúng, transaction có thể dễ dàng khóa một số lượng lớn orderes, khiến chúng không available cho user khác.

**Concurrency problem**

Vấn đề chủ yếu phát sinh khi cả hai người dùng cố gắng viết cùng một dữ liệu hoặc khi một người đang viết và người kia đang đọc. Ngoài logic này, còn có một số loại vấn đề đồng thời phổ biến:

- **Dirty Read**: xảy ra khi 1 transaction A đọc 1 row khi nó đang được update bởi 1 transaction B khác và chưa được commit. Transaction A sẽ đọc dữ liệu vẫn chưa được commit. Ví dụ 1 người A trong tài khoản có 3 triệu và đang thực hiện 1 giao dịch để nạp vào 2 triệu cho tài khoản. Transaction đã chạy update xong tài khoản lên 5 triệu nhưng vẫn còn 1 số thao tác chưa chạy tới và dữ liệu này vẫn chưa được commit. 1 người B khác dùng chung tài khoản thực hiện kiểm tra số dư, và kết quả trả về là 5 triệu. Giao dịch của người A xảy ra sự cố và báo lỗi, dữ liệu được roll back về 3 triệu. Như vậy người B đang nhận được dữ liệu sai.

- **Lost Updates**: xảy ra khi hai quy trình cố gắng thao tác cùng một dữ liệu đồng thời. Điều này có thể dẫn đến mất dữ liệu hoặc quy trình thứ hai có thể overwrite quy trình đầu tiên dẫn đến mất dữ liệu.

- **Non-repeatable Reads**: xảy ra khi một quy trình đang đọc data thì quy trình khác viết data. Trong đọc non-repeatable, quy trình đầu tiên đọc giá trị có thể nhận được hai giá trị khác nhau, vì dữ liệu đã thay đổi được đọc lần thứ hai vì quy trình hai thay đổi dữ liệu.

- **Phantom Reads**: hai truy vấn giống nhau được thực thi bởi hai user cho thấy hai output khác nhau. Ví dụ, nếu user A chọn một truy vẫn để đọc một vài data, ngay lúc đó user B thêm một vài data mới nhưng user A chỉ có thể đọc data cũ tại lần truy vấn đầu tiên, khi user A thực hiện truy vấn lại (cùng câu lệnh cũ) và có được tập data khác.

**Isolation level** (mức cô lập dữ liệu): 

```SET TRANSACTION ISOLATION LEVEL [TYPE_OF_ISOLATION_LEVEL]```

Mỗi transaction được chỉ định 1 isolation level để chỉ định **mức độ mà nó phải được cách ly khỏi các sự sửa đổi dữ liệu được thực hiện bởi các transaction khác**.

SQL cung cấp các mức isolation levels sau xếp theo thứ tự tăng dần của mức độ cô lập của dữ liệu: Read Uncommitted, Read Commited, Repeatable Read, Serializable, Snapshot

- ***Read uncommitted*** (mức cô lập thấp nhất): Khi transaction thực hiện ở mức này, các truy vấn vẫn có thể truy nhập vào các bản ghi đang được cập nhật bởi một transaction khác và nhận được dữ liệu tại thời điểm đó mặc dù dữ liệu đó chưa được commit (uncommited data). Điều này sẽ dẫn đến có thể xảy ra **Dirty read**.

- ***Read commited*** (mức isolation mặc định của SQL Server Database Engine: Transaction sẽ không đọc được dữ liệu đang được cập nhật mà phải đợi đến khi việc cập nhật thực hiện xong. Vì thế nó tránh được dirty read, tuy nhiên việc read commited chỉ áp dụng cho lệnh **update** mà không áp dụng cho lệnh ~~insert~~ hoặc ~~delete~~, vì thế có thể xảy ra **phantom read**.

- ***Repeatable read*** (mặc định ở innoDB engine): ngăn không cho transaction ghi vào dữ liệu đang được đọc bởi một transaction khác cho đến khi transaction khác đó hoàn tất.

- ***Serializable** (mức cô lập cao nhất): các transactions hoàn toàn tách biệt với nhau, SQL đặt read lock và write lock trên dữ liệu cho tới khi transaction kết thúc (**~~phantom read~~**)

- ***Snapshot***: (chỉ có thể sử dụng khi row versioning được bật, tương đương với Serializable). Khi transaction đang select các bản ghi, nó không khóa các bản ghi này lại mà tạo một bản sao (snapshot) và select trên đó. Vì vậy các transaction khác insert/update lên các bản ghi đó không gây ảnh hưởng đến transaction ban đầu. Nó làm giảm blocking giữa các transaction mà vẫn đảm bảo tính toàn vẹn dữ liệu. Tuy nhiên cần thêm bộ nhớ để lưu bản sao của các bản ghi.

|Isolation level|Dirty read|Nonrepeatable read|Phantom read|
|---|:----:|:---:|:---:|
|Read uncommited|Y|Y|Y|
|Read commited|N|Y|Y|
|Repeatable read|N|N|Y|
|Serializable read|N|N|N|
|Snapshot|N|N|N|

**Concurrency type**

- ***Read-only (Share lock)*** (kiểu mặc định): Cursor có thể đọc data nhưng không thể update hay delete data. Mặc dù DBMS có thể khóa rows để thực thi các mức độ cô lập Repeatable Read và Serializable, nhưng nó có thể sử dụng read locks thay vì write locks. Kết quả này dẫn đến concurency cao hơn vì các transaction khác ít nhất có thể đọc data. Giao dịch giữ Share lock được phép đọc dữ liệu, nhưng không được phép ghi. Nhiều transaction có thể đồng thời giữ Share lock trên cùng 1 đơn vị dữ liệu.

- ***Exclusive Lock***: hay còn gọi là write lock là lock mà một transaction chiếm hữu khi muốn đọc và ghi dữ liệu. Tại 1 thời điểm chỉ có tối đa 1 transaction được quyền giữ Exclusive lock trên 1 đơn dữ liệu.Không thể thiết lập Share lock trên đơn vị dữ liệu đang có Exclusive lock.

- ***Update lock***: Khóa dự định ghi. Update lock sử dụng khi đọc dữ liệu với dự định ghi trở lại trên dữ liệu này. Update lock là chế độ khoá trung gian giữa Share lock và Exclusive lock. Khi thực hiện thao tác ghi lên dữ liệu thì bắt buộc Update lock phải tự động chuyển thành Exclusive lock. Transaction giữ Update lock được phép GHI + ĐỌC dữ liệu. Tại 1 thời điểm chỉ có tối đa 1 transaction được quyền giữ Update lock trên 1 đơn dữ liệu. Có thể thiết lập Share lock trên đơn vị dữ liệu đang có Update lock

- ***Locking***: cursor sử dụng mức độ thấp nhất của việc khóa cần thiết để đảm bảo nó có thể update hoặc xóa row trong tập kết quả. Kết quả là mức độ concurrency thường thấp, đặc biệt là tại mức cô lập Repeatable Read và Serializable. Mỗi transaction yêu cầu các loại khóa khác nhau trên resource như: row lock, page lock hay table lock, ... tùy theo transaction phụ thuộc vào gì. Lock ngăn các transaction khác không cho chúng thay đổi dữ liệu. Các transaction sẽ giải phóng Lock khi nó không còn phụ thuộc vào các tài nguyên bị Lock nữa. Khi này các transaction khác mới có thể truy cập những tài nguyên này.

     Khi 1 tài nguyên bị Lock, các transaction khác sẽ không thể thao tác được với tài nguyên này mà phải đợi đến khi transaction đang giữ tài nguyên giải phóng Lock mới có thể truy cập. Điều này sẽ dẫn đến việc các transaction phải đợi nhau quá lâu dẫn tới giảm đáng kể hiệu năng của hệ thống. 

**Optimistic concurrency using row versions and values**: Cursor sử dụng optimistic concurrency: updates hoặc deletes rows chỉ khi không có thay đổi kể từ lần đọc gần nhất. Để phát hiện thay đổi, nó so sánh các row version và values. Không có gì đảm bảo rằng cursor sẽ có thể update hoặc xóa hàng, nhưng concurrency cao hơn nhiều so với khi locking. 

**Row versioning**

Row versioning lưu trữ các versions của tài nguyên đang bị lock, các transaction khác nếu chỉ yêu cầu đọc các tài nguyên này sẽ được trả về version phù hợp mà không cần phải đợi đến khi tài nguyên được giải phóng Lock. Điều này sẽ giúp giảm đáng kể khả năng nhiều transaction phải đợi nhau để sử dụng tài nguyên.

**Optimistic Concurrency**

Optimistic concurrency xuất phát từ tên của nó, từ giả định lạc quan rằng các vụ va chạm giữa các transaction sẽ hiếm khi xảy ra; Một vụ va chạm được cho là đã xảy ra khi một transaction khác cập nhật hoặc xóa một data row giữa thời gian data row đó được đọc bởi transaction hiện tại và thời gian nó được cập nhật hoặc xóa. Nó trái ngược với pessimistic concurrency, hoặc locking, trong đó nhà phát triển ứng dụng tin rằng các va chạm như vậy là phổ biến.

Trong Optimistic concurrency, một hàng được mở khóa cho đến khi cập nhật hoặc xóa nó. Tại thời điểm đó, row được đọc lại và kiểm tra xem nó có được thay đổi kể từ lần đọc lần cuối không. Nếu row đã thay đổi, bản cập nhật hoặc xóa thất bại và phải được thử lại.

Để xác định xem một hàng đã bị thay đổi chưa, version mới của nó được kiểm tra lại với cached version. Việc kiểm tra này có thể dựa trên row version, chẳng hạn timestamp column trong SQL Server, hoặc giá trị của mồi column trong hàng. Many DBMS không ủng hộ row version.

Optimistic concurrency có thể được thực hiện bởi data source hoặc apllication. Cả hai trường hợp này, application nên sử dựng mức cô lập transaction thấp, chẳng hạn như Read commited.

Nếu optimistic concurrency được thực thi bởi data source, application thiết lập 
SQL_ATTR_CONCURRENCY statement attribute thành SQL_CONCUR_ROWVER hoặc SQL_CONCUR_VALUES. Để update hoặc xóa row, nó thực thi một positioned update hoặc câu lệnh xóa hoặc gọi SQLSetPos giống như với pessimistic concurrency; trình điều khiển hoặc data source trả về SQLSTATE 01001 (Cursor operation conflict) nếu cập nhật hoặc xóa thất bại vì va chạm.

Nếu application tự nó thực thi optimistic concurrency, nó thiết lập
SQL_ATTR_CONCURRENCY statement attribute thành SQL_CONCUR_READ_ONLY để đọc một row. Nếu nó so sánh row version và không biể row version column, nó gọi SQLSpecialColumns với tùy chọn SQL_ROWVER để xác định tên của column này.

Application cập nhật hoặc xóa hàng bằng việc tăng concurrency tới SQL_CONCUR_LOCK (để có được quyền truy cập tới hàng) và thực thi câu lệnh UPDATE hoặc DELETE với mệnh đề WHERE chỉ ra cụ thể version hoặc value của hàng khi application đọc nó. Nếu hàng đã được thay đổi, câu lệnh sẽ thất bại. Nếu mệnh đề WHERE không chỉ ra hàng cụ thể, câu lệnh có thể update hoặc xóa hàng, row version luôn luôn xác định row một cách cụ thể, nhưng row values xác định hàng cụ thể chỉ khi nó bao gồm primary key.

## **Function** (<a name="Function"></a>)
Gồm 2 loại: **Function hệ thống** và **Function do người dùng tự định nghĩa**

Function người dùng tự định nghĩa gồm 2 loại:
- Scalar-valued: Trả về giá trị vô hướng của các kiểu dữ liệu T-SQL
- Table-valued: Trả về bảng, là kết quả của một hoặc nhiều lệnh

*Lưu ý:*

 Tên function phải là duy nhất trong 1 CSDL. 
 
 Function được tạo/định nghĩa trong CSDL nào thì chỉ sử dụng trong CSDL đó. Khác với Function có sẵn của SQL được truy cập ở bất cứ đâu

***Function trả về giá trị loại Scalar-valued***:

      CREATE FUNCTION <Tên function>
      ([@<tên tham số> <kiểu dữ liệu> [= <giá trị mặc định>], …,[...]])
      RETURNS <kiểu dữ liệu>
      [WITH ENCRYPTION]
      [AS]
      BEGIN
      [Thân của hàm]
      RETURN <Biểu thức giá trị đơn>
      END

Trong đó:

  - Tên function: Tên của hàm chúng ta sẽ tạo
  - Tên tham số: Là các tham số Input cho hàm. Khai báo báo gồm tên của tham số (trước tên tham số sử dụng tiền tố @), kiểu dữ liệu của tham số, chúng ta có thể chỉ định giá trị mặc định cho tham số. Có thể chỉ định nhiều tham số đầu vào
  - RETURNS: từ khóa này chỉ định kiểu dữ liệu hàm sẽ trả về. Kiểu dữ liệu phải được chỉ định kiểu độ dài dữ liệu. Ví dụ: varchar(100)
  - WITH ENCRYPTION: Từ khóa chỉ định code của hàm sẽ được mã hóa trong bảng syscomments.
  - AS: Từ khóa cho biết code của hàm bắt đầu.
  - BEGIN: Đi cùng với END để tạo thành bao khối bao các câu lệnh trong thân hàm.
  - RETURN: Từ khóa này sẽ gửi giá trị tới thủ tục gọi hàm

***Function trả về giá trị bảng đơn giản***: Trả về bảng, là kết quả của một câu lệnh SELECT đơn

      CREATE FUNCTION <Tên function>
      ([@<tên tham số> <kiểu dữ liệu> [= <giá trị mặc định>], …,[...]])
      RETURNS TABLE
      [WITH ENCRYPTION]
      [AS]
      RETURN <Câu lệnh SQL>
      END

***Function trả về giá trị bảng đa câu lệnh***

      CREATE FUNCTION <Tên function>
      ([@<tên tham số> <kiểu dữ liệu> [= <giá trị mặc định>], …,[...]])
      RETURNS @<tên biến trả về> TABLE (<tên cột 1> <kiểu dữ liệu> [tùy chọn thuộc tính], ..., <tên cột n> <kiểu dữ liệu> [tùy chọn thuộc tính])
      [AS]
      BEGIN
      <Câu lệnh SQL>
      RETURN
      END

**Tham chiếu tới hàm:**

```SELECT [tên hàm](tham số)```

**Thay đổi hàm:**

      ALTER FUNCTION <Tên function>
           ([@<tên tham số> <kiểu dữ liệu> [= <giá trị mặc định>], …,[...]])
      RETURNS <kiểu dữ liệu> | TABLE
      [WITH ENCRYPTION]
      [AS]
      BEGIN
          [Thân của hàm]
      RETURN <Biểu thức giá trị đơn> | Câu lệnh SQL
      END

**Xem nội dung của hàm:**

```EXEC sp_helptext 'FunctionName'```

**Xóa hàm:**

```DROP [tên hàm]```

Ví dụ: Bài toán quản lý vay có thế chấp tài sản

![SĐVL](https://images.viblo.asia/dd3e6dec-18fb-4ca2-a4ad-97ee3c91a7f2.png)

Tạo function cho biết số lượng khách hàng theo địa chỉ bất kỳ nhận vào với điều kiện là khách hàng có tổng số tiền vay từ trước đến nay từ 200 triệu trở lên.
 
  + Hàm trả về giá trị scalar:

        CREATE FUNCTION count_customer_with_address (@address varchar(200))
        RETURNS int
        AS 
        BEGIN
	    DECLARE @count int = 0
	    SELECT @count = count(*) FROM (
          SELECT Vay.MaKH 
          FROM Vay,KhachHang
          WHERE Vay.MaKH=KhachHang.MaKH AND KhachHang.DiaChi= @address
          GROUp BY Vay.MaKH
          HAVING SUM(Vay.SoTienVay)>=200
          ) AS Temp
          RETURN @count
         END

Gọi thực thi function vừa tạo:

```PRINT dbo.count_customer_with_address('Ha Noi')```

  + Hàm trả về đơn bảng:

        CREATE FUNCTION count_customer_with_address2 (@address varchar(200))
        RETURNS TABLE
        AS 
            RETURN SELECT count(*) AS 'Total customers' FROM (
            SELECT Vay.MaKH 
            FROM Vay,KhachHang
            WHERE Vay.MaKH=KhachHang.MaKH AND KhachHang.DiaChi= @address
            GROUp BY Vay.MaKH
            HAVING SUM(Vay.SoTienVay)>=200
        ) AS Temp

   + Hàm trả về giá trị bảng đa câu lệnh:

         CREATE FUNCTION count_customer_with_address3 (@address varchar(200))
         RETURNS @new_table TABLE (DiaChi varchar(200), SoLuong int)
         AS
         BEGIN
	     DECLARE @count int = 0
	     SELECT @count = count(*) FROM (
           SELECT Vay.MaKH 
           FROM Vay,KhachHang
           WHERE Vay.MaKH=KhachHang.MaKH AND KhachHang.DiaChi= @address
           GROUp BY Vay.MaKH
           HAVING SUM(Vay.SoTienVay)>=200
           ) AS Temp
           INSERT INTO @new_table VALUES (@address, @count)
         RETURN
         END   

## **Stored Procedure** (<a name="StoredProcedure"></a>)

Một Stored Procedure bao gồm các câu lệnh Transact-SQL và được lưu lại trong cơ sở dữ liệu. Các lập trình viên chỉ cần gọi ra và thực thi thông qua SQL Server Management Studio hoặc ngay trong ứng dụng đang phát triển.

- Tạo Stored Procedure:

```CREATE PROCEDURE StoredProcedureName AS```

Ví dụ:

      CREATE PROCEDURE MyStoredProcedure AS
      SET ROWCOUNT 10
      SELECT Products.ProductName AS TenMostExpensiveProducts, Products.UnitPrice
      FROM Products
      ORDER BY Products.UnitPrice DESC

- Sửa Stored Procedure:

```ALTER PROCEDURE MyStoredProcedure AS```

- Thực thi Stored Procedure:

```EXEC MyStoredProcedure @ParameterName="MyParameter"```

## **VIEW (<a name="View"></a>)**

VIEW là một **bảng ảo** trong cơ sở dữ liệu có nội dung được định nghĩa thông qua một câu lệnh SQL nào đó. VIEW bao gồm các hàng và cột giống như một bảng thực. Các **trường trong VIEW** là các **trường từ một hoặc nhiều bảng thực** trong Database.

VIEW **không** được xem là một **cấu trúc lưu trữ dữ liệu tồn tại** trong cơ sở dữ liệu. Dữ liệu quan sát được trong VIEW được lấy từ các bảng thông qua câu lệnh truy vấn dữ liệu và được sử dụng để **hạn chế truy cập cơ sở dữ liệu** hoặc để ẩn dữ liệu phức tạp.

Có thể coi View cũng là một table nhưng chức năng của nó là chỉ để đọc, nên không thể thực hiện các thao tác như insert, update hay delete trên view.

VIEW được tạo ra bằng cách SELECT các cột trong các TABLE, khi dữ liệu trong table được cập nhật, view cũng tự động được cập nhật.

- Tạo VIEW:

```CREATE VIEW ten_view AS SELECT [columns] FROM [table] [dieu_kien]```

- Sửa thông tin trong VIEW:

```UPDATE [tên VIEW] SET [thông tin update] WHERE [điều kiện]```

- Xóa VIEW:

```DROP VIEW [tên view]```

## **Trigger** (<a name="Trigger"></a>)

Trigger là các stored procedure đặc biệt, được thực thi tự động khi xảy ra một sự kiện trong database:

- Trigger ngôn ngữ thao tác (data manipulation language - DML): xảy ra khi user sửa đổi data bằng các sự kiện data manipulation language (insert, update, delete)

- Trigger ngôn ngữ định nghĩa (Data definition language): xảy ra khi phản hồi lại các sự kiện data defintion langguage (create, alter, drop)

- Trigger đăng nhập (Log on): xảy ra khi có sự kiện log on

***Tạo trigger***

      CREATE TRIGGER [schema_name.]trigger_name
      ON table_name
      AFTER  {[INSERT],[UPDATE],[DELETE]}
      [NOT FOR REPLICATION]
      AS
      {sql_statements}

Trong đó:

- schema_name: tên của schema mà trigger thuộc
- trigger_name: tên user chỉ định dùng cho trigger
- table_name: bảng mà trigger sẽ tác động tới
- Sự kiện kích hoạt trigger được liệt kê trong câu lệnh after (sự kiện này có thể là insert, update, delete). Một trigger cí thể tác động tới một hoặc nhiều sự kiện.
- NOT FOR REPLICATION: tùy chọn chỉ thị SQL server không được kích hoạt trigger khi việc sửa đổi dữ liệu được thực hiện như một phần của quá trình sao chép
- sql_statements: một hoặc nhiều câu lệnh Transact - SQL được sử dụng để thực hiện các hành động sau khi sự kiện xay ra

***Tắt tạm thời trigger***

      DISABLE TRIGGER [schema_name.][trigger_name] 
      ON [object_name | DATABASE | ALL SERVER]

***Bật trigger đã bị tắt***

      ENABLE TRIGGER [schema_name.][trigger_name] 
      ON [object_name | DATABASE | ALL SERVER]

***Xóa trigger***

- DML Trigger
  
      DROP TRIGGER [ IF EXISTS ] [schema_name.]trigger_name [ ,...n ] [ ; ]  
  
- DDL Trigger
  
      DROP TRIGGER [ IF EXISTS ] trigger_name [ ,...n ]   
      ON { DATABASE | ALL SERVER }   
      [ ; ]  
  
- Logon Trigger
  
      DROP TRIGGER [ IF EXISTS ] trigger_name [ ,...n ]   
      ON ALL SERVER

## **Index** (<a name="index"></a>)

INDEX là bảng tra cứu đặc biệt mà công cụ tìm kiếm cơ sở dữ liệu có thể sử dụng để tăng nhanh thời gian và hiệu suất truy xuất dữ liệu.

INDEX giúp **tăng tốc các truy vấn SELECT** chứa các mệnh đề **WHERE hoặc ORDER**, nhưng nó làm **chậm** việc dữ liệu nhập vào với các lệnh **UPDATE và INSERT** (vì mỗi lần update/insert cần tính lại index). 

Tạo hoặc xóa index không ảnh hưởng tới dữ liệu.

***Các kiểu index có trong SQL:***

- Single-Column Index: được tạo cho duy nhất 1 cột trong bảng

      CREATE INDEX ten_index ON ten_bang;

- Unique Index: không cho phép chèn bất kỳ giá trị trùng lặp nào vào bảng

      CREATE INDEX ten_index
      ON ten_bang (ten_cot);

- Composite Index: kết hợp hai hoặc nhiều cột trong một bảng

      CREATE UNIQUE INDEX ten_index
      ON ten_bang (ten_cot);

- Implicit Index: tạo tự động bởi Database Server khi một bảng được tạo. Các Index ngầm định được tạo tự động cho các ràng buộc Primary key và các ràng buộc Unique

**Xóa index đã tạo**

```DROP INDEX ten_index;```

***Search Argument-Able (sargable)*** 

## **Partition** (<a name="partition"></a>)

*Không có sẵn trong các version kể từ SQL Server 2016 (13.x) SP1 về trước*

*Database engine mặc định hỗ trợ tối đa 15,000 partitions cho mỗi table. Trong các versioin trước SQL Server 2012 (11.x), mặc định hỗ trợ tối đa 1,000 partition*.

**Partition** là việc **phân chia một table thành những phần nhỏ** theo một **logic** nhất định, được phân biệt bằng key (thường là tên column trong table).

Mỗi lần truy vấn DB engine phải duyệt qua toàn bộ bảng để lấy dữ liệu, gây ra vấn đề về **performance** khi bản ghi trong table quá lớn. Partition giúp ta chỉ lấy dữ liệu tại vùng nhất định thay vì toàn bộ table.

Data của các table đã được phân vùng và đánh chỉ số được chia thành các unit, và được lưu trữ trong một filegroup. Data được phân vùng theo chiều ngang, do đó các nhóm rows được tương thích tới từng partition. Tất cả các partition của một table phải được lưu trữ trong cùng một database

Các kiểu partition:

- Range partitioning: chia table ra thành nhiều khoảng giá trị liên tiếp và không chồng chéo lên nhau

Range partition giúp việc insert và tìm kiếm nhanh hơn: khi insert nếu có giá trị nằm trong khoảng nào thì nó sẽ được insert vào trong đúng khoảng đã định nghĩa (tương tự với tìm kiếm)

- List partitioning: nhặt những phần tử được chỉ định tạo thành 1 danh sách

- Columns partitioning
- Hash partitioning
- Key partitioning
- Subpartitioning

**Các thành phần của partition**

- Partition function: định nghĩa cách mà các row của table được ghép tới tập các partition dựa vào giá trị của các cột quan trọng (gọi là partitioning column). 

    Partition function xác định số lượng partition và giới hạn partition mà table sẽ có.

    Các loại range (LEFT hoặc RIGHT) chỉ ra cách mà giá trị giới hạn của partition function sẽ được đặt vào kết quả phân vùng

    + LEFT range (mặc định): dấu bằng ở giới hạn trên của mỗi part (trừ part cuối cùng) 

    |partition|Part1|part2|part3|
    |--|--|--|--|
    |Value intervals|values <=1000|1000 < values >= 2000|2000 < values|

    + RIGHT range: dấu bằng ở giới hạn dưới của mỗi part (trừ part đầu tiên)

    |partition|Part1|part2|part3|
    |--|--|--|--|
    |Value intervals|values <1000|1000 <= values > 2000|2000 <= values|

CREATE PARTITION FUNCTION

     CREATE PARTITION FUNCTION partition_function_name ( input_parameter_type )  
     AS RANGE [ LEFT | RIGHT ]   
     FOR VALUES ( [ boundary_value [ ,...n ] ] )   
     [ ; ]  

Ví dụ:

     CREATE PARTITION FUNCTION [myDateRangePF1] (datetime)  
     AS RANGE RIGHT FOR VALUES ('20030201', '20030301', '20030401',  
               '20030501', '20030601', '20030701', '20030801',   
               '20030901', '20031001', '20031101', '20031201');

- Partition scheme: ghép các part của partition function tới một hoặc nhiều filegroup.

  Việc đặt các partition vào nhiều filegroup để đảm bảo việc bạn có thể thực hiện độc lập các hoạt động sao lưu và khôi phục các partition.

CREATE PARTITION SCHEME

     CREATE PARTITION SCHEME partition_scheme_name  
     AS PARTITION partition_function_name  
     [ ALL ] TO ( { file_group_name | [ PRIMARY ] } [ ,...n ] )  
     [ ; ]

Ví dụ:

     CREATE PARTITION FUNCTION myRangePF2 (INT)  
     AS RANGE LEFT FOR VALUES (1, 100, 1000);  
     GO  
     CREATE PARTITION SCHEME myRangePS2  
     AS PARTITION myRangePF2  
     TO ( FG1, FG2, test1fg, test2fg );
Kết quả:

|Filegroup|Partition|Values|
|--|--|--|
|FG1|1|<=1|
|FG1|2|>1 AND <=100|
|FG1|1|<100 AND >=1000|
|FG2|1|>1000|


- Partitioning column: Cột mà partition function sử dụng để phân vùng table. Khi chọn partitioning column cần cân nhắc:

  + Partitioning column có thể một hoặc nhiều column
  + Không chọn các cột của các loại dữ liệu đối tượng lớn (LOB), chẳng hạn như ntext, văn bản, hình ảnh, xml, varchar (max), nvarchar (max) và varbinary (max).
  + Các column của tất cả các loại data hợp lệ để làm index key column có thể sử dụng là partitioning column, trừ timestamp 
  + Không chọn Microsoft .NET Framework common language runtime (CLR) loại user-defined  và alias data type 

Lưu ý:

- Partition function và partition scheme được giới hạn trong database mà nó được tạo. The scope of a partition function and scheme is limited to the database in which they have been created. Trong database đó, partiton function riêng biệt với các function khác.

- Nếu bất kỳ row nào có giá trị NULL tại partitioning column, row đó đưuọc đặt ở part ngoài cùng bên trái (left-most partition). Tuy nhiên, nếu NULL là giá trị boundary đầu tiên và sử dụng RANGE RIGHT trong partition function, thì left-most partition trống, và NULL được đặt trong partition thứ hai.

**Create partitioned tables**

1. Tạo một hoặc nhiều Filegroup hoặc Filegroup và các data file tương ứng sẽ giữ các phân vùng được chỉ định bởi partition scheme. Có thể chọn gán tất cả các partition cho một filegroup duy nhất, sử dụng FileSgroup hiện có, chẳng hạn như PRIMARY filegroup.

Ví dụ: Trong DB partitionTest, thêm filegroup FG1

     ALTER DATABASE PartitionTest  
     ADD FILEGROUP FG1;  
     GO  

2. Tạo một partition function để ghép các row của table tới tưng partition dựa vào giá trị của một column cụ thể. Có thể sử dụng một partition function duy nhất cho nhiều đối tượng partition.
3. Tạo một partition scheme để ghép các partition của table tới một hoặc nhiều file group. Có thể sử dụng một scheme function duy nhất cho nhiều đối tượng partition.
4 CREATE hoặc ALTER Table và chỉ định partition scheme là vị trí lưu trữ, cùng với cột sẽ đóng vai trò là partitioning column.

Ví dụ:

    --Tạo DATABASE---
    CREATE DATABASE PartitionTest;
    GO

    USE PartitionTest;
    GO
    --Tạo filegroup trong Database--
    ALTER DATABASE PartitionTest  
    ADD FILEGROUP test1fg;  
    GO  
    ALTER DATABASE PartitionTest  
    ADD FILEGROUP test2fg;  
    GO  
    ALTER DATABASE PartitionTest  
    ADD FILEGROUP test3fg;  
    GO  
    ALTER DATABASE PartitionTest  
    ADD FILEGROUP test4fg;   

    --Tạo các file và thêm file vừa tạo vào từng filegroup--
    ALTER DATABASE PartitionTest   
    ADD FILE   
    (  
        NAME = partitiontest1,  
        FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\partitiontest1.ndf',  
        SIZE = 5MB,  
        FILEGROWTH = 5MB  
    )  
    TO FILEGROUP test1fg;  
    ALTER DATABASE PartitionTest   
    ADD FILE   
    (  
        NAME = partitiontest2,  
        FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\partitiontest2.ndf',  
        SIZE = 5MB,  
        FILEGROWTH = 5MB  
    )  
    TO FILEGROUP test2fg;  
    GO  
    ALTER DATABASE PartitionTest   
    ADD FILE   
    (  
    NAME = partitiontest3,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\partitiontest3.ndf',  
    SIZE = 5MB,  
    FILEGROWTH = 5MB  
    )  
    TO FILEGROUP test3fg;  
    GO  
    ALTER DATABASE PartitionTest   
    ADD FILE   
    (  
    NAME = partitiontest4,  
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\partitiontest4.ndf',  
    SIZE = 5MB,  
    FILEGROWTH = 5MB  
    )  
    TO FILEGROUP test4fg;  
    GO  

    --Tạo partiton function-- 
    CREATE PARTITION FUNCTION myRangePF1 (datetime2(0))  
    AS RANGE RIGHT FOR VALUES ('2022-04-01', '2022-05-01', '2022-06-01') ;  
    GO  

    --Tạo partition scheme--
    CREATE PARTITION SCHEME myRangePS1  
    AS PARTITION myRangePF1  
    TO (test1fg, test2fg, test3fg, test4fg) ;  
    GO  

    --Tạo partition table--
    CREATE TABLE PartitionTable (col1 datetime2(0) PRIMARY KEY, col2 char(10))  
    ON myRangePS1 (col1) ;  
    GO




## **Logs** (<a name="logs"></a>)

Mỗi database có một transaction log ghi lại tất cả các transaction và những **thay đổi trong database** gây ra bởi mỗi transaction.

Nếu có một lỗi hệ thống xảy ra, transaction log sẽ giúp database trở lại trạng thái nhất quán

Quá trình này diễn ra như sau: 
1. Đầu tiên, khi có một sự thay đổi data như Insert, Update, Delete được yêu cầu từ các ứng dụng, SQL Server sẽ tải **(load) data page** tương ứng lên memory (vùng bộ nhớ này gọi là **data cache**), sau đó data trong data cache được thay đổi(những data page bị thay đổi còn gọi là **dirty-page**). 
2. Tiếp theo mọi sự thay đổi đều được ghi vào transaction log file (**write-ahead log**). Mỗi dirty page sẽ có một bản ghi tương ứng trong log file, bao gồm chi tiết hành động (UPDATE, DELETE, hay INSERT), dữ liệu trước khi xảy ra hành động, và dữ liệu sau khi xảy ra hành động. 
3. Cuối cùng thì quá trình **Check Point Process** sẽ kiểm tra và viết tất cả những transaction đã được commited (hoàn tất) vào đĩa cứng (flushing the page). Check point process định kỳ quét bộ nhớ và ghi các trang bẩn ra đĩa (data file) và đánh dấu chúng lại là “sạch”. Checkpoint cũng tạo một bản ghi trong log file, tất nhiên với nội dung là “CHECKPOINT”. Điều này cực kỳ quan trọng cho quá trình khôi phục (recovery).

![logsfile](https://voer.edu.vn/file/4176)

Transaction log hỗ trợ các hoạt động sau:

- Khôi phục một transaction: Nếu một application thực hiện lệnh rollback, hoặc database engine phát hiện lỗi (chẳng hạn mất kết nối với client), bản ghi log được sử dụng để roll back các sửa đổi được thực hiện bởi một transaction không hoàn thành.
- Khôi phục tất các các transaction không hoàn thành khi SQL Server được khởi động: Nếu server lỗi, database có thể ở trạng thái mà một vài sửa đổi chưa được viết từ buffer cache tới data files, và có thể có một vài sửa đổi từ transaction chưa hoàn thành trong datafile. Khi một instance của SQL khởi động, nó khởi chạy recovery của mỗi database. Mỗi thay đổi được ghi trong log có thể chưa được ghi trong datafile sẽ được được roll back. Mỗi transaction chưa hoàn thành được tìm thấy trong transasction log sau đó được roll back để đảm bảo tính toàn vẹn của database.
- Kéo một database được khôi phục, file, filegroup hoặc page tới điểm lỗi
- Hỗ trợ sao chép trânsaction

**Đặc điểm của transaction log**

- transaction log được thực thi như là một file riêng biệt hoặc tập các file trong database. Log cache được quản lý một các riêng biệt khỏi buffer cache cho các data page
- transaction log có thể được thực thi trong một vài file. Các file được định nghĩa để mở rộng một cách tự động bởi giá trị FILEGROWTH cho mỗi log
- Cơ chế để tái sử dụng space trong log file nhanh và ảnh hưởng tối thiể tới thông lượng transaction.

**Kiến trúc logic của transaction log**

**Transaction log** hoạt động như là một **chuỗi các bản ghi log**. Mỗi bản ghi log được định danh bởi một **log sequence number (LSN)**. Mỗi bản ghi log mới có LSN cao hơn LSN của bản ghi trước đó. Các bản ghi log được **lưu trữ theo trình tự nối tiếp**, chúng được tạo sao cho nếu LSN2 lớn hơn LSN1, thay đổi được mô tả bởi bản ghi LSN2 xảy ra sau thay đổi được mô tả bởi bản ghi LSN1. Mỗi bản ghi log chuứa **ID của transaction** mà nó thuộc về. 

Bản ghi log để ghi lại những sửa đổi data hoặc là hoạt động logic được thực hiện, hoặc là chúng ghi lại hình ảnh trước và sau của data được sửa đổi (hình ảnh trước là bản copy của data trước khi thực hiện hoạt động, hình ảnh sau là bản sao của data sau khi hoạt động được thực hiện)

Các bước khôi phục hoạt động phụ thuộc vào loại bản ghi log

- Ghi chép lại Hoạt động logic:

  + Để roll forward các hoạt động logic, hoạt động đó sẽ được thực hiện lại
  + Để roll back hoạt động logic, hoạt động ngược lại sẽ được thực hiện

- Ghi chép lại ảnh trước và sau:

  + Để roll forward các hoạt động, ảnh sau được áp dụng
  + Để roll back hoạt động logic, ảnh trước được áp dụng

Nhiều hoạt động được ghi lại trong transaction log, bao gồm:

- Bắt đầu hoặc kết thúc mỗi transaction
- Mỗi thay đổi data (insert, update hoặc xóa), bao gồm những thay đổi bởi stored procedure hệ thống hoặc các câu lệnh định nghĩa dữ liệu (data definiton language) tới bất kỳ table (bao gồm system table)
- Tạo hoặc xóa table/index

Hoạt động roll back cũng được ghi nhật ký. Mỗi transaction dự trữ space trên transaction log để đảm bảo đủ log space hỗ trợ việc rollback (có thể do câu lệnh roll back được yêu cầu thực thi hoặc do lỗi). Tổng space phụ thuộc vào hoạt động của transaction, Nhưng nhìn chung nó bằng với lượng space được sử dụng để ghi lại từng thao tác. Space dự trữ được giải phóng khi transaction hoàn thành.

Phần log file từ bản ghi log đầu tiên cần phải có để rollback toàn bộ database thành công tới bản ghi log được ghi cuối cùng gọi là phần active của log (active log/tail of the log). Đó là phần log cần thiết để khôi phục hoàn toàn database. Không một đoạn nào của active log có thể bị phân cắt. LSN của bản ghi đầu tiên được gọi là LSN khôi phục tối thiểu (MinLSN).

**Kiến trúc vật lý của transaction**

Transaction log trong database tương ứng với một hoặc nhiều file vật lý. Về mặt lý thuyết, log file là chuỗi các bản ghi log. Mặt vật lý, chuỗi các bản ghi log được lưu trữ hiệu quả trong tập các file vật lý thực thi transaction log. Cần phải có một log file cho mỗi database.

- Virtual log files (VLFs): Database engine chia mỗi file log vật lý thành một số virtual log file. VLFs có kích thước không cố định, và không có số lượng VLFs cố định cho một file log vật lý. Database engine chọn kích thước của VLFs một các linh động trong khi tạo ra hoặc mở rộng log file. Database engine cố gắng duy trì số lượng virtual file nhỏ. Kích thước hoặc số lượng của virtual log file không thể được cấu hình hoặc thiết lập bởi admin.

  Nếu log file phát triển tới một kích thước lớn với nhiều sự tăng trưởng nhỏ, cần nhiều VLFs. Điều này có thể làm chậm quá trình khởi động database, backup log và restore operation. Nếu log file được thiết lập tới một kích thước lớn với một vài hoặc chỉ một sự tăng trưởng, sẽ có một vài VLFs lớn.

- Bản chất tuần hoàn của transaction log: Transaction log là một wrap-around file. Ví dụ một database mà file log vật lý được chia thành 4 VLFs file, khi tạo database, logical log file bắt đầu với file log vật lý. Các bản ghi log mới được thêm vào cuối logical log và mở rộng về phía cuối log vật lý. Log truncation giải phóng bất kỳ virtual log nào ghi lại tất cả xuất hiện trước LSN phục hồi tối thiểu - MinLSN (MinLSN là LSN của bản ghi log cũ nhất được yêu cầu cho việc roll back toàn cơ sở dữ liệu thành công). 

![VLFs](https://docs.microsoft.com/en-us/sql/relational-databases/media/tranlog3.png?view=sql-server-ver16)

Khi điểm cuối của logical log chạm tới điểm cuối của file log vật lý, bản ghi log mới wrap around tới điểm bắt đầu của file log vật lý

![wraparound](https://docs.microsoft.com/en-us/sql/relational-databases/media/tranlog4.png?view=sql-server-ver16)

Tuần hoàn này lặp lại không có điểm cuối, miễn là điểm cuối của logical log không bao giờ chạm tới điểm bắt đầu của logical log. Nếu một bản ghi log cũ được phân cắt đủ thường xuyên để luôn chừa đủ chỗ cho tất cả các bản ghi log mới được tạo qua checkpoint tiếp theo, log sẽ không bao giờ đầy. Tuy nhiên, nếu điểm cuối cảu logical log chạm tới điểm bắt đầu, một trong hai điều sau có thể xảy ra:

- Nếu FIELGROWTH được enable cho log và vẫn còn space trong ổ đĩa, file được mở rộng bởi thông số growth-increment được chỉ định và bản ghi log mới được thêm vào.
- Nếu FILEGROWTH không được thiết lập enable, hoặc ổ đĩa có ít space trống hơn tham số growth_increment được chi định, xuất hiện lỗi 9002

Nếu log chứa nhiều life log vật lý, logical file sẽ di chuyển qua toàn bộ fiel log vật lý trước khi nó wrap về điểm bât đầu của file log vật lý đầu tiên.

**Log truncation** (giữ cho log không bị đầy)

Log truncation xóa các VLFs không active khỏi logical transaction log của SQL database, space trống trong logical log để tái sử dụng cho physical transaction log. Nếu một transaction log không bao giờ được phân cắt sẽ dẫn đến đầy tất cả ổ đĩa chứa log file vật lý của nó. Tuy nhiên, trước khi log được truncate, cần phải có một hoạt động checkpoint. Một checkpoint ghi các page được sửa đổi trong bộ nhớ hiện tại (dirty page) và thông tin nhật ký transaction từ bộ nhớ tới ổ đĩa. Khi checkpoint được thực hiện, phần không active của transaction log được đánh dấu là có thể tái sử dụng. Sau đó, phần không hoạt động có thể được giải phóng bởi log truncation.

Ví dụ:

*transaction log chưa được phân cắt**

![trans1](https://docs.microsoft.com/en-us/sql/relational-databases/media/tranlog2.png?view=sql-server-ver16)

4 VLFs được sử dụng trong logical log. Logical log bất đầu ngay tại VLF đầu tiên và kết thúc tại VLF 4. Bản ghi MinLSN tại VLF3, VLF 1 và 2 chỉ chứa bản ghi log inactive, những record này có thể được phân cắt, VLF 5 vẫn chưa được sử dụng nên không phải một phần của logical log hiện tại.

![trans2](https://docs.microsoft.com/en-us/sql/relational-databases/media/tranlog3.png?view=sql-server-ver16)

VFL 1 và 2 được giải phóng để tái sử dụng, bây giờ logical log bắt đầu tại VLF 3, VLF 5 vẫn chưa được sử dụng, nên nó không là một phần của logical log hiện tại.

Phân cắt log xảy ra tự động sau mỗi sự kiện sau, trừ khi bị delay vì lý do nào đó:

- Theo mô hình phục hồi simple, sau một checkpoint
- Theo mô hình phục hồi full hoặc mô hình phục hồi bulk-logged, sau một log back up, nếu một checkpoint được thực hiện kể từ backup trước.

**Write-ahead transasction log**

SQL sử dụng thuật toán write-ahead logging (WAL) để đảm bảo rằng không một sự sửa đổi dữ liệu nào được viết lên ổ đĩa trước khi bản ghi log tương ứng được ghi vào ổ đĩa.

Cách data sửa đổi được ghi vào ổ đĩa: SQL duy trì buffer cache (đọc data page khi data được hồi phục). Khi một page được sửa đổi trong buffer cache, nó không ngay lập tức được viết vào ổ đĩa, thay vào đó, page được đánh dấu là dirty. Một data page có thể có nhiều hơn một logical write được tạo trước khi nó được ghi vào ổ đía một cách vật lý. Với mỗi logical write, một bản ghi log transaction được thêm vào log cache để ghi lại sự thay đổi. Bản ghi log phải được ghi vào ổ đĩa trước khi dirty page tương ứng bị loại bỏ khỏi buffer cache và viết vào ổ đĩa. Quá trình checkpoint định kỳ quét buffer cache với page từ database được chỉ định và viết tất cả các dirty page vào ổ đĩa. Checkpoint tiết kiệm thời gian trong quá tình khôi phục sau đó băng cách tạo ra điểm mà tất cả các dirty page đều được đảm bảo là đã được ghi vào ổ đĩa.

Việc ghi một data page đã sửa đổi từ buffer cache vào ổ đĩa được gọi là flushing page. SQL ngăn chặn một dirty page khỏi việc bị flush trước khi bản ghi log tương ứng được ghi. Bản ghi log được ghi vào ổ đĩa khi mà buffer log đã được flush. Điều này xảy ra bất cứ khi nào transaction commit hoặc log buffer đầy.

## **SQL Server Agent**(<a name="Agent"></a>)

Công cụ trong SQL Server giúp thực hiện 1 công việc theo lịch trình đặt sẵn. Các bước thực hiện

- Tạo 1 job
- Tạo các step để hoàn thành job
- Tạo schedule cho các step vừa tạo (thiết lập thời gian bắt đầu, kết thúc, chu kỳ thực hiện, thời gian thực hiện, ...)

**SQL Server Agent Fixed Database Roles**

SQL Server có các quyền chỉnh sửa database **msdb** sau, nhằm quản lý tốt hơn quyền truy cập tới SQL Server Agent
- SQLAgentUserRole
- SQLAgentReaderRole
- SQLAgentOperatorRole
(Các quyền trên được liệt kê từ ít đặc quyền nhất đến nhiều đặc quyền nhất)

Khi user không có một trong các quyền trên kết nối tới SQL Server trong SSMS, node SQL Server Agent không được hiển thị. User phải có một trong các quyền trên hoặc là thành viên của **sysadmin** fixed server role mới có thể sử dụng SQL Seerver Agent



### **Tạo một job**



### **Configure**

Bộ đầy đủ các lựa chọn cấu hình SQL Server Agent có sẵn trên SQL Sever Management Studio

- Chọn **SQL Sever Agent** tại Object Explorer (SSMS) để administer jobs, operators, alert
- Để sử dụng các function, SQL Server Agent phải được cấu hình để sử dụng thông tin xác thực của tài khoản là thành viên của  sysadmin trong SQL Sever. Tài khoản này phải có các quyền Windows sau:

  - Đăng nhập như một service (SeServiceLogonRight)
  - Thay thế một process-level token (SeAssignPrimaryTokenPrivilege)
  - Bỏ qua traverse checking (SeChangeNotifyPrivilege)
  - Điều chỉnh memory quotas cho một quá trình (SeIncreaseQuotasPrivilege)

Để cấu hình SQL Server Agent

1. Chọn Start -> Star Menu -> Control Panel
2. Trong Control Panel -> System and Security -> Administrative Tools -> Local Security Policy
3.Trong Local Security Policy, chọn chevron để mở rộng Local Policies folder -> chọn User Rights Assignment folder
4. Chuột phải vào permission mà bạn muốn cấu hình cho SQL Server -> Properties
5. Trong hộp thoại permission's properties, xác thực tài khoản SQL Server Agent chạy được liệt kê. Nếu không, chọn Add User or Group, nhập tài khoản mà SQL Server Agent chạy trong Select Users, Computers, Service Accounts, hoặc hộp thoại Groups, sau đó chọn OK.
6. Lặp lại các bước trên với mỗi permission mà bạn muốn thêm vào SQL Server agent, -> Chọn OK.

**A Job Catergory**

Job Catergory giúp tổ chức các job để dễ dàng lọc hay nhóm lại (chẳng hạn: tổ chức tất cả các job backup database trong database maintenance catergory)

Để assign một job vào job catergory:
*Sử dụng SQL Server Management Studio*
1. In Object Explorer, click the plus sign to expand the server where you want to assign a job to a job category.

2. Click the plus sign to expand SQL Server Agent.

3. Click the plus sign to expand the Jobs folder.

4. Right-click the job you want to edit and select Properties.

5. In the Job Properties -job_name dialog box, in the Category list, select the job category you want to assign to the job.

6. Click OK.

*T-SQL*

1. In Object Explorer, connect to an instance of Database Engine.

2. On the Standard bar, click New Query.

3. Copy and paste the following example into the query window and click Execute.

      -- adding a new job category to the "NightlyBackups" job  
      USE msdb ;  
      GO  
      EXEC dbo.sp_update_job  
            @job_name = N'NightlyBackups',  
            @category_name = N'[Uncategorized (Local)]';  
      GO

**Xóa tự động một job**

*Sử dụng SQL Server Management Studio*

1. In Object Explorer, connect to an instance of the SQL Server Database Engine, and then expand that instance.

2. Expand SQL Server Agent, expand Jobs, right-click the job you want to edit, and then click Properties.

3. Select the Notifications page.

4. Check Automatically delete job, and choose one of the following:

-  Click When the job succeeds to delete the job status when it has completed successfully.

- Click When the job fails to delete the job when it has completed unsuccessfully.

- Click When the job completes to delete the job regardless of completion status.

**Tự động restart**

*Sử dụng SSMS*

1. In Object Explorer, click the plus sign to expand the server where you want to configure SQL Server Agent to automatically restart.

2. Right-click SQL Server Agent, and then click Properties.

3. On the General page, check Auto restart SQL Server Agent if it stops unexpectedly.

**Liệt kê thông tin Job Catergory**

*Sử dụng T-SQL*

1. In Object Explorer, connect to an instance of Database Engine.

2. On the Standard bar, click New Query.

3. Copy and paste the following example into the query window and click Execute

       -- returns information about jobs that are administered locally  
       USE msdb ;  
       GO  

       EXEC dbo.sp_help_category  
       @type = N'LOCAL' ;  
       GO

**Start a job**

*Sử dụng SSMS*

1. In Object Explorer, connect to an instance of the SQL Server Database Engine, and then expand that instance.

2. Expand SQL Server Agent, and expand Jobs. Depending on how you want the job to start, do one of the following:

- If you are working on a single server, or working on a target server, or running a local server job on a master server, right-click the job you want to start, and then click Start Job.

- If you want to start multiple jobs, right-click Job Activity Monitor, and then click View Job Activity. In the Job Activity Monitor you can select multiple jobs, right-click your selection, and click Start Jobs.

- If you are working on a master server and want all targeted servers to run the job simultaneously, right-click the job you want to start, click Start Job, and then click Start on all targeted servers.

- If you are working on a master server and want to specify target servers for the job, right-click the job you want to start, click Start Job, and then click Start on specific target servers. In the Post Download Instructions dialog box, select the These target servers check box, and then select each target server on which this job should run.

*T-SQL*

1. In Object Explorer, connect to an instance of Database Engine.

2. On the Standard bar, click New Query.

3. Copy and paste the following example into the query window and click Execute.

            -- starts a job named Weekly Sales Data Backup.       
            USE msdb ;  
            GO  

            EXEC dbo.sp_start_job N'Weekly Sales Data Backup' ;  
            GO

**Stop a job**

*SSMS*

1. In Object Explorer, connect to an instance of the SQL Server Database Engine, and then expand that instance.

2. Expand SQL Server Agent, expand Jobs, right-click the job you want to stop, and then click Stop Job.

3. If you want to stop multiple jobs, right-click Job Activity Monitor, and then click View Job Activity. In the Job Activity Monitor, select the jobs you want to stop, right-click your selection, and then click Stop Jobs.

*T-SQL*

1. In Object Explorer, connect to an instance of Database Engine.

2. On the Standard bar, click New Query.

3. Copy and paste the following example into the query window and click Execute.

      -- stops a job named Weekly Sales Data Backup  
      USE msdb ;  
      GO  

      EXEC dbo.sp_stop_job  
      N'Weekly Sales Data Backup' ;  
      GO

**Disable/enable a job**

*SSMS*

1. In Object Explorer, connect to an instance of the SQL Server Database Engine, and then expand that instance.

2. Expand SQL Server Agent.

3. Expand Jobs, and then right-click the job that you want to disable or enable.

4. To disable a job, click Disable. To enable a job, click Enable.

*T-SQL*

1. In Object Explorer, connect to an instance of Database Engine.

2. On the Standard bar, click New Query.

3. Copy and paste the following example into the query window and click Execute.

      -- changes the name, description, and disables status of the job NightlyBackups.  
      USE msdb ;  
      GO  

      EXEC dbo.sp_update_job  
    @job_name = N'NightlyBackups',  
    @new_name = N'NightlyBackups -- Disabled',  
    @description = N'Nightly backups disabled during server migration.',  
    @enabled = 0 ;  
      GO

### **Create**

**Create a CmdExec Job Step**

- *SSMS*

In Object Explorer, connect to an instance of the SQL Server Database Engine, and then expand that instance.

Expand SQL Server Agent, create a new job or right-click an existing job, and then click Properties.

In the Job Properties dialog, click the Steps page, and then click New.

In the New Job Step dialog, type a job Step name.

In the Type list, choose Operating system (CmdExec).

In Run as list, select the proxy account with the credentials that the job will use. By default, CmdExec job steps run under the context of the SQL Server Agent service account.

In the Process exit code of a successful command box, enter a value from 0 to 999999.

In the Command box, enter the operating system command or executable program. See "Using Transact T-SQL for an example.

Click the Advanced page to set job step options, such as: what action to take if the job step succeeds or fails, how many times SQL Server Agent should try to execute the job step, and the file where SQL Server Agent can write the job step output. Only members of the sysadmin fixed server role can write job step output to an operating system file.

- *T-SQL*

In Object Explorer, connect to an instance of Database Engine.

On the Standard bar, click New Query.

Copy and paste the following example into the query window and click Execute.

      -- creates a job step that uses CmdExec  
      USE msdb;  
      GO  
      EXEC sp_add_jobstep  
            @job_name = N'Weekly Sales Data Backup',  
            @step_name = N'Set database to read only',  
            @subsystem = N'CMDEXEC',  
            @command = 'C:\clickme_scripts\SQL11\PostBOLReorg GetHsX.exe',   
            @retry_attempts = 5,  
            @retry_interval = 5 ;  
      GO


### **Ví dụ**

Cơ sở dữ liệu ShoppingCart có 2 bảng: OrdersGoods (lưu thông tin đơn hàng tại thời điểm hiện tại) và OrdersHistoryGoods (lưu thông tin lịch sử đơn đặt hàng)

Yêu cầu: Tạo một job tự động chạy sau mỗi 1 phút. Đầu tiên, tạo các dữ liệu ramdom vào bảng OrdersGoods. Tiếp theo, thêm các dữ liệu trong bảng OrdersGoods vào bảng OrdersHistoryGoods. Cuối cùng, xóa data trong bảng OrdersGoods. 

- Tạo cơ sở dữ liệu và các thủ tục liên quan:

      -- Tao database ShoppingCart 
      CREATE DATABASE ExpOfScheduleAJob_ShoppingCart;
      GO

      USE ExpOfScheduleAJob_ShoppingCart;
      GO
      --Tao cac table OrdersGoods (thong tin ve hang hoa da dat) và table OrdersHisstoryGoods (thong tin ve lich su order hang hoa)
      CREATE TABLE OrdersGoods
      (
      OrderId INT,
      CustomerId INT,
      Amount INT,
      OrderDate DATETIME
      )
      GO

      CREATE TABLE OrdersHistoryGoods
      (
      OrderId INT,
      CustomerId INT,
      Amount INT,
      OrderDate DATETIME
      )
      GO

      --Procedure xoa data trong table Orders
      CREATE PROCEDURE delete_data_Orders_table
      AS
      DELETE from OrdersGoods; 
      GO

      --procedure tao ramdom data cho table Orders
      CREATE PROCEDURE insert_data_orders_table
      AS
      BEGIN
      DECLARE @OrderId INT, @CustomerId INT, @Amount INT
      SET @OrderId=CAST(100*RAND() AS int)
      SET @CustomerId=CAST(1000*RAND() AS int)
      SET @Amount=CAST(500*RAND() AS int)

      INSERT INTO OrdersGoods VALUES (@OrderId, @CustomerId, @Amount, GETDATE())
      END
      GO

      --procedure cap nhat data tu table orders sang table orderhistory
      CREATE PROCEDURE update_data_OrderHistoty_table
      AS
      INSERT INTO OrdersHistoryGoods SELECT * FROM OrdersGoods
      GO

- Tạo Job:

*Sử dụng SSMS*

1. Trong **Object Explorer**, tại node **SQL Server Agent**, mục **Jobs**, ấn *chuột phải*, chọn **New Job**
2. Xuất hiện hộp thoại New Job. Trong node **General**, đặt tên cho Job tại mục **Name**, chọn Owner của Job, chọn loại Category
3. Trong node **Step**, chọn **New**. Tại node General, đặt tên cho step, chọn **Database** mà step sẽ thao tác, tại **Comand** gõ các câu lệnh mà step sẽ thực hiện. Tại node Advanced, mục On success action chọn hành động tiếp theo sẽ xảy ra nếu step thực hiện thành công (thực hiện bước tiếp theo/quay lại bước đầu tiên/...) và hành động nếu step thực hiện thất bại.Ấn OK
4. Trong node **Schedule**, chọn **New**. Đặt tên cho schedule tại mục name, chọn loại schedule (định kỳ/bắt đầu ngay khi SQL Server Agent bắt đầu/...). Chọn chu kỳ thực hiện job (hàng tuần/hàng ngày). Tại mục duration chọn thười gian bắt đầu, kết thúc. Ấn OK
5. Trở lại hộp thoại New Job, ấn OK
6. Sau khi tạo Job, có thể xem lịch sử thực hiện các step của job bằng cách: Trong **Object Explorer**, tại node **SQL Server Agent**, mục **Jobs**, ấn chuột phải, chọn view history

**Schedule a Job**

Xét 03 cách Schedule (duration = 1 min)

- Tạo dữ liệu cho bảng Orders (success thì chuyển sang bước 2) -> Update dữ liệu từ bảng Orders vào OrdersHistory (success thì chuyển sang bước 3) -> Xóa dữ liệu trong bảng Orders (success thì quay lại bước 1)

Kết quả hiển thị:

Bảng Orders: Mỗi lượt chạy hiển thị 1 dữ liệu (trong 60s có rất nhiều lần bảng orders được tạo dữ liệu rồi lại xóa (lặp vô tận), đến giây thứ 60 thì vừa tạo dữ liệu cuối cùng của chu kỳ)

Bảng OrdersHistory: Kỳ vọng mỗi record là bản ghi của dữ liệu ở bảng orders (cách nhau 1 min). Thực tế: bảng OrdersHistory lưu data của nhiều lần cập nhật trong vòng 1 min (mỗi 1 min, job chạy lại được vài lần rồi, vì bước 3 quay lại bước 1 nên là vòng lặp vô tận).

=> Khắc phục:

- Tạo dữ liệu cho bảng Orders (success thì chuyển sang bước 2) -> Update dữ liệu từ bảng Orders vào OrdersHistory (success thì chuyển sang bước 3) -> Xóa dữ liệu trong bảng Orders (success thì kết thúc Schedule (Go to the next step/Quit the job reporting success))
Kết quả hiển thị:

Bảng Orders: không có dữ liệu nào được hiển thị (vì data cứ được tạo ở bước 1 xong lại bị xóa ở bước 3, chờ hết 1 min lại được tạo ở bước 1 và bị xóa ở bước 3) - không giống kỳ vọng (bảng orders lưu thông tin về lần orders ở thời điểm hiện tại)

Bảng OrdersHistory: mỗi record là dữ liệu ở bảng orders data cách nhau 1 min.

=> Khắc phục:

- Xóa dữ liệu trong bảng Orders -> Tạo dữ liệu cho bảng Orders (success thì chuyển sang bước 3) -> Update dữ liệu từ bảng Orders vào OrdersHistory (success thì kết thúc Schedule (Go to the next step/Quit the job reporting success))

Kết quả hiển thị:

Bảng Orders: Mỗi lượt chạy hiển thị 1 dữ liệu

Bảng OrdersHistory: mỗi record là dữ liệu ở bảng orders data cách nhau 1 min.