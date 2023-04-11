# Table of contents
- [Table of contents](#table-of-contents)
    - [Tổng quan](#tổng-quan)
    - [Cài đặt](#cài-đặt)
    - [Các khái niệm cơ bản](#các-khái-niệm-cơ-bản)
    - [DBT project](#dbt-project)
    - [DBT deployment](#dbt-deployment)

Source: [getdbt](https://docs.getdbt.com/docs)

DBT products gồm: dbt Cloud và dbt Core.\
Phạm vi tìm hiểu: dbt Core.

## Tổng quan
Sửa các file sử dụng code editor (locally), run project sử dụng CLI
## Cài đặt (pip install)
- Tạo project (Visual studio code/Pycharm)
- Tại terminal:

*Install dbt Core:*\
``pip install dbt-core`` \
hoặc\
``pip install --upgrade dbt-core`` (cài đặt version mới nhất)\
hoặc\
``pip install --upgrade dbt-core==0.19.0`` (cài đặt version 0.19.0)

*Install Sqlserver adapter:*\
``pip install dbt-sqlserver``
## DBT project
### **Khởi tạo dbt project**
Terminal: ``dbt init``\
Nhập tên project. Ví dụ: MOHA

**MOHA**\
├── **analysis**\
├── **dbt_packages**\
├── **logs**\
├── **macros**\
│   └── compare_table_on_grc_madv_kydulieu.yml\
├── **models**\
│   ├── olap\
│   │   └── logs\
│   │       ├── dbt.log\
│   ├── schema.yml\
│   ├── ubnd.sql\
├── **seeds**\
├── **snapshots**\
├── **target**\
└── **tests**\
├── *packages.yml*\
├── *dbt_project.yml*\
├── *README.md*

Tổ chức project bằng ***dbt_project.yml*** file.\
Một project gồm các resource sau:
|Resource|Mô tả|
|--|--|
|models| Mỗi model ở một file duy nhất, transform raw data thành dataset (để phân tích)|
|snapshots|Capture mutable tables (có thể refer lại sau đó)|
|seeds| CSV file (để load vào data platform (Database) bằng dbt)|
|tests| SQL queries để test models/resources trong project|
|macros| Blocks of code được sử dụng nhiều lần|
|docs| Docs của project|
|exposures| Định nghĩa và mô tả downstream use|
|metrics| Định nghĩa metric|
|analysis|Tổ chức các câu truy vấn phân tích|

**Cấu hình project**

Mỗi dbt project có một file cấu hình (*dbt_project.yml*) - để định nghĩa directory của project và các cấu hình khác.
|YMLkey|Mô tả|
|--|--|
|name| Tên project|
|version| Version của project|
|require-dbt-version| Đảm bảo project sẽ chỉ hoạt động trong một dải dbt-core version|
|profile|profile mà dbt sử dụng để connect tới data platform (database), profile chứa các cấu hình của data platform (host, port, user name, password, ...)|
|model-paths| Directoies tới nơi mà model và source được lưu trữ|
|seed-paths| Directoies tới nơi mà seed files được lưu trữ|
|test-paths| Directoies tới nơi mà test files được lưu trữ|
|analysis-paths| Directoies tới nơi mà analysis files được lưu trữ|
|macro-paths| Directoies tới nơi mà macro được lưu trữ|
|snapshot-paths| Directoies tới nơi mà snapshot được lưu trữ|
|docs-paths| Directoies tới nơi mà docs block được lưu trữ|
|vars| Các biến project được sử dụng để compile|

*dbt_project.yml*

```
# Name your project! Project names should contain only lowercase characters
# and underscores. A good package name should reflect your organization's
# name or the intended use of these models
name: 'MOHA'
version: '1.0.0'
config-version: 2

# This setting configures which "profile" dbt uses for this project.
profile: 'olap'

# These configurations specify where dbt should look for different types of files.
# The `model-paths` config, for example, states that models in this project can be
# found in the "models/" directory. You probably won't need to change these!
model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

target-path: "target"  # directory which will store compiled SQL files
clean-targets:         # directories to be removed by `dbt clean`
  - "target"
  - "dbt_packages"


# Configuring models
# Full documentation: https://docs.getdbt.com/docs/configuring-models

# In this example config, we tell dbt to build all models in the example/ directory
# as tables. These settings can be overridden in the individual model files
# using the `{{ config(...) }}` macro.
models:
  olap:
    # Config indicated by + and applies to all files under models/example/
    +materialized: ephemeral
```
## Các khái niệm cơ bản
### **Sources**
Được định nghĩa trong *.yml* file (directory *models*). Sources giúp đặt tên và mô tả dữ liệu được extract và load vào warehouse. Bằng cách declare các tables là source trong dbt, có thể:

- Seclect from source tables trong models (sử dụng: {{source()}} function), giúp xác định lineage của data
- Test các giả định về source data
- Tính các freshness của source data

1. Khai báo một source

Được liệt kê dưới *source* key:\
*models/schema.yml*
```
version: 2

sources:

  - name: to_chuc_hanh_chinh
    database: olap_test
    tables:
      - name: f_so_ubnd_co_ld_chu_chot_nu
      - name: d_nhiem_ky

  - name: common
    database: olap_test
    tables:
      - name: d_cap_don_vi_hanh_chinh
      - name: d_tong_so
      - name: d_don_vi_hanh_chinh
      - name: d_thong_tin_bieu
      - name: d_loai_don_vi

  - name: linh_vuc_01
    database: serving_1_test
    tables:
      - name: so_ubnd 
```
2. Select from source\
Khi một source đã được define, nó có thể được referenced từ một model - sử dụng {{source()}} function
*models/ubnd.sql*
```
-- Group code: A026: Số UBND cấp tỉnh
select
    NEWID() id,
    N'Số UBND' thong_tin,
    nk.name ky_du_lieu,
    dvhc.code ma_dv_hc,
    dvhc.name ten_dv_hc,
    '1' phan_cap,
    null parent_id,
    'cap_tinh' param_key,
    fact.so_ubnd_co_ld_chu_chot_nu param_value,
    'A026' group_code,
    GETDATE() created_at,
    GETDATE() updated_at
from {{ source('to_chuc_hanh_chinh', 'f_so_ubnd_co_ld_chu_chot_nu') }} fact
left join {{ source('common', 'd_don_vi_hanh_chinh') }} dvhc on fact.don_vi_hanh_chinh_id = dvhc.id
left join {{ source('to_chuc_hanh_chinh', 'd_nhiem_ky') }} nk on fact.nhiem_ky_id = nk.id
where fact.cap_don_vi_hanh_chinh_id = 2 and tong_so_id is null
```

3. Source properties

Khai báo trong file *.yml*, *models* directory.
~~~
version: 2

sources:
  - name: <string> # required
    description: <markdown_string>
    database: <database_name>
    schema: <schema_name>
    loader: <string>
    loaded_at_field: <column_name>
    meta: {<dictionary>}
    tags: [<string>]
    
# requires v1.1+
    config:
      <source_config>: <config_value>

    overrides: <string>

    freshness:
      warn_after:
        count: <positive_integer>
        period: minute | hour | day
      error_after:
        count: <positive_integer>
        period: minute | hour | day
      filter: <where-condition>

    quoting:
      database: true | false
      schema: true | false
      identifier: true | false

    tables:
      - name: <string> #required
        description: <markdown_string>
        meta: {<dictionary>}
        identifier: <table_name>
        loaded_at_field: <column_name>
        tests:
          - <test>
          - ... # declare additional tests
        tags: [<string>]
        freshness:
          warn_after:
            count: <positive_integer>
            period: minute | hour | day
          error_after:
            count: <positive_integer>
            period: minute | hour | day
          filter: <where-condition>

        quoting:
          database: true | false
          schema: true | false
          identifier: true | false
        external: {<dictionary>}
        columns:
          - name: <column_name> # required
            description: <markdown_string>
            meta: {<dictionary>}
            quote: true | false
            tests:
              - <test>
              - ... # declare additional tests
            tags: [<string>]
          - name: ... # declare properties of additional columns

      - name: ... # declare properties of additional source tables

  - name: ... # declare properties of additional sources
~~~
4. Source configurations 

Source được cấu hình thông qua *config* block trong *.yml* file (*model* directory), hoặc từ *dbt_project.yml* file, bên dưới *source* key (cách này thường dùng để cấu hình các source được import từ một package, có thể disable source nếu muốn).

*dbt_project.yml*
```
sources:
  <resource-path>:
    +enabled: true | false
```
### **Models (SQL model)**
SQL model là các câu lệnh select được lưu dưới dạng file sql (trong *model* directory). Ngoài ra còn Python model nhưng thường dùng cho việc training hoặc deploy data science models.
- Mỗi *.sql file* chứa một model/câu lệnh select
- Tên model là tên sql file

Khi excute ``` dbt run``` trong terminal, dbt sẽ build model này bằng cách *create view* hoặc *create table* (Tuỳ vào cấu hình *materialized* của model trong dbt_project.yml*).

Mặc định, dbt tạo model là view, build model trong target schema được define, sử dụng file name là tên của view hoặc table trong database.

1. Cấu hình models

Có thể thiết lập trong *dbt_project.yml* hoặc sử dụng *config* block. Các cấu hình bao gồm:
- Thay đổi materialization được sử dụng để tạo model trong warehouse
- Build model thành các schema riêng biệt
- Apply tags cho model

*dbt_project.yml*
```
...
models:
  olap:
    # Config indicated by + and applies to all files under models/example/
    +materialized: ephemeral
```
2. Building dependencies giữa các models

Sử dụng *ref* function. Sử dụng *ref* function để
- Run model -> tạo ra dependent acyclic graph (DAG)
- Quản lý các môi trường riêng biệt - dbt sẽ thay thế các model trong ref function với database name -> Viết transform thành các module, có thể tái sử dụng model, giảm lặp code.
### **Materializations**
Materialization: cách mà dbt build model trong warehouse. Các loại materialization:
- table
- view
- incremental
- ephemeral
Cấu hình material: trong *dbt_project.yml* hoặc trong *config* block tại .sql file (*model* directory)
```

{{ config(materialized='table', sort='timestamp', dist='user_id') }}

select *
from ...
```
***View***

Model được dbt build thành view trong warehouse, bằng câu lệnh *create view*
- Ưu điểm: alwways have the latest record
- Nhược điểm: slow to query

***Table***

Model được dbt build thành table trong warehouse, bằng câu lệnh *create table*
- Ưu điểm: alwways havw the latest record
- Nhược điểm: slow to query

## DBT deployment

