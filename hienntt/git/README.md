# Git
Hệ thống quản lý phiên bản phân tán - Distributed Version Control System (DVCS)

Tải về và cài đặt: [Download](https://git-scm.com/downloads)

Kiểm tra phiên bản Git:

    git --version

Hiển thị các lệnh Git:

    git --help

## 1. Configure Git
Thiết lập tên: 
    
    git config --global user.name "Tên của Bạn"

Thiết lập tên: 
    
    git config --global user.email emailcuaban@domain.com

Hiển thị các tham số thiết lập Git:

    git config --list

## 2. Basic Commands

- File Stages:

![File Stages](https://git-scm.com/book/en/v2/images/lifecycle.png)

- Working Area:

![Working Area](https://www.i2tutorials.com/wp-content/media/2023/02/work2.png)

| Command                                   | Mô tả                                                                                                                                                                  | Lưu ý                                                                                                                                                                                         | 
|:------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```git init```                            | Khởi tạo 1 kho chứa Git mới (Git repository) ở local                                                                                                                   | Chạy xong thì nó sẽ tạo ra một thư mục con (ẩn) tên .git, thư mục này chứa tất cả thông tin mô tả cho kho chứa dự án (Repo) mới                                                               |
| ```git add .```                           | Bắt đầu theo dõi, chuyển những file có thay đổi từ Working Directory vào Staging Area                                                                                  |                                                                                                                                                                                               |
| ```git commit -m "Message"```             | Chuyển những file có thay đổi từ Staging Area vào CSDL Git                                                                                                             |                                                                                                                                                                                               |
| ```git status```                          | Kiểm tra trạng thái các file khi có sửa đổi                                                                                                                            | - new file (untracked): file mới tạo<br/>- modified: đã bị sửa đổi và vẫn ở trong Working Directory<br/>- staged: đã đưa vào Staging Area<br/>- committed: đã được commit và lưu vào CSDL Git |
| ```git log```                             | Kiểm tra các lần commit                                                                                                                                                |                                                                                                                                                                                               |
| ```git log -2```                          | Kiểm tra 2 lần commit gần nhất                                                                                                                                         |                                                                                                                                                                                               |
| ```git log -p```                          | Hiển thị chi tiết thay đổi của từng commit                                                                                                                             |                                                                                                                                                                                               |
| ```git log --oneline --graph```           | Kiểm tra rút gọn các lần commit trên local (xem sơ đồ các nhánh)                                                                                                       |                                                                                                                                                                                               |
| ```git log -- oneline origin/master```    | Kiểm tra rút gọn các lần commit trên remote                                                                                                                            |                                                                                                                                                                                               |
| ```git diff```                            | Kiểm tra sự thay đổi thư mục làm việc so với commit cuối                                                                                                               |                                                                                                                                                                                               |
| ```git diff --staged```                   | Kiểm tra sự thay đổi của index (staging) với commit cuối                                                                                                               |                                                                                                                                                                                               |
| ```git diff hash-commit1 hash-commit2```  | Kiểm tra thay đổi giữa hai commit                                                                                                                                      |                                                                                                                                                                                               |
| ```git restore .```                       | Phục hồi lại tất cả các file vừa xóa từ lần commit gần nhất                                                                                                            |                                                                                                                                                                                               |
| ```git restore filename```                | Phục hồi lại file chỉ định từ commit gần nhất                                                                                                                          |                                                                                                                                                                                               |
| ```git restore --staged .```              | Đưa các file từ staged về modified                                                                                                                                     |                                                                                                                                                                                               |
| ```git checkout -- .```                   | Phục hồi tất cả các file                                                                                                                                               |                                                                                                                                                                                               |
| ```git checkout commit_hash --filename``` | Phục hồi lại file chỉ định từ commit chỉ định                                                                                                                          |                                                                                                                                                                                               |
| ```git reset --soft HEAD~1```             | Hủy commit cuối, con trỏ HEAD sẽ chuyển về commit cha. Đồng thời những thay đổi của commit cuối được chuyển vào vùng staging nhằm để có cơ hội commit lại hoặc sửa đổi |                                                                                                                                                                                               |
| ```git reset --hard HEAD~1```             | Kết quả giống với dùng tham số --soft, chỉ có một khác biết là nội dung thay đổi của commit cuối không đưa đưa vào staging mà bị hủy luôn                              |                                                                                                                                                                                               |
| ```git reset```                           | Hủy git add khi đã cập nhật thay đổi vào vùng staging                                                                                                                  |                                                                                                                                                                                               |
| ```git reset --filename```                | Hủy đưa một file vào staging                                                                                                                                           |                                                                                                                                                                                               |

### Working with Remote Origin
| Command                                     | Mô tả                                                                             | Lưu ý                                                                                                                           | 
|:--------------------------------------------|:----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| ```git remote```                            | Check các remote đang có                                                          |                                                                                                                                 |
| ```git remote```                            | Check các remote đang có                                                          |                                                                                                                                 |
| ```git remote -v```                         | Xem chi tiết kết nối đang có                                                      |                                                                                                                                 |
| ```git remote add origin path```            | Tạo thêm kết nối                                                                  | Trong 1 local repo có thể tạo nhiều remote                                                                                      |
| ```git remote rm xyz```                     | Xóa kết nối                                                                       |                                                                                                                                 |
| ```git push -u origin master```             | Push từ local lên server                                                          | Thêm -u trong lần đầu push để tạo ra upstream, lần sau push thì chỉ cần git push là sẽ up lên remote origin nhánh master        |
| ```git push origin --all```                 | Push tất cả các branch của remote origin lên                                      |                                                                                                                                 |
| ```git push origin xyz```                   | Push commit ở nhánh _xyz_ của remote origin lên                                   |                                                                                                                                 |
| ```git push --delete origin xyz```          | Xóa nhánh _xyz_ ở remote origin                                                   |                                                                                                                                 |
| ```git clone git clone path-git path-des``` | Copy Repo từ thư mục này sang thư mục khác                                        |                                                                                                                                 |
| ```git clone user@host:/path/to/repo.git``` | Copy Repo từ server về bằng giao thức ssh                                         |                                                                                                                                 |
| ```git clone url-repo```                    | Copy Repo bằng giao thức https                                                    | VD: Kết nối với GitHub, đã tự tạo remote rồi                                                                                    |
| ```git fetch origin```                      | Xem để cập nhật các thông tin mới có từ remote                                    |                                                                                                                                 |
| ```git pull origin master```                | Cập nhật từ remote origin cho nhánh master                                        |                                                                                                                                 |

### Working with Branches
| Command                        | Mô tả                                                  | Lưu ý                                                                                                                                     |
|:-------------------------------|:-------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| ```git branch```               | Check các branch đang có trên local                    |                                                                                                                                           |
| ```git branch -a```            | Check các branch đang có trên remote                   |                                                                                                                                           |
| ```git branch alpha```         | Tạo nhánh mới đặt tên là _alpha_                       |                                                                                                                                           |
| ```git branch -d alpha```      | Xóa nhánh _alpha_                                      |                                                                                                                                           |
| ```git checkout alpha```       | Chuyển sang làm việc ở nhánh _alpha_                   |                                                                                                                                           |
| ```git switch master```        | Chuyển về nhánh master                                 | Tương tự git checkout                                                                                                                     |
| ```git merge aplha```          | Gộp nhánh _alpha_ vào nhánh con trỏ HEAD đang chỉ tới  | Nếu xung đột thì mở file xung đột ra xem lấy phiên bản nào Accept Both Changes/Current Change/Incoming Change -> git add . -> git commit  |
| ```git merge --abort```        | Quay về trạng thái trước khi gộp nhánh khi có xung đột |                                                                                                                                           |
| ```git mergetool```            | Xem trạng thái xung đột                                |                                                                                                                                           |
| ```git checkout hash-commit``` | Về commit có mã hash đó                                |                                                                                                                                           |

## 3. Notes

- Khi muốn untrack các file thì tạo file _.gitignore_ ở thư mục chính rồi add các tên file không cần theo dõi vào
- Nếu file/folder được tạo ra trước _.gitignore_ rồi thì sau đó sẽ không tự được untrack, phải dùng các câu sau đây để untrack:
```
git rm -r --cached ..\..\..\.idea
git commit -m 'untrack .idea folder'
```