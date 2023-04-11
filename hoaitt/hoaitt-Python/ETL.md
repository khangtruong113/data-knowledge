# ETL (extract - transform - load)

**Extract**: thu thập data từ nhiều nguồn khác nhau.

**Transform**: biến đổi data được trích xuất thành biểu mẫu để có thể đặt vào cơ sở dũ liệu khác

- Cleaning
- Normalize
- Deduplicate
- Conform
- Arrange

**Load**: ghi chép data vào cơ sở dữ liệu đích.

- Load toàn bộ: khó bảo trì
- Load tăng dần: dễ quản lý

![ETL_process](https://websitehcm.com/wp-content/uploads/2022/02/image-352.png.webp)

Đầu tiên, ETL trích xuất dữ liệu từ các nguồn dữ liệu đồng nhất hoặc không đồng nhất. 

Tiếp theo, nó gửi dữ liệu vào một khu vực lưu trữ các thay đổi trên tập tin (staging area). 

Từ đó, dữ liệu trải qua quá trình làm sạch, làm giàu, chuyển đổi, và cuối cùng được lưu trữ trong kho dữ liệu.

# Batch ETL

![batch](https://uploads-ssl.webflow.com/5e3a6b6029e8b285ad11a875/5ea01d3433a17b181dca2e6d_88072419_131058701758787_5661524966445678592_n.jpeg)

Dữ liệu mới được sinh ra sẽ được gom thành các batch, sau đó sẽ được xử lý.

Hai cách phổ biến để xác định khi nào các batch này sẽ được xử lý là:

- Dựa trên một khoảng thời gian nhất định. Ví dụ: cứ 60 phút xử lý một lần
- Dựa trên một số điều kiện nhất định. Ví dụ: cứ thu thập đủ 50 files dữ liệu sẽ xử lý một lần, hay cứ thu thập đủ 100G dữ liệu sẽ xử lý một lần, …

# Streaming ETL

![stream](https://uploads-ssl.webflow.com/5e3a6b6029e8b285ad11a875/5ea01d34df8913baf8b99714_87889087_131059325092058_6775830312720007168_n.jpeg)

Dữ liệu sẽ được xử lý ngay khi đến, sẽ được xử lý ngay khi dữ liệu được phát sinh. 

Tuy nhiên, rất nhiều hệ thống hiện nay hỗ trợ khái niệm cửa sổ (window) trong stream processing (Window là khoảng thời gian trước và sau thời điểm hiện tại khi dữ liệu xuất hiện)