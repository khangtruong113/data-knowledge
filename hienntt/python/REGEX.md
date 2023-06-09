# Python 3 Regex Playbook
From [Pluralsight](<https://app.pluralsight.com/course-player?clipId=be89ac2d-0078-41e0-92c9-ecc8fc33883a>)

Nguồn khác: [tra cứu và test regex pattern](https://regex101.com/), [cheat sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/).
<br>
<br>
<br>
**Regex = regular expression**: là một chuỗi các ký tự đặc biệt được định nghĩa để tạo nên các mẫu (pattern) => check xem chuỗi có match với pattern không

**Use cases**:
- Tìm kiếm 1 text file cho một pattern cụ thể (ví dụ .txt)
- Validate data types (ví dụ kiểu số)
- Thay thế một đoạn của chuỗi mà match với pattern

## 1. Regex trong Python
### 1.1. Special character
| Phân loại        | Special character | Cách đọc       | Mô tả                                                                                                             | Ví dụ, note                                                                                                                                                                                                                                                                                                                 |
|:-----------------|:------------------|:---------------|:------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wildcard         | .                 | dot            | Match bất kỳ ký tự nào trừ new line                                                                               | f.n ~ fun, fan                                                                                                                                                                                                                                                                                                              |
| Anchors          | ^                 | caret          | Match phần bắt đầu của chuỗi (mỗi dòng, không phải cả chuỗi)                                                                           | ^Plural ~ Pluralsight                                                                                                                                                                                                                                                                                                       |
| Anchors          | $                 | dollar         | Match phần kết thúc của chuỗi (mỗi dòng, không phải cả chuỗi)                                                     | Sight$ ~ Pluralsight                                                                                                                                                                                                                                                                                                        |
| Escape character | \\                | backslash      | Match ký tự đặc biệt                                                                                              | regex\. ~ I like regex.                                                                                                                                                                                                                                                                                                     |
| Character class  | []                | square bracket | Match 1 ký tự từ một nhóm ký tự (trong character class, chỉ các ký tự đặc biệt ], \, ^, - là có ý nghĩa đặc biệt) | - apologi[sz]e ~ I'd like to apologise<br>- [a-g], [A-G], [a-gA-G]: match 1 ký tự thuộc range<br>- [^abc]: loại trừ ký tự<br>- [0-9] = \d<br>[^0-9] = \D<br>- \s: match ký tự whitespace<br>- \S: match ký tự không phải whitespace<br>- \w: match word characters gồm chữ số và gạch dưới<br>- \W: non-word characters<br> |
| Character group  | ()                | parentheses    | Treat the group as a single unit                                                                                  | (abc), (abc\|def)                                                                                                                                                                                                                                                                                                           |
| Repetition       | +                 | plus           | One or more times                                                                                                 | .+\.txt ~ data.txt, a.txt, 1234.txt                                                                                                                                                                                                                                                                                         |
| Repetition       | *                 | asterisk       | Zero or more times                                                                                                | .*\.txt ~ data.txt, a.txt, .txt                                                                                                                                                                                                                                                                                             |
| Repetition       | ?                 | question mark  | Zero or one                                                                                                       | colou?r ~ color, colour                                                                                                                                                                                                                                                                                                     |
| Repetition       | {n}               | curly bracket  | Xuất hiện chính xác bao nhiêu lần                                                                                 | - (ha){2} ~ haha<br>- ^#((\d\|[A-Fa-f]){3}){1,2}$ ~ match bất cứ một hex color code, vd: #EBB8DD,#F88                                                                                                                                                                                                                       |
| Repetition       | {n,m}             | curly bracket  | Xuất hiện chính từ bao nhiêu đến bao nhiêu lần                                                                    | (ha){2,5} ~ hahaha                                                                                                                                                                                                                                                                                                          |

### 1.2. Python functions
| Function  | Syntax                                                                                                     | Mô tả                                                                                                                                      |
|:----------|:-----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| search    | search(pattern, string to be searched, optional flags)                                                     | Scan chuỗi và tìm first match, trả về none nếu không match hoặc nếu match sẽ in ra phần match                                              |
| match     | match(pattern, string to be searched, optional flags)                                                      | Check xem phần bắt đầu của chuỗi có match với pattern không                                                                                |
| fullmatch | fullmatch(pattern, string to be searched, optional flags)                                                  | Check xem full string có match với pattern không                                                                                           |
| findall   | findall(pattern, string to be searched, optional flags)                                                    | Search string cho các match non-overlapping (không nối chồng)                                                                              |
| sub/subn  | sub/subn(pattern, replacement, string to be searched, optional max number of replacements, optional flags) | Search string cho tất cả các match non-overlapping và thay thế chúng. Subn khác sub ở chỗ sẽ trả về một tuple gồm chuỗi và số replacements |
| split     | split(pattern, string, optional max number of split, optional flags)                                       | Split string ở mọi chỗ có pattern, trả về list                                                                                             |
| escape    | escape(pattern)                                                                                            | Làm ký tự đặc biệt regex thành ký tự đặc biệt đúng nghĩa                                                                                   |
| compile   | compile(pattern)                                                                                           | Biên dịch 1 pattern thành 1 regex object                                                                                                   |
_Xem ví dụ thực hành tại file REGEX.md_

### 1.3. Match object
| Syntax   | Mô tả                                                                                                |
|:---------|:-----------------------------------------------------------------------------------------------------|
| string() | Trả về original string mà match pattern                                                              |
| group()  | Trả về string mà match regex pattern, nếu có nhiều group có thể thêm số vào đằng sau để lấy ra group |
| groups() | Trả về tuple chứa tất cả string match regex pattern                                                  |
| start()  | Trả về vị trí bắt đầu của phần match                                                                 |
| end()    | Trả về vị trí kết thúc của phần match                                                                |
| span()   | Bao gồm cả vị trí bắt đầu và kết thúc của phần match                                                 |
_Xem ví dụ thực hành tại file REGEX.md_

### 1.4. Flags
| Syntax1       | Syntax2 | Mô tả                                                                                                                            |
|:--------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------|
| re.IGNORECASE | re.I    | Bỏ phân biệt hoa thường                                                                                                          |
| re.DOTALL     | re.S    | Match bất kỳ ký tự nào kể cả new line                                                                                            |
| re.MULTILINE  |         | Nếu như ^ và $ chỉ match với mỗi dòng chứ không phải cả chuỗi thì khi dùng multiline sẽ check được cả chuỗi kể cả khi có newline |

