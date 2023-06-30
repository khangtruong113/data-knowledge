# DBT
DBT (Data Build Tool) là công cụ hỗ trợ việc transform, document, test trở nên dễ dàng hơn. Nó giúp một DA có thể thực hiện một phần công việc của DE, phát triển các model phức tạp và sát với nhu cầu business mà không cần phải sử dụng nguồn lực (thường là luôn bị quá tải) của các DE.

Có 2 phiên bản: 
- dbt Cloud (tính phí)
- dbt CLI/dbt Core (sử dụng trong phần tìm hiểu dbt này)

[Cài đặt dbt Core](https://docs.getdbt.com/docs/core/installation): install packages: dbt-core, dbt-sqlserver

[Quickstart for dbt Core](https://docs.getdbt.com/quickstarts/manual-install?step=1)

[Một số câu lệnh cơ bản](https://docs.getdbt.com/reference/commands/build):

| Commands                                                             | Description                                                                                                               |
|:---------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| ```dbt debug```                                                      | Check set up                                                                                                              |
| ```dbt run```                                                        | Run all models                                                                                                            |
| ```dbt run --select <model_name>``` OR ```dbt run -s <model_name>``` | Run only model selected (```dbt run -s dim_customers+``` sẽ chỉ áp dụng cho dim_customers và các models downstream của nó |
| ```dbt docs generate```                                              | Create catalog                                                                                                            |
| ```dbt docs serve```                                                 | Go to dbt docs web                                                                                                        |
| ```dbt build```                                                      | Builds and tests your selected resources such as models, seeds, snapshots, and tests                                      |
| ```dbt test```                                                       | Executes the tests you defined for your project                                                                           |

## 1. DBT Project Structure
Một project gồm các resources sau:

| Resource  | Description                                                                                                                                                    |
|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| models    | Mỗi model nằm trong 1 file riêng và chứa logic transform raw data thành dataset để phân tích hoặc có thể là các bước trung gian trong quá trình transformation |
| snapshots | Cách capture lại trạng tahsi của các bảng có thay đổi để sau này có thể tham khảo                                                                              |	
| seeds     | CSV files với static data mà có thể load vào data platform với dbt                                                                                             |
| tests     | SQL queries viết để test models và resources trong project                                                                                                     |
| macros    | Blocks of code mà có thể tái sử dụng nhiều lần                                                                                                                 |
| docs      | Docs cho dự án mà bạn có thể tự build                                                                                                                          |
| sources   | Cách đặt tên và mô tả data được load vào warehouse bởi Extract and Load tools                                                                                  |
| exposures | Cách định nghĩa và mô tả downstream use của project                                                                                                            |
| metrics   | Cách định nghĩa metríc cho project                                                                                                                             |
| analysis  | Cách tổ chức các truy vấn SQL phân tích trong project                                                                                                          |

The basic building blocks of every dbt project are:
- The model (sql file)
- The model metadata (yml file)
- The model documentation data (md file)

Three primary layers in the ```models``` directory, which build on each other:
- Staging — creating our atoms, our initial modular building blocks, from source data 
- Intermediate — stacking layers of logic with clear and specific purposes to prepare our staging models to join into the entities we want 
- Marts — bringing together our modular pieces into a wide, rich vision of the entities our organization cares about

Tham khảo: [getdbt1](https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview), [getdbt2](https://docs.getdbt.com/docs/build/projects),
[medium](https://medium0.com/everything-full-stack/dbt-project-structure-bc796694c661)

## 2. Creating a DBT Project
- Khởi tạo một dbt project bằng lệnh: ```dbt init```
- Nhập tên project: dbt_tutorial
- Chọn database sẽ sử dụng: sqlserver

### dbt_project.yml
Tối thiểu mọi project đều phải có configuration file ```dbt_project.yml```. Chỉnh sửa file ```dbt_project.yml``` để set up configuration:

| YAML key            | Mô tả                                                                                                                                              |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| name                | Tên project                                                                                                                                        |
| version             | Version của project                                                                                                                                |
| require-dbt-version | Đảm bảo project sẽ chỉ hoạt động trong một dải dbt Core versions                                                                                   |
| profile             | Profile mà dbt sử dụng để connect tới data platform (database), profile chứa các cấu hình của data platform (host, port, user name, password, ...) |
| model-paths         | Directories tới nơi mà model và source được lưu trữ                                                                                                |
| seed-paths          | Directories tới nơi mà seed files được lưu trữ                                                                                                     |
| test-paths          | Directories tới nơi mà test files được lưu trữ                                                                                                     |
| analysis-paths      | Directories tới nơi mà analysis files được lưu trữ                                                                                                 |
| macro-paths         | Directories tới nơi mà macro được lưu trữ                                                                                                          |
| snapshot-paths      | Directories tới nơi mà snapshot được lưu trữ                                                                                                       |
| docs-paths          | Directories tới nơi mà docs block được lưu trữ                                                                                                     |
| vars                | Các biến project được sử dụng để compile                                                                                                           |

```
name: string

config-version: 2
version: version

profile: profilename

model-paths: [directorypath]
seed-paths: [directorypath]
test-paths: [directorypath]
analysis-paths: [directorypath]
macro-paths: [directorypath]
snapshot-paths: [directorypath]
docs-paths: [directorypath]
asset-paths: [directorypath]

target-path: directorypath
log-path: directorypath
packages-install-path: directorypath

clean-targets: [directorypath]

query-comment: string

require-dbt-version: version-range | [version-range]

quoting:
  database: true | false
  schema: true | false
  identifier: true | false

models:
  <model-configs>

seeds:
  <seed-configs>

snapshots:
  <snapshot-configs>

sources:
  <source-configs>
  
tests:
  <test-configs>

vars:
  <variables>

on-run-start: sql-statement | [sql-statement]
on-run-end: sql-statement | [sql-statement]

dispatch:
  - macro_namespace: packagename
    search_order: [packagename]
```

### profiles.yml
Khi chạy dbt từ CLI (command line), nó sẽ đọc ```profiles.yml``` để tìm ```profile``` name và sẽ nhìn vào profile có cùng tên đó ở trong ```profiles.yml```. Profile này chứa tất cả thông tin mà dbt cần để kết nối với data platform.

```
config:
  send_anonymous_usage_stats: <true | false>
  use_colors: <true | false>
  partial_parse: <true | false>
  printer_width: <integer>
  write_json: <true | false>
  warn_error: <true | false>
  warn_error_options: <include: all | include: [<error-name>] | include: all, exclude: [<error-name>]>
  log_format: <text | json | default>
  debug: <true | false>
  version_check: <true | false>
  fail_fast: <true | false>
  use_experimental_parser: <true | false>
  static_parser: <true | false>

<profile-name>:
  target: <target-name> # this is the default target
  outputs:
    <target-name>:
      type: <bigquery | postgres | redshift | snowflake | other>
      schema: <schema_identifier>
      threads: <natural_number>

      ### database-specific connection details
      ...

    <target-name>: # additional targets
      ...

<profile-name>: # additional profiles
  ...
```

## 3. Models
**Models in dbt**
- Models are SQL select statements 
- Models live in 'models' folder 
- Each model has 1-to-1 relationship with a table or view in the DWH

**Modularity**
- Building a final product piece by piece rather than all at once 
- Each model is reusable for other downstream models

**Model Name Conventions**
- Source: the raw data that has already been loaded
- Staging: clean and standardlize the data, one to one with sources tables
- Intermediate: models between staging and final models, always built on staging models, can hide it
- Facts: things that are occurring or have occurred (events, clicks, votes - keep happening over time)
- Dimensions: people, place, or thing, users, companies, product, customers

**Materialization**: [xem thêm tại đây](https://docs.getdbt.com/guides/best-practices/materializations/1-guide-overview) 
- views
- tables
- incremental model

Có thể configure materialization ở đầu mỗi models (file .sql):

```
{{ config(materialized='view')}}
---------------------------------
{{ config(materialized='table')}}
```
Hoặc configure cho cả thư mục ở model luôn tại file ```dbt_project.yml```:
```
models:
  dbt_tutorial:
    marts:
      core:
        +materialized: table
    staging:
      +materialized: view
```
Nếu ở ```dbt_project.yml``` set là view nhưng vào ```models``` set là table thì lúc chạy sẽ generate ra table.

**Build dependecies between models**

Sử dụng 'ref' function trong câu lệnh ở model

**Tạo file ```.yml``` để lam docs cho models**

_Xem thêm ví dụ về phần Models này ở directory ```models```_

## 4. Sources

- Configure source chỉ cần update ở 1 nơi (.yml file): database, schema
- Source funtion example: {{source('stripe','payments')}} compiles to raw.stripe.payments
- Visualize raw tables trong lineage

## 5. Tests

## 6. Documentation

## 7. Seeds, Snapshots, Exposures

## 8. Jinja & Macros

## 9. Packages

## 10. Analyses

## 11. Metrics
