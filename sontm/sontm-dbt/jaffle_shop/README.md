# DBT

**dbt (data build tool)** makes data engineering activities accessible to people with data analyst skills to transform the data in the warehouse using simple select statements, effectively creating your entire transformation process with code.
You can write custom business logic using SQL, automate data quality testing, deploy the code, and deliver trusted data with data documentation side-by-side with the code.

**dbt Cloud vs dbt Core**:
- `dbt Core` is a free, open-source, command-line tool that enables users to design their data models using SQL. It then converts these models into optimized SQL code that can be executed on data warehouses or other data storage systems.
- In contrast, `dbt Cloud` is a cloud-based solution that offers additional features and capabilities in addition to those offered by dbt Core. It provides a web interface for managing data models and also includes scheduling options, collaboration tools, and integrations with other data tools.
 
## 0. Installation
[**Install dbt Core**](https://docs.getdbt.com/docs/core/installation): `dbt-core`, `dbt-<adapter>`

## 1. dbt Command reference

|  Command | Description  |
|---|---|
| `dbt init`  |  Initializes a new dbt project |
| `dbt debug`    |  Debugs dbt connections and projects  |
|   `dbt run`  |  Runs the models in a project  |
|  `dbt run --select <model_name>` <br> `dbt run -s <model_name>`  |  Run only model selected   |
|  `dbt build`  |  Build and test all selected resources (models, seeds, snapshots, tests)  |
|  `dbt test`  | executes tests defined in a project   |
|  `dbt docs generate`  |  Create catalog  |
|  `dbt docs serve` |  dbt docs serve  |
|  `dbt seed` |   loads CSV files into the database  |
|  `dbt compile` |  compiles (but does not run) the models in a project  |
|  `dbt deps` | downloads dependencies for a project   |

## 2. Creating a dbt Project

In the folder you will see the following folders.

```
.
├── analysis
├── dbt_packages
├── logs
├── macros
├── models
│   ├── marts
│   │   ├── core
│   │   └── 
│   └── staging
├── snapshots
├── tests
├── target
├── .gitignore
├── dbt_projects.yml
├── profiles.yml
└── README.md
```

|  Folder/File | Description  |
|---|---|
| `models`  | Each model lives in a single file and contains logic that either transforms raw data into a dataset that is ready for analytics or, more often, is an intermediate step in such a transformation.  |
| `snapshots`  | 	A way to capture the state of your mutable tables so you can refer to it later.  |
| `seeds`  | CSV files with static data that you can load into your data platform with dbt.  |
| `tests`  |  SQL queries that you can write to test the models and resources in your project. |
| `macros`  |  Blocks of code that you can reuse multiple times. |
|  `analysis` |  A way to organize analytical SQL queries in your project such as the general ledger from your QuickBooks. |
|  `dbt_project.yml`   |  Contains important information that tells dbt how to operate on your project.    |
| `profiles.yml `   |  Contains the connection details for your data platform    |

**dbt_project.yml**: Every dbt project needs a `dbt_project.yml` file — this is how dbt knows a directory is a dbt project. It also contains important information that tells dbt how to operate on your project.

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

**profiles.yml**: When you invoke dbt from the command line, dbt parses your `dbt_project.yml` and obtains the profile name, which dbt needs to connect to your data warehouse.

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
A SQL model is a `select` statement. Models are defined in .sql files (typically in your models directory):

- Each `.sql` file contains one model / `select` statement
- The model name is inherited from the filename.
- Models can be nested in subdirectories within the `models` directory

When you execute the `dbt run` command, `db`t will build this model data warehouse by wrapping it in a `create view as` or `create table as` statement.

**Configuration:**
Configurations are "model settings" that can be set in your `dbt_project.yml` file, and in your model file using a config block. Some example configurations include:

- Changing the materialization that a model uses — a materialization determines the SQL that dbt uses to create the model in your warehouse.
- Build models into separate schemas.
- Apply tags to a model.

Model configuration:
```
name: jaffle_shop
config-version: 2
...

models:
  jaffle_shop: # this matches the `name:`` config
    +materialized: view # this applies to all models in the current project
    marts:
      +materialized: table # this applies to all models in the `marts/` directory
      marketing:
        +schema: marketing # this applies to all models in the `marts/marketing/`` directory

```

The materialization can be configured as a table with the following configuration block at the top of the model file:

```
{{ config(
materialized='table'/'view'
) }}
```

**Building dependencies between models**

You can build dependencies between models by using the `ref` function in place of table names in a query. Use the name of another model as the argument for `ref`.

```
with customers as (

    select * from {{ ref('stg_customers') }}

),

orders as (

    select * from {{ ref('stg_orders') }}

),

...

```

`dbt` uses the ref function to:
- Determine the order to run the models by creating a `dependent acyclic graph (DAG)`.

![DAG](https://docs.getdbt.com/img/dbt-dag.png)
- Manage separate environments — dbt will replace the model specified in the `ref` function with the database name for the table (or view)


## 4. Sources

Sources make it possible to name and describe the data loaded into your warehouse by your Extract and Load tools. By declaring these tables as sources in dbt, you can then

- Select from source tables in your models using the `{{ source() }}` function, helping define the lineage of your data
- Test your assumptions about your source data
- Calculate the freshness of your source data

**Configuration:**
Sources are defined in .yml files nested under a sources: key. (***By default, schema will be the same as name***)
```
version: 2

sources:
  - name: jaffle_shop
    database: raw  
    schema: jaffle_shop  
    tables:
      - name: orders
      - name: customers

  - name: stripe
    tables:
      - name: payments
```

**Selecting from a source**
Once a source has been defined, it can be referenced from a model using the` {{ source()}}` function.

`select * from {{ source(source_name, table_name) }}`


Using the `{{ source () }} `function also creates a dependency between the model and the source table.

## 5. Tests
Testing allows us to make sure that the SQL transformations we write produce a model that meets our assertions.
In `dbt`, tests are written as select statements. These select statements are run against your materialized models to ensure they meet your assertions.

There are **two types of tests** - `generic tests` and `singular tests`:
- `Generic tests` are written in YAML and return the number of records that do not meet your assertions. These are run on specific columns in a model.
- `Singular tests` are specific queries that you run against your models. These are run on the entire model.

**Generic tests**: 
A `generic test` are configured in a YAML file and defined in a test block, which contains a parametrized query and accepts arguments.
Example:
```
version: 2

models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: status
        tests:
          - accepted_values:
              values: ['placed', 'shipped', 'completed', 'returned']
      - name: customer_id
        tests:
          - relationships:
              to: ref('customers')
              field: id
```

`dbt` ships with four built in tests: `unique`, `not null`, `accepted values`, `relationships`:
- `Unique` tests to see if every value in a column is unique
- `Not_null` tests to see if every value in a column is not null
- `Accepted_values` tests to make sure every value in a column is equal to a value in a provided list
- `Relationships` tests to ensure that every value in a column exists in a column in another model


**Singular tests**: write the exact SQL that will return failing records and  
these tests are defined in `.sql` files, typically in your `tests` directory (as defined by your `test-paths` config). These `tests` are defined in `.sql` files, typically in your tests directory (as defined by your test-paths config):
```
-- Refunds have a negative amount, so the total amount should always be >= 0.
-- Therefore return records where this isn't true to make the test fail
select
    order_id,
    sum(amount) as total_amount
from {{ ref('fct_payments' )}}
group by 1
having not(total_amount >= 0)
```

**Tests** can be run against your current project using a range of commands:
- `dbt test` runs all tests in the dbt project
- `dbt test --select test_type:generic`
- `dbt test --select test_type:singular`
- `dbt test --select one_specific_model`

**Storing test failures**

Normally, a test query will calculate failures as part of its execution. 
If you set the optional `--store-failures` flag or `store_failures config`, `dbt` will first save the results of a test query to a table in the database, and then query that table to calculate the number of failures.

`dbt test --store-failures`

## 6. Documentation

`dbt` provides a way to generate documentation for your dbt project and render it as a website. The documentation for your project includes:

- `Information about your project`: including model code, a DAG of your project, any tests you've added to a column, and more.
- `Information about your data warehouse`: including column data types, and table sizes. This information is generated by running queries against the information schema.

Importantly, dbt also provides a way to add `descriptions` to models, columns, sources, and more, to further enhance your documentation.

**Adding descriptions**:
To add descriptions to your project, use the description: key in the same files where you declare `tests` and `sources`, like so:

```
version: 2

models:
  - name: events
    description: This table contains clickstream events from the marketing website

    columns:
      - name: event_id
        description: This is a unique identifier for the event
        tests:
          - unique
          - not_null

      - name: user-id
        quote: true
        description: The user who performed the event
        tests:
          - not_null

```

**Generating project documentation**

`dbt docs generate`: compile relevant information about your dbt project and warehouse into manifest.json and catalog.json files respectively.
`dbt docs serve`: use these .json files to populate a local website.
 ## 7. Jinja
 `Jinja` a templating language written in the python programming language. `Jinja` is used in `dbt` to write functional SQL. For example, we can write a dynamic pivot model using `Jinja`.

 **Jinja Basics**

There are three Jinja delimiters to be aware of in Jinja.

- `{% … %}` is used for statements. These perform any function programming such as setting a variable or starting a for loop.
- `{{ … }}` is used for expressions. These will print text to the rendered file. In most cases in dbt, this will compile your Jinja to pure SQL.
- `{# … #}` is used for comments. This allows us to document our code inline. This will not be rendered in the pure SQL that you create when you run dbt compile or dbt run.

When used in a `dbt` model, your Jinja needs to compile to a valid query. 
-> To check what SQL your Jinja compiles to: Run `dbt compile` from the command line. Then open the compiled SQL file in the `target/compiled/{project name}/` directory. Use a split screen in your code editor to keep both files open at once.

`Dictionaries` are data structures composed of key-value pairs.

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

`Lists` are data structures that are ordered and indexed by integers.

```
{% set self = [‘me’, ‘myself’] %}

{{ self[0] }}

me
```

`If/else statements` are control statements that make it possible to provide instructions for a computer to make decisions based on clear criteria.
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

`For loops` make it possible to repeat a code block while passing different values for each iteration through the loop.
```
{% set flavors = [‘chocolate’, ‘vanilla’, ‘strawberry’] %}

{% for flavor in flavors %}

Today I want {{ flavor }} ice cream!

{% endfor %}

Today I want chocolate ice cream!

Today I want vanilla ice cream!

Today I want strawberry ice cream!
```

## 8. Macros
`Macros` in Jinja are pieces of code that can be reused multiple times – they are analogous to "functions" in other programming languages, and are extremely useful if you find yourself repeating code across multiple models. 
`Macros` are defined in `.sql` files, typically in your `macros` directory (docs).
Example:

```
{% macro cents_to_dollars(column_name, precision=2) %}
    ({{ column_name }} / 100)::numeric(16, {{ precision }})
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
This would be ***compiled*** to:
```
select
  id as payment_id,
  (amount / 100)::numeric(16, 2) as amount_usd,
  ...
from app_data.payments
```

