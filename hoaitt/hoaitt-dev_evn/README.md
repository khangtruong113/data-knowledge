# Install Vagrant in Windows

- Vagrant là ứng dụng hỗ trợ người dùng *tạo ra các máy ảo* trên máy tính *theo nhu cầu* của họ, quản lý toàn bộ máy ảo* bằng các lệnh, hỗ trợ các **box** (một gói hệ điều hành với các thiết lập riêng biệt). Đặc biệt là cho phép chuyển thiết lập các máy ảo trong máy mình sang một máy khác (re-package)/cho phép các thành viên trong team truy cập vào thư mục riêng trên máy chủ mà không cần cài đặt thêm gì.

- Để sử dụng Vagrant, cần cài đặt máy ảo trước (![VirtualBox]() or [VMare])

- Các thao tác ở vagrant đều thông qua lệnh (dùng Git Bash/cmd với Window, Terminal đối với Linux)

- Khi dùng Vagrant, cần tạo một thư mục riêng cho mỗi máy ảo (mỗi thư mục này sẽ chứa các thiết lập cho một máy ảo)

> Cách cài đặt Vagrant

- Bước 1: Cài đặt VirtualBox/VMare

- Bước 2: Cài đặt Git Bash 

- Bước 3: Cài đặt Vagrant

  + Truy cập website (https://www.vagrantup.com/downloads) và tải gói cài đặt tương ứng với hệ điều hành

  + Cài đặt như một phần mềm bình thường và khởi động lại máy tính

# Một số khái niệm

- **Vagrant Box**: gói hệ điều hành đã cài sẵn một số ứng dụng cần thiết (VD: box Ubuntu 12.04 có sẵn LAMP), tải các box về máy sẵn, sau đó bạn có thể sử dụng box đã tải cho các máy ảo tùy thích

- **Packer** : tool to create image, [here] (https://learn.hashicorp.com/tutorials/packer/getting-started-build-image)

- **Vagrantfile** : là tập tin cấu hình mà Vagrant dùng để triển khai và cấu hình các máy ảo

- **Provider** : là phần mềm máy ảo cho phép Vagrant triển khai các máy ảo trên đó. Như VirtualBox, VMware, Hyper-V, Docker

- **Provisioner** : Một khi máy ảo được triển khai, Provisionner sẽ khởi động tiến trình cài đặt và cấu hình tự động cho các máy ảo bằng: Script Shell, Ansible... 

# Cài đặt và xác định box

Sau khi cài đặt Vagrant sẽ không có box sẵn mà cần tải về để sử dụng ([danh sách các box](https://vagrantcloud.com/discover/featured))

```vagrant box add [tên box muốn sử dụng]```

Sau đó, chọn ứng dụng sẽ sử dụng box (nếu là VirtualBox thì gõ số 1 và Enter)

* Để kiểm tra danh sách các box

```vagrant box list```

# Tạo máy ảo mới

- Tạo thư mục riêng cho máy ảo mới

```mkdir [tên thư mục]```

*(Thư mục tạo ra mặc định nằm ở C:\Users\Tên-User\(Windows))*

- Truy cập vào thư mục vừa tạo

```cd [tên thư mục]```

- Xem đường dẫn thư mục đang truy cập

```pwd```

- Truy cập vào thư mục xong, cài đặt máy ảo mới bằng lệnh

```vagrant init [tên box]```

- Khởi động máy ảo

```vagrant up```

- Truy cập vào máy ảo vừa khởi động

```vagrant ssh```

# Một số lệnh cơ bản khác

* vagrant suspend: Để máy ảo tạm nghỉ

* vagrant halt: Shutdown máy ảo

*vagrant login: Đăng nhặp vào hệ thống vagrant cloud

*ᴠagrant ѕhare --ѕѕh: Chia ѕẻ máу ảo của bạn cho người khác truу cập, (gõ lệnh ᴠagrant login trước khi dùng tính năng nàу)

# Vagrant share

- Chia sẻ vagrant bằng lệnh:

```vagrant share```

- Có 3 mode chính:

  + HTTP sharing: Tạo một URL dẫn tới Vagrant environment. Người sử dụng URL này không cần cài đặt Vagrant 

  + SSH sharing: cho phép SSH truy cập Vagrant environment ở remote:
  
     ```vagrant connect --ssh```

  + General sharing: cho phép bất kỳ ai truy cập vào bất kỳ exposed port của Vagrant environment ở phía remote bằng lệnh:
   
     ```vagrant connect```

# Synced folder

Muốn đồng bộ tệp tin ở folder trên local và folder trên máy áo: Trong vagrant file:

```config.ᴠm.ѕуnced_folder "../[folder trên locla]", "/[folder trên máy ảo]```

# Provisioning

khi bật máy lên lần đầu, vagrant sẽ thực hiện việc cài đặt các phần mềm cho máy của bạn theo những gì bạn thiết lập. Phương pháp đơn giản và cổ điển nhất là sử dụng shell script. 

*Ví dụ, muốn cài đặt git ngay khi bật máy lần đầu, tại Vagrantfile:*

    config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get install git
    SHELL

# Networking

config network để có thể access vào máy ảo và chạy website của mình. 

Tại vagrant fiel:

```config.vm.network :forwarded_port, host: 4567, guest: 80```

//access đến cổng 4567 của máy chủ sẽ được chuyển đến cổng 80 của máy ảo

