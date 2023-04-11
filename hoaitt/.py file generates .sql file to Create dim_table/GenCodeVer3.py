import pandas as pd
import io

#This function is wrote to creat SQL file
#Input:
    # 1. The location of the file (file_location), must be string (For example: 'F:\Synodus\DA.BNV\Dim_Fact_Listing_09072022.xlsx')
        # The excel file has 2 sheets
        # The first sheet gives information about the list of tables (column C) and their schemas (column B), is named 'Danh sách bảng dim'
        # Anorther sheet gives information about the structure of single table, is named 'Cấu trúc bảng dim'
        # The order of table in the first sheet may be not the same in the second
    # 2. The name of SQL file, must be tring, not must be contain '.sql' (For example: 'CreateTable', not 'CreateTable.sql')
    # 3. The name of database (DB_name), must be string

#Out put:
    #CreateTable.sql file which creats tables are given in the .xlsx file
    #The .sql file is created in the current folder
    #The table has only primary key (not foreign key), the fileds that is the primary key must be filled 'P' in the 'P/K key?' colummn in 'Cấu trúc bảng dim' sheet
    #Structure of SQL file:
        #--Create databse
            # CREATE DATABASE DB_name;
            # GO
            # USE DB_name;
            # GO
        #--Create schemas:
            # IF SCHEMA_ID('shema_name') IS NULL
            #   EXECUTE ('CREATE SCHEMA schema_name');
            # GO
        #-Create table:
            ##Pre_table
            # IF OBJECT_ID('schema_name.table_name') IS NULL
            # CREATE TABLE schema_name.table_name

            ##Inner_table
            # (
                # column1 datatype (NOT NULL PRIMARY KEY),
                # column... datatype (NOT NULL PRIMARY KEY),
            #  )
            #GO

#Notes:
    #Trim all .xlsx file before running this function
    #Just only tables that has apperanced in both 2 sheets with the same name has been created

def gen_script(file_location,SQL_file_name,DB_name):

##Get data from the excel file that has already read

    #dim_list contains the list of schema and correspond table name (is extracted from 'Danh sách bảng dim' sheet)
    #included 2 columns (the one is schema list (contains many dupplicated values, used to 'create Schemma_name.Table_name'), and the other is the correspond tables)
    dim_list = pd.read_excel(file_location, sheet_name='Danh sách bảng dim',usecols="B:C")
    dim_list = dim_list.values

    #return a list of schema (is extracted from 'Danh sách bảng dim' sheet
    schema_list= pd.read_excel(file_location, sheet_name='Danh sách bảng dim',usecols="B")
    schema_list= schema_list.values

    # remove dupplicate values in schema_list (tables can use the same schema)
    # schema only contains the diferrent values, it used to create the schemas needed
    schema = []
    [schema.append(x) for x in schema_list if x not in schema]

    #return the lisSt supplies the name of tables and their structure (is extracted from 'Danh sách bảng dim' sheet
    #table_struc has repeating structure:
        # |Bảng Table_name|----------------------|
        # |Tên trường|Kiểu dữ liệu|Rỗng?|P/K Key?|
        # |----------|------------|-----|--------|
    table_struc = pd.read_excel (file_location, header=None, index_col=False,sheet_name='Cấu trúc bảng dim',usecols="A:D")
    table_struc = table_struc.values

    # this function to create a database with the defined name (database_name)
    def gen_database(database_name):
        gen_database = "CREATE DATABASE %s; \nGO \nUSE %s; \nGO" %(database_name, database_name)
        return gen_database

    # This function to generate all schemas that needed
    def gen_schema():
        sche = ''
        for x in schema:
            x = x[0]
            single_sche = "IF SCHEMA_ID('%s') IS NULL\n  EXECUTE ('CREATE SCHEMA %s');\nGO\n" %(x, x)
            sche = ''.join([sche, single_sche, '\n'])
        return sche

    # This function to generate all tables that needed
    def gen_table():
        # This function to generate the first scripts of creat tables
        #like:
            # IF OBJECT_ID('schema_name.table_name') IS NULL
            # CREATE TABLE schema_name.table_name
            #(
        def gen_the_first_of_the_table():
            schema_table = []
            #schema_table is the list of strings ('schema_name.table_name')
            for i in dim_list:
                table_name = '%s.%s' %(i[0], i[1]) #i[0] returns the schema and i[1] returns the correspond table name
                table_name = table_name.replace('\xa0', '')
                schema_table.append(table_name)
            # pre_name is the list of strings
                # IF OBJECT_ID('schema_name.table_name') IS NULL
                # CREATE TABLE schema_name.table_name
                #(
            pre_table = []
            for i in schema_table:
                pre_code = "IF OBJECT_ID('%s" % (i) + "') IS NULL" + "\n" \
                           + "CREATE TABLE %s" % (i) + '\n' + '('
                pre_table.append(pre_code)
            return pre_table

        # This function to generate the body of the script to create table, return table = [table_name, inner_table]
        # table_name is the name of table list (following 'Cấu trúc bảng dim' sheet
        # inner_table is the list of strings that contains the body of scripts to create table
        #like:
            # column1 datatype (NOT NULL PRIMARY KEY),
            # column... datatype (NOT NULL PRIMARY KEY),
            #  )
            # GO

        def gen_inner_table():
            # script to declare variables
            #declare_field is the list of string that has created by combining A, B, C, D column in 'Cấu trúc bảng dim' sheet
            declare_field = []
            for i in table_struc:
                #declare_a is a string has structure (name_field data_type) (For example: 'user_id int')
                declare_single_field = "%s %s" %((i)[0],(i)[1])
                #if 'Rỗng?' column is blank, 'NOT NULL' is set for this field
                if pd.isna((i)[2]):
                    declare_single_field = declare_single_field + " NOT NULL"
                # if 'P/F Key? ' column is 'P', 'PRIMARY KEY' is set for this field
                i[3]=str(i[3]).replace('\xa0','')
                if i[3]=='P':
                    declare_single_field = declare_single_field + " PRIMARY KEY"
                #remove blanks in cells and add ', \n'
                declare_single_field = str(declare_single_field).replace(u'\xa0', u' ')
                declare_single_field = declare_single_field + ',' + '\n'
                declare_field.append(declare_single_field)

            inner_table = []
            inner = ''
            table_name = []
            #if declare[i] contains 'Bảng ' (that is the row given the name of the table),
            # the flag is on and inner string contains all the previous declares row untill the flag is off

            for i in declare_field:
                if "Bảng" in i:
                    inner = inner + ')' \
                            + '\n' + 'GO'
                    table_name.append(i)
                    inner_table.append(inner)
                    inner = ''
                    continue
                # if declare[i] contains 'Tên ' (that is [Tên trường Kiểu dữ liệu] row, the row is dropt, inner will not take this row
                else:
                    if "Tên" in i:
                        continue
                    # if declare[i] doesn't contains 'Tên ' and 'Bảng ' (implicates that is rows to declares avairables), inner will take this row
                    else:
                        inner = inner + str(i)
            #apply to the first table, that hasn't been inner yet
            inner = inner + ')' + '\n' + 'GO'
            inner_table.append(inner)
            del inner_table[0]
            table = [table_name, inner_table]
            return table

        # returns create_table is the list of string that has structure:
            # IF OBJECT_ID('schema_name.table_name') IS NULL
            # CREATE TABLE schema_name.table_name
            # (
            # column1 datatype (NOT NULL PRIMARY KEY),
            # column... datatype (NOT NULL PRIMARY KEY),
            #  )
            # GO
        create_table = ''

        pre = gen_the_first_of_the_table()
        #table_list is the name_table list has extracted from 'Danh sách bảng dim' sheet
        table_list = []
        for i in dim_list:
            i = str(i[1]).replace('\xa0', '')
            table_list.append(i)

        inner_table = gen_inner_table()
        #inner is the body of script to create table list has extracted from 'Cấu trúc bảng dim' sheet
        inner = inner_table[1]
        #cor_table is the name_table list has extracted from 'Cấu trusc bảng dim' sheet
        cor_table = inner_table[0]
        #if name of table in 'Danh sách bảng dim' and 'Cấu trúc bảng dim' are the same, the table will be created
        created_table_num=0
        for i in range(len(table_list)):
            for j in range(len(cor_table)):
                table = ''
                cor_table[j] = cor_table[j].replace('Bảng ', '')
                cor_table[j] = cor_table[j].replace('NOT NULL', '')
                cor_table[j] = cor_table[j].replace('\n', '')
                cor_table[j] = cor_table[j].replace('nan', '')
                cor_table[j] = cor_table[j].replace(',', '')
                cor_table[j] = cor_table[j].replace(' ', '')
                if table_list[i] == cor_table[j]:
                    table = table + str(pre[i]) + '\n' + str(inner[j])
                    create_table = create_table + str(table) + '\n' + '\n'
                    created_table_num = created_table_num + 1
        print('%s.sql file has been appeared in the current folder'%SQL_file_name+'\n'+'The number of tables created is %d'%(created_table_num))
        # print(table_not_created)
        return create_table

    script = str(gen_database(database_name=DB_name))\
             +'\n'+str(gen_schema())\
             +'\n'+str(gen_table())
    # print(script)

    file_name = SQL_file_name+'.sql'
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(script)

gen_script(DB_name='BNV',file_location='F:\Synodus\DA.BNV\Dim_Fact_Listing_09072022.xlsx',SQL_file_name='create_table')










