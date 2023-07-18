# DBT
DBT (Data Build Tool) là công cụ hỗ trợ việc transform, document, test trở nên dễ dàng hơn. Nó giúp một DA có thể thực hiện một phần công việc của DE, phát triển các model phức tạp và sát với nhu cầu business mà không cần phải sử dụng nguồn lực (thường là luôn bị quá tải) của các DE.

Có 2 phiên bản: 
- dbt Cloud (tính phí)
- dbt CLI (sử dụng trong phần tìm hiểu dbt này)

[Cài đặt dbt Core](https://docs.getdbt.com/docs/core/installation): install packages: dbt-core, dbt-sqlserver

[Quickstart for dbt Core](https://docs.getdbt.com/quickstarts/manual-install?step=1)

[Một số câu lệnh cơ bản](https://docs.getdbt.com/reference/commands/build):

| Commands                                                             | Description                                                                                                                                                                                              |
|:---------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```dbt debug```                                                      | Check set up                                                                                                                                                                                             |
| ```dbt run```                                                        | Run all models                                                                                                                                                                                           |
| ```dbt run --select <model_name>``` OR ```dbt run -s <model_name>``` | Run only model selected (```dbt run -s dim_customers+``` sẽ chỉ áp dụng cho dim_customers và các models downstream của nó                                                                                |
| ```dbt test```                                                       | Executes the tests you defined for your project                                                                                                                                                          |
| ```dbt test --select <model_name>```                                 | Test only model selected                                                                                                                                                                                 |
| ```dbt build```                                                      | Builds and tests your selected resources such as models, seeds, snapshots, and tests                                                                                                                     |
| ```dbt build --select <model_name>```                                | ```+<model_name>```: áp dụng cho model_name và các models upstream của nó (từ source đến model đó) <br> ```<model_name>+```: áp dụng cho model_name và các models downstream (từ model đó đến cuối flow) |
| ```dbt docs generate```                                              | Create catalog                                                                                                                                                                                           |
| ```dbt docs serve```                                                 | Go to dbt docs web                                                                                                                                                                                       |
| ```dbt clean```                                                      | Delete all folders specified in the ```clean-targets``` list specified in ```dbt_project.yml```. You can use this to delete the ```dbt_packages``` and ```target``` directories                          |
| ```dbt compile```                                                    | Generate executable SQL from source ```model```, ```test```, and ```analysis``` files. You can find these compiled SQL files in the ```target/``` directory of your dbt project                          |

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

**Tạo file ```.yml``` để làm docs cho models**

_Xem thêm ví dụ về phần Models này ở directory ```models```_

## 4. Sources

- Configure source chỉ cần update ở 1 nơi (.yml file): database, schema
- Source funtion example: {{source('stripe','payments')}} compiles to raw.stripe.payments
- Visualize raw tables trong lineage

## 5. Tests

Có 2 loại tests trong dbt:

- Singular tests: logic riêng cho từng model

  &rarr; Tạo file ```.sql``` trong folder ```tests``` để viết rules


- Generic tests: chung chung và mang tính đại diện hơn, chỉ cần thể hiện qua các dòng YAML code 
  - unique
  - not_null
  - accepted_values
  - relationships

  &rarr; Tạo file ```.yml``` trong folder ```models``` để thêm điều kiện khi khai báo table/view

_Note:_ Thay vì run và test từng model thì có thể sử dụng ```dbt build``` để test xong run lần lượt các model luôn.

## 6. Documentation

- Mục đích: để mọi người trong data team đều xem được data đến từ đâu, query như thế nào
- DAG: auto generate để show flow của data từ source đến final models.
- Có thể add text để mô tả
- Tạo documentation:
  - Thêm dòng ```description``` vào file ```.yml``` khi định nghĩa source, stg,... models
  - Có thể tạo file ```.md``` rồi tạo bảng định nghĩa trong đó rồi thêm vào dòng ```description```: '{{ ("doc_block") }}'

## 7. Analyses
Khái niệm về ```models``` của dbt giúp các nhóm dữ liệu dễ dàng kiểm soát phiên bản và cộng tác trong quá trình chuyển đổi dữ liệu. Tuy nhiên, đôi khi, một câu lệnh sql nhất định không hoàn toàn phù hợp với khuôn mẫu của mô hình dbt. Các tệp sql "phân tích" này có thể được tạo phiên bản bên trong dự án dbt của bạn bằng chức năng ```analysis``` của dbt.

Bất kỳ tệp ```.sql``` nào được tìm thấy trong thư mục ```analyses/``` của dự án dbt sẽ được compile nhưng không được execute. Điều này có nghĩa là các nhà phân tích có thể sử dụng chức năng dbt như ```{{ ref(...) }}``` để chọn từ các models theo cách không phụ thuộc vào môi trường.

Để compile sang một câu sql có thể chạy được, chạy ```dbt compile```. Sau đó tìm file SQL đã được compile trong ```target/compiled/{project name}/analyses/```. Có thể paste vào sql hoặc BI tool để chạy câu sql này, nhớ rằng ở trogn database nó là dạng ```analysis```, không phải ```model```.

- sql files in the ```analyses``` folder with all models, tests, macros,... nhưng không phải models hay tests,...
- support Jinja
- can be compiled with ```dbt compile```
- one off queries
- training queries
- auditing/refactoring

## 8. Seeds
Import data từ file ```.csv``` vào database, file ```.csv``` này được đặt trong ```seeds``` folder, ngoài ra trong folder này cũng có thể tạo file ```.yml``` để khai báo seeds (chạy ```dbt test --models <seed_name>```).

Chạy ```dbt seed ``` để thực thi việc import csv vào database thành một bảng.

Sử dụng ```{{ ref(...) }}``` trong các model để tính toán bình thường.

- csv files in the data folder
- build a table from a small amount of data in a csv file
- build these tables with ```dbt seed```
- seeds are not designed for large or frequently changing data

## 9. Snapshots

- help to "look back in time"
- implement type-2 Slowly Changing Dimensions over mutable source tables: track việc thêm mới hoặc update, không track được khi xóa đi
- có 2 kiểu strategy: ```timestamp``` và ```check``` (kiểu check này cần define cả ```check_cols```)

```
{% snapshot orders_snapshot_timestamp %}

    {{
        config(
          target_schema='snapshots',
          strategy='timestamp',
          unique_key='id',
          updated_at='updated_at',
        )
    }}

    select * from {{ source('jaffle_shop', 'orders') }}

{% endsnapshot %}
```

```
{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='snapshots',
          strategy='check',
          unique_key='id',
          check_cols=['status', 'is_cancelled'],
        )
    }}

    select * from {{ source('jaffle_shop', 'orders') }}

{% endsnapshot %}
```

- snapshot meta-fields:

| Field          | Meaning                                                                            | Usage                                                                           |
|:---------------|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| dbt_valid_from | The timestamp when this snapshot row was first inserted                            | This column can be used to order the different "versions" of a record.          |
| dbt_valid_to   | The timestamp when this row became invalidated.                                    | The most recent snapshot record will have ```dbt_valid_to``` set to ```null```. |
| dbt_scd_id     | A unique key generated for each snapshotted record.                                | This is used internally by dbt                                                  |
| dbt_updated_at | The updated_at timestamp of the source record when this snapshot row was inserted. | This is used internally by dbt                                                  |


## 10. Exposures

- make it possible to define and describe a downstream use of your dbt project, such as in a dashboard, application, or data science pipeline
- run, test, and list resources that feed into your exposure 
- populate a dedicated page in the auto-generated documentation site with context relevant to data consumers

``` 
version: 2

exposures:
  
  - name: weekly_jaffle_report
    type: dashboard
    maturity: high
    url: https://bi.tool/dashboards/1
    description: >
      Did someone say "exponential growth"?

    depends_on:
      - ref('fct_orders')
      - ref('dim_customers')
      - source('gsheets', 'goals')

    owner:
      name: Callum McData
      email: data@jaffleshop.com
```

## 11. Jinja
- Python based templating language
- Brings functional aspects to SQL
- Enables better collaboration
- Write SQL faster with less lines of code

There are three Jinja delimiters to be aware of in Jinja:

- ```{% … %}``` is used for statements. These perform any function programming such as setting a variable or starting a for loop.
- ```{{ … }}``` is used for expressions. These will print text to the rendered file. In most cases in dbt, this will compile your Jinja to pure SQL.
- ```{# … #}``` is used for comments. This allows us to document our code inline. This will not be rendered in the pure SQL that you create when you run dbt compile or dbt run.

A few helpful features of Jinja include dictionaries, lists, if/else statements, for loops, and macros:

- Dictionaries are data structures composed of key-value pairs.
```
{% set person = {
    ‘name’: ‘me’,
    ‘number’: 3
} %}

{{ person.name }}

me

{{ person[‘number’] }}

3
```

- Lists are data structures that are ordered and indexed by integers.
```
{% set self = [‘me’, ‘myself’] %}

{{ self[0] }}

me
```

- If/else statements are control statements that make it possible to provide instructions for a computer to make decisions based on clear criteria.
```
{% set temperature = 80.0 %}

On a day like this, I especially like

{% if temperature > 70.0 %}

a refreshing mango sorbet.

{% else %}

A decadent chocolate ice cream.

{% endif %}

On a day like this, I especially like

a refreshing mango sorbet
```

- For loops make it possible to repeat a code block while passing different values for each iteration through the loop.
```
{% set flavors = [‘chocolate’, ‘vanilla’, ‘strawberry’] %}

{% for flavor in flavors %}

Today I want {{ flavor }} ice cream!

{% endfor %}

Today I want chocolate ice cream!

Today I want vanilla ice cream!

Today I want strawberry ice cream!
```

- Macros are a way of writing functions in Jinja. This allows us to write a set of statements once and then reference those statements throughout your code base.
```
{% macro hoyquiero(flavor, dessert = ‘ice cream’) %}

Today I want {{ flavor }} {{ dessert }}!

{% endmacro %}

{{ hoyquiero(flavor = ‘chocolate’) }}

Today I want chocolate ice cream!

{{ hoyquiero(mango, sorbet) }}

Today I want mango sorbet!
```

_**Note:** Whitespace Control:_ We can control for whitespace by adding a single dash on either side of the Jinja delimiter. This will trim the whitespace between the Jinja delimiter on that side of the expression.

When used in a dbt model, your Jinja needs to compile to a valid query. To check what SQL your Jinja compiles to:

- Using dbt Cloud: Click the compile button to see the compiled SQL in the Compiled SQL pane
- Using the dbt CLI: Run dbt compile from the command line. Then open the compiled SQL file in the ```target/compiled/{project name}/``` directory. Use a split screen in your code editor to keep both files open at once.

## 12. Macros
- Một đoạn code có thể sử dụng lại nhiều lần
- Có thể hiểu tương tự như functions ở các ngôn ngữ lập trình khác
- Defined in `.sql` files and `macros` folder
- Macro files can contain one or more macros

Macro files can contain one or more macros — here's an example:
``` 
{% macro cents_to_dollars(column_name, scale=2) %}
    ({{ column_name }} / 100)::numeric(16, {{ scale }})
{% endmacro %}
```

A model which uses this macro might look like:
```
select
  id as payment_id,
  {{ cents_to_dollars('amount') }} as amount_usd,
  ...
from app_data.payments
```

This would be compiled to:
```
select
  id as payment_id,
  (amount / 100)::numeric(16, 2) as amount_usd,
  ...
from app_data.payments
```

## 13. Packages
- import models and macros that have already been written
- leverage modeling of common sources
- leverage macros across your dbt project
- find packages at hub.getdbt.com

## 14. Metrics
Là 1 package trong dbt, có thể dùng để tính toán các hàm cơ bản theo 1 bảng calendar được set up sẵn

Xem [tại đây](https://docs.getdbt.com/docs/build/metrics)

## 15. Hooks and Operations
Hooks are Pre and Post database commands executed within the flow of data pipelines.

Hooks can be defined in two ways:

- Within the model, seed, snapshot (pre-hook, post-hook)
- Within the dbt_project.yml (on-run-start, on-run-end)