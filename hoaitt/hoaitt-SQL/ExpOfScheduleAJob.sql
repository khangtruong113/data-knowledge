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

-- Our business requirement is to create a job that will run every 1 minute. 
-- first, it will insert all the records which are present in the Orders table into the OrdersHistory table
-- and then it will delete all the records from the Orders table.

Select * from OrdersGoods;
Select * from OrdersHistoryGoods;

delete from OrdersGoods;
delete from OrdersHistoryGoods;