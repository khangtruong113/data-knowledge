# Python file để viết script tạo bảng trong SQL theo fiel .xlsx cung cấp thông tin về bảng dim

Run python file sẽ tạo file .sql ngay trong thư mục chứa file python và thông báo số lượng bảng sẽ được tạo ra

**Excel file convention**
- Chứa 2 sheets: "Danh sách bảng dim" và "Cấu trúc bảng dim"
    + "Danh sách bảng dim" có: 
        + Cột C chứa tên bảng
        + Cột D chứa tên schema tương ứng
        + Giá trị tại các cột khác không ảnh hưởng đến kết quả)
    + "Cấu trúc bảng dim" có: 
        + Cột A chứa tên trường 
        + Cột B chứa Kiểu dữ liệu tương ứng
        + Cột C thể hiện dữ liệu có được phép rỗng hay không (nếu trống, thì được phép rồng, nếu có giá trị 'x' thì không được phép rỗng)
        + Cột D thể hiện trường đó có phải primary key hay không (nếu có giá trị 'P', thì trường là primary key)
        + Giá trị tại các cột khác không ảnh hưởng đến kết quả
        + Các hàng có cấu trúc lặp lại: Bảng tên_bảng -> Dòng tiêu đề (Tên trường, Kiểu dữ liệu, Rỗng?, P/K key?)

        |Bảng tên_bảng|  |  |  |
        |----------|--------|---------|--------|

        |Tên trường|Kiểu dữ liệu|Rỗng?|P/F Key?|
        |----------|--------|---------|--------|
        |id|int||P|
        |so_van_ban|nvarchar(500)|||
        |...|...|...|...|
        
        |Bảng tên_bảng|  |  |  |
        |----------|--------|---------|--------|

        |Tên trường|Kiểu dữ liệu|Rỗng?|P/F Key?|
        |----------|--------|---------|--------|
        |...|...|...|...|

- Thứ tự các bảng trong sheet 'Danh sách bảng dim' và 'Cấu trúc bảng dim' không cần phải giống nhau. Function sẽ match tên bảng trong sheet 'Danh sách bảng dim' và 'Cấu trúc bảng dim' để viết script tạo bảng

- Do đó, các bảng chỉ được tạo ra nếu có tên (giống nhau) trong cả hai sheet
- File excel mẫu được đính kèm: 'Dim_Fact_Listing_09072022.xlsx'





