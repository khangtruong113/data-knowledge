import pandas as pd
import io
from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
'''
This function is wrote to creat SQL file
Input:
    1. The location of the file (file_location), must be string (For example: 'F:\Synodus\DA.BNV\Dim_Fact_Listing_09072022.xlsx')
        The excel file has 2 sheets
        The first sheet gives information about the list of tables (column C) and their schemas (column B), is named 'Danh sách bảng dim'
        Anorther sheet gives information about the structure of single table, is named 'Cấu trúc bảng dim'
        The order of table in the first sheet may be not the same in the second
    2. The name of SQL file, must be tring, not must be contain '.sql' (For example: 'CreateTable', not 'CreateTable.sql')
    3. The name of database (DB_name), must be string
Out put:
    CreateTable.sql file which creats tables are given in the .xlsx file
    The .sql file is created in the current folder
    The table has only primary key (not foreign key), the fileds that is the primary key must be filled 'P' in the 'P/K key?' colummn in 'Cấu trúc bảng dim' sheet
    Structure of SQL file:
        --Create databse
            CREATE DATABASE DB_name;
            GO
            USE DB_name;
            GO
        --Create schemas:
            IF SCHEMA_ID('shema_name') IS NULL
              EXECUTE ('CREATE SCHEMA schema_name');
            GO
        -Create table:
            #Pre_table
            IF OBJECT_ID('schema_name.table_name') IS NULL
            CREATE TABLE schema_name.table_name

            #Inner_table
            (
                column1 datatype (NOT NULL PRIMARY KEY),
                column... datatype (NOT NULL PRIMARY KEY),
             )
            GO
Notes:
    Trim whole .xlsx file before running this function
    Just only tables that has apperanced in both 2 sheets with the same name has been created
'''

@task(name = "Extract data from excel file", retries = 3, retry_delay_seconds = 60)
def extract(file_location):
    '''
    got data from the excel file that has already read
        input: file_location - contain the location of the file that you want to extract
        out put:
            1. dim_list: contains the list of schema and correspond table name
            (is extracted from 'Danh sách bảng dim' sheet)
            2. schema: a list of schemas (is extracted from 'Danh sách bảng dim' sheet),
            only contains the diferrent values, it's used to create the schemas needed
            3. table_struc: the name of tables and their structure (is extracted from 'Danh sách bảng dim' sheet, has repeating structure:
                |Bảng Table_name|----------------------|
                |Tên trường|Kiểu dữ liệu|Rỗng?|P/K Key?|
                |----------|------------|-----|--------|
    '''
    dim_list = pd.read_excel(file_location, sheet_name = 'Danh sách bảng dim', usecols = "B:C")
    dim_list = dim_list.values

    schema_list = pd.read_excel(file_location, sheet_name = 'Danh sách bảng dim', usecols = "B")
    schema_list = schema_list.values
    schema = []
    [schema.append(x) for x in schema_list if x not in schema]

    table_struc = pd.read_excel(file_location, header = None, index_col = False, sheet_name = 'Cấu trúc bảng dim', usecols = "A:D")
    table_struc = table_struc.values

    return dim_list, schema, table_struc

@task(name = "Create databse")
def gen_database(database_name):
    '''
    this function to create a database with the defined name (database_name)
        input: database_name - the name of the database
        output: SQL script to creat database
    '''
    database = "CREATE DATABASE %s; \nGO \nUSE %s; \nGO" % (database_name, database_name)
    return database

@task(name = "Create schema")
def gen_schema(schema):
    '''
        this function to generate all schemas that needed
        input: schema - the list of needed schema to create
        output: SQL script to creat schemas
    '''
    sche = ''
    for x in schema:
        x = x[0]
        single_sche = "IF SCHEMA_ID('%s') IS NULL\n  EXECUTE ('CREATE SCHEMA %s');\nGO\n" % (x, x)
        sche = ''.join([sche, single_sche, '\n'])
    return sche

@task(name = "Create the opening the of tables")
def gen_the_first_of_the_table(dim_list):
    '''
    this function to generate the opening of the creating tables script
    - input: dim_list to return the list of strings ('schema_name.table_name')
    - output:
        IF OBJECT_ID('schema_name.table_name') IS NULL
        CREATE TABLE schema_name.table_name
        (
    '''
    schema_table = []
    # schema_table is the list of strings ('schema_name.table_name')
    for i in dim_list:
        table_name = '%s.%s' % (i[0], i[1])  # i[0] returns the schema and i[1] returns the correspond table name
        table_name = table_name.replace('\xa0', '')
        schema_table.append(table_name)
    # pre_table is the list of strings
    # IF OBJECT_ID('schema_name.table_name') IS NULL
    # CREATE TABLE schema_name.table_name
    # (
    pre_table = []
    for i in schema_table:
        pre_code = "IF OBJECT_ID('%s" % (i) + "') IS NULL" + "\n" \
                   + "CREATE TABLE %s" % (i) + '\n' + '('
        pre_table.append(pre_code)
    return pre_table

@task(name = "Create the body of the tables")
def gen_inner_table(table_struc):
    '''
    this function to generate the body of the script to create table
    - input: table_struc (is extracted from "Cau truc bang dim" sheet to generate the declaring field script
    - output: table = [table_name, inner_table]
        - table_name is the name of table list (is extracted from 'Cấu trúc bảng dim' sheet)
        - inner_table is the list of strings that contains the body of scripts to create table
        form:
        column1 datatype (NOT NULL PRIMARY KEY),
        column... datatype (NOT NULL PRIMARY KEY),
         )
        GO
    '''
    # declare_field is the list of string that has created by combining A, B, C, D column in 'Cấu trúc bảng dim' sheet
    declare_field = []
    for i in table_struc:
        # declare_a is a string has structure (name_field data_type) (For example: 'user_id int')
        declare_single_field = "%s %s" % ((i)[0], (i)[1])
        # if 'Rỗng?' column is blank, 'NOT NULL' is set for this field
        if pd.isna((i)[2]):
            declare_single_field = declare_single_field + " NOT NULL"
        # if 'P/F Key?' column is 'P', 'PRIMARY KEY' is set for this field
        i[3] = str(i[3]).replace('\xa0', '')
        if i[3] == 'P':
            declare_single_field = declare_single_field + " PRIMARY KEY"
        # remove blanks in cells and add ', \n'
        declare_single_field = str(declare_single_field).replace(u'\xa0', u' ')
        declare_single_field = declare_single_field + ',' + '\n'
        declare_field.append(declare_single_field)

    inner_table = []
    inner = ''
    table_name = []
    # if declare_filed[i] contains 'Bảng ' (that is the row given the name of the table),
    # the flag is on and inner string contains all the previous declares row until the flag is off
    for i in declare_field:
        if "Bảng" in i:
            inner = inner + ')' \
                    + '\n' + 'GO'
            table_name.append(i)
            inner_table.append(inner)
            inner = ''
            continue
        # if declare_filed[i] contains 'Tên ' (that is [Tên trường Kiểu dữ liệu] row, the row is dropt, inner will not take this row
        else:
            if "Tên" in i:
                continue
            # if declare_filed[i] doesn't contains 'Tên ' and 'Bảng ' (implicates that i is rows to declares avairables), inner will take this row
            else:
                inner = inner + str(i)
    # apply to the first table, that hasn't been inner yet
    inner = inner + ')' + '\n' + 'GO'
    inner_table.append(inner)
    del inner_table[0]
    # # print(inner_table)
    # print(table_name)
    return table_name, inner_table

@task(name = "Create the completed tables")
def gen_table(dim_list, pre_table, table_name, inner_table):
    # this function to generate all tables that needed
    '''
    returns create_table is the list of string that has structure:
        IF OBJECT_ID('schema_name.table_name') IS NULL
        CREATE TABLE schema_name.table_name
        (
        column1 datatype (NOT NULL PRIMARY KEY),
        column... datatype (NOT NULL PRIMARY KEY),
        )
        GO
    '''
    create_table = ''
    # table_list is the name_table list has extracted from 'Danh sách bảng dim' sheet
    table_list = []
    for i in dim_list:
        i = str(i[1]).replace('\xa0', '')
        table_list.append(i)

    # if name of table in 'Danh sách bảng dim' and 'Cấu trúc bảng dim' are the same, the table will be created
    created_table_num = 0
    for i in range(len(table_list)):
        for j in range(len(table_name)):
            table = ''
            table_name[j] = table_name[j].replace('Bảng ', '')
            table_name[j] = table_name[j].replace('NOT NULL', '')
            table_name[j] = table_name[j].replace('\n', '')
            table_name[j] = table_name[j].replace('nan', '')
            table_name[j] = table_name[j].replace(',', '')
            table_name[j] = table_name[j].replace(' ', '')
            if table_list[i] == table_name[j]:
                table = table + str(pre_table[i]) + '\n' + str(inner_table[j])
                create_table = create_table + str(table) + '\n' + '\n'
                created_table_num = created_table_num + 1
    return create_table, created_table_num

@task(name = "Transform data from excel file to T-SQL")
def transform(database, sche, create_table):
    '''
    input:
    - database_name: the name of the database
    - dim_list: the list of dim tables
    - schema: the list of different schema name
    - table_struc: display the structure of single table (columns, type data, atributes)
    output:
    - script - SQL file will create database, schemas and tables
    - number_created_table: the number of the table have been created
    '''
    script = str(database) \
             + '\n' + str(sche) \
             + '\n' + str(create_table)
    return script

@task(name = "Load data into sql file")
def load(script, SQL_file_name):
    '''
    this funtion to create a SQL file with its content is scripts
    input:
    - script: the string contain context of SQL file
    - SQL_file_name - the name of the sql file
    output: sql file in the current folder
    '''
    file_name = SQL_file_name+'.sql'
    with io.open(file_name, "w", encoding = "utf-8") as f:
        f.write(script)

@flow(name = "Modeling",
    description = "My flow using SequentialTaskRunner",
    task_runner = SequentialTaskRunner())
def gen_code_flow(file_location, database_name, SQL_file_name):
    dim_list, schema, table_struc = extract(file_location)
    database = gen_database(database_name)
    sche = gen_schema(schema)
    pre_table = gen_the_first_of_the_table(dim_list)
    table_name, inner_table = gen_inner_table(table_struc)
    create_table, created_table_num = gen_table(dim_list, pre_table, table_name, inner_table)
    script = transform(database, sche, create_table)
    load(script, SQL_file_name)
    # print the number of created tables
    print('%s.sql file has appeared in the current folder' %SQL_file_name + '\n'
          + 'The number of tables created is %s' %(str(created_table_num)))

gen_code_flow (file_location = 'F:\Synodus\DA.BNV\Dim_Fact_Listing_12_09.xlsx',
               database_name = 'BNV',
               SQL_file_name = 'create_table_prefect')













