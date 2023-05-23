# Vagrant Repositories
Đây là folder chứa các Vagrant Repository và hướng dẫn sử dụng cơ bản

## 1. MS SQL Server 2019 - Ubuntu 20.04
### Mô tả chung
- OS: Ubuntu 20.04
- Service: MS SQL Server 2019
### Default setting
- Address: 10.10.10.10 (host-only network)
- Port Database: 1433
- username: delabs
- password: H1z1@#2022
### Hướng dẫn
- cd vào thư mục chứa Vagrantfile (ví dụ: `ms_sql_server_ubuntu_20.04`)
```
cd ms_sql_server_ubuntu_20.04
```
- Tạo và chạy VM: 
```
vagrant up
```
- Remote vào VM:
```
vagrant ssh
```
- Xóa VM
```
vagrant destroy
```
- Truy cập vào database theo default setting