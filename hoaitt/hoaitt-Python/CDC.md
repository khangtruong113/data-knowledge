# CDC - Change data capture

CDC - **ghi lại các hoạt động của database khi các table và row bị modified**. 

CDC thường có sẵn trong Azure SQL database, SQL server và Azure SQL managed instance.

## Overview

CDC sử dụng **SQL agent** để ghi lại hoạt động insert, update, delete được thực hiện với table. 

Cần có Column information và metadata để apply những thay đổi cho target inviroment được ghi lại cho các hàng bị chỉnh sửa và được lưu trong các change table phản ánh cấu trúc cột của các source table bị theo dõi. Table-valued function được cung cấp để cho phép truy cập có hệ thống vào các change data của consumer.

Ví dụ về data consumer mà kỹ thuật này hướng đến là ứng dụng ETL (extract, transform, load). Một ứng dụng ETL từng bước một load change data từ SQL Server source table tới một data warehouse hoặc data mart. Mặc dù biểu diễn của các source table trong data warehouse phải phản ánh những thay đổi trong source table, nhưng một kỹ thuật đầu cuối refresh một replica của source là không phù hợp. Thay vào đó, cần một luồng change data đáng tin cậy được cấu trúc để các consumer có thể apply nó cho các biểu diễn target khác nhau của data.

## Data flow

Hình minh họa sau cho thấy data flow cơ bản của CDC:

![CDC_flow](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/media/cdcdataflow.gif?view=sql-server-ver16)

Nguồn **change data** của CDC là **SQL server transaction log**. Khi các hành động insert, update và delete được áp dụng với các source table được theo dõi, các mục mô tả các thay đổi đó được thêm vào log. **Log server** như là **input** của **quá trình capture**. Nó đọc log và thêm thông tin về các thay đổi của các change table liên quan của table bị theo dõi. Các function được cung cấp để liệt kê các thay đổi xuất hiện trong các change table trên một phạm vi chỉ định, trả về thông tin theo dạng của tập kết quả được lọc. Tập kết quả được lọc thường được sử dụng bởi một quy trình ứng dụng để cập nhật representation của source trong một vài môi trường bên ngoài.

## Capture instance

Trước khi các thay đổi trong bất kỳ một table nào của database có thể được theo dõi, CDC phải được **enable** cho database. Điều này được thực hiện bằng cách sử dụng stored procedure **sys.sp_cdc_enable_db**. Khi database được enable, source table có thể được coi như là các table được theo dõi bởi stored procedure *sys.sp_cdc_enable_table*. Khi đó, một capture instance liên quan được tạo ra để hỗ trợ việc lan truyền change data trong source table. Capture instance bao gồm một change table và tối đa 02 query function. Metadata mô tả cấu hình chi tiết của capture instance được giữ lại trong bảng CDC metadata **cdc.change_table, cdc.index_columns, cdc.captured_columns**. Các thông tin này có thể lấy được bằng cách sử dụng stored procedure *sys.sp_cdc_help_change_data_capture*.

Tất cả các object liên quan đến capture instance được tạo ra trong CDC schema của database được enable. Các yêu cầu của tên capture instance là một object name hợp lệ, phải là duy nhất trong các database capture instance. Mặc định, tên là <schema name_table name> của source table. Change table liên quan tới nó được đặt tên bằng cách thêm _CT vào teen capture instance name. Function được dùng để truy vấn các thay đổi đưọc đặt tên bằng cách thêm vào trước fn_cdc_get_all_changes_ tên của instance name. Nếu capture instance được cấu hình để hỗ trợ net changes, function truy vấn net_changes cũng được tạo và đặt tên bằng cách thêm vào trước fn_cdc_get_net_changes_ tên của capture instance.

## Change table

5 cột đầu tiên của CDC change table là các cột metadata. Nó cung cấp thông tin bổ sung liên quan tới các thay đổi được ghi lại. Các cột còn lại phản ảnh các cột được capture (đã xác nhận) từ source table theo tên, và thường theo type. Các cột này lưu trữ capture column data được gom lại từ các source table.

Mỗi hành động insert hoặc delete được apply cho source table xuất hiện như một row trong change table. Data column của row trả kết quả từ hành động insert chứa các column value sau khi insert. Các data column của row trả kết quả tuef hành động delete chứa các column value trước khi delete. Hành động update yêu cầu one-row entry để xác định các column value trước khi update, và row entry thứ hai để xác định column value sau khi update.

Mỗi row trong change table cũng chứa metadata bổ sung cho phép giải thích các hoạt động thay đổi. 
- Column __&start_lsn xác định commit lod sequence number (LSN) được gán cho thay đổi.
- Column __$seqval được sử dụng để yêu cầu nhiều sự thay đổi xảy ra trong cùng một transaction
- Column __$operation ghi lại các hoạt động liên quan đến thay đổi: 1 = delete, 2 = insert, 3 = update (before image), and 4 = update (after image)
- Column __$update _mask là một variable bit mask với một được định nghĩa là bit cho mỗi cột được capture. Với insert và delete, update mask luôn có tất cả bit set. Tuy nhiên, update row sẽ chỉ có những bit set tương ứng với các column đã thay đổi.

## Validity interval

CDC validity interval của một database là thời gian xuyên suốt change dât sẵn có cho capture instance. Validity interval bắt đầu khi capture instance đầu tiên được tạo ra cho database table, và tiếp tục tới hiện tại.
### Database

Data được tích góp trong change table sẽ phát triển không theo hệ thống nếu không 'cắt tỉa' data một cách định kỳ và có hệ thống. Quá trình CDC cleanup có trách nhiệm thực thi các chính sách cleanup retention-based. Đầu tiên, nó loại bỏ endpoint thấp của validity interval để đáp ứng giới hạn thời gian. Sau đó, nó loại bỏ các các change table entry hết hạn. Mặc định, ba ngày của data được giữ lại.

# Enable & disable CDC

## Enable

Trước khi capture instance được tạo cho các table riêng biệt, một thành viên sysadmin fixed server role (chỉ trên SQL Server/Azure SQL Managed Instance) hoặc db_owner phải enable đầu tieen database cho CDC. Điều này được thực hiện bằng cách run sys.sp_cdc_enable_db (Transact-SQL) trong database. Để xác định xem database đã được enable chưa, truy vấn is_cdc_enabled trong sys.database.

Khi một database được enable cho CDC, cdc schema, cdc user, metadata tables và các object hệ thống khác được tạo cho database. cdc schema chứa các CDC metadata table và sau đó các source table được enable cho CDC, mỗi change table serve là một repository cho change data. cdc schema cũng chứa các system function liên quan được sử dụng để truy vấn change data.

CDC yêu cầu cả cdc schema và cdc user. Nếu shema hoặc database user được đặt tên cdc đang tồn tại trong database, db khôn gtheer enable CDC cho đến khi schema hoặc user bị bỏ hoặc rename

Lưu ý:

Để định vị template trong SQL Server management studio, chọn View, click Template Explorer và chọn SQL Server Templates. change data capture như một sub-folder.
~~~
-- ====  
-- Enable Database for CDC template   
-- ====  
USE MyDB  
GO  
EXEC sys.sp_cdc_enable_db  
GO
~~~

## Disable 

disabling db loại bỏ tất cả các CDC metadata liên quan, bao gồm cdc user và schema và CDC job. Tuy nhiên, bất kỳ gating roles nào được tạo bởi CDC sẽ không được loại bỏ tự động mà cần được delete riêng. 

Nếu database đã được enable CDC bị bỏ, CDC job cũng tự động bị loại bỏ.

    -- =======  
    -- Disable Database for change data capture template   
    -- =======  
    USE MyDB  
    GO  
    EXEC sys.sp_cdc_disable_db  
    GO

## Enable for a table

Sau khi database được enable CDC, thành viên của **db_owner** được fix **database role** có thể tạo một **capture instance** cho từng source table bằng cách dùng sp **sys.sp_cdc_enable_table**. Để xem liệu source table đã được enable cho CDC chưa, thử **is_tracked_by_cdc** column trong sys.tables.

**Columns in the source table to be captured**: mặc định tất cả các column trong source table được coi là các column được capture. Nếu chỉ cần theo dõi một tập các column (vì lý do riêng hoặc do hiệu suất), sử dụng  @captured_column_list để chỉ định các tập column cần theo dõi.

**A filegroup to contain the change table**

Mặc định, change table được đặt trong filegroup mặc định của database. Database owner muốn kiểm soát nơi đặt các change table có thể sử dụng thông số @filegroup_name để chỉ định filegroup cụ thể cho change table liên quan đến capture instance. Các filegroup được gọi tên phải đã tồn tại. Thông thường, khuyến nghị change table được đặt trong filegroup riêng biệt với source table.

    -- =========  
    -- Enable a Table Specifying Filegroup Option Template  
    -- =========  
    USE MyDB  
    GO  
    
    EXEC sys.sp_cdc_enable_table  
    @source_schema = N'dbo',  
    @source_name   = N'MyTable',  
    @role_name     = N'MyRole',  
    @filegroup_name = N'MyDB_CT',  
    @supports_net_changes = 1  
    GO

## Disable for a table

Thành viên của db_owner fixed database role có thể loại bỏ capture instance cho mỗi source table bằng cách dùng sys.sp_cdc_disable_table. Để xem một source table hiện tại đã được enable CDC chưa, thử is_tracked_by_cdc trong sys,table. Nếu không có table được enable cho database sau khi disabling, cdc job cũng đã được removed.

Nếu cdc-enable bị bỏ, cdc metadata liên quan cũng tự động bị bỏ.

    -- =====  
    -- Disable a Capture Instance for a Table template   
    -- =====  
    USE MyDB  
    GO  
    EXEC sys.sp_cdc_disable_table  
    @source_schema = N'dbo',  
    @source_name   = N'MyTable',  
    @capture_instance = N'dbo_MyTable'  
    GO

# Capture job

Capture job được bắt đầu bằng cách run sp_MScdc_capture_job, store procedure này bắt đầu bằng việc trích xuất các giá trị được cài đặt cho maxtrans, maxscans, continous, và pollinginterval từ msdb.dbo.cdc_jobs

**Parameters**

## maxtrans

Cho biết số transaction tối đa có thê xử lý trong mỗi lần scan log. Nếu trong mỗi lần scan, số lượng transaction sẽ sử lý vượt quá giới hạn, sẽ không có trans nào được thêm vào scan hiện tại. Sau khi chu trình scan hoàn thành, số lượng trans đã xử lý sẽ luôn ít hơn hoặc bằng maxtrans.

## maxscans 

Chỉ ra số lượng chu trình scan tối đa cố gắng để drain log trước khi cái khác returning (nếu không thiết lập continous) hoặc chở đề thực thi (nếu thiết lập continous)

## continous

Kiểm soát xem sp_cdc_scan có tiếp tiệp run cho đến khi bị dừng (chế độ continous)

## One-shot mode

Trong chế độ One-shot, capture job yêu cầu sp_cdc_scan thực hiện tối đa maxtrans scan để cố gắng drain log và return. Bất kỳ trans nào hơn maxtrans đang hiệ diện trong log sẽ được xử lý trong scan sau.

One-shot mode không được khuyến nghị cho mục đích sản xuất, vì nó dựa trên job schedule để quản lý tần suất chu trình scan được run.

### Continous mode and polling interval

capture job yêu cầu sp_cdc_scan run liên tục, điều này cho phép sp quản lý chính vòng lặp đợi của nó bằng cách cung cấp không chỉ maxtrans và maxscan mà còn có số giây giữa quá trình log (polling interval). Trong chế độ này, capture job luôn active, thực thi WAITFOR giữa log scanning.

# Cleanup jobS

## Strucutre

Khởi đầu bằng cách run sp_MScdc_cleanup_job, bắt đầu bằng cách thiết lập retention: thời gian tối đa trans được lưu giữ thông tin trước khi cleanup và threshold: số trans bị bỏ mỗi lần cleanup. 