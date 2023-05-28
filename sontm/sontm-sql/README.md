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

