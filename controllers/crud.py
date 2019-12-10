import pymysql
import credentials as credentials
import helpers.strings as st

def dbConnection():
    try:
        db_connection = pymysql.connect(credentials.server,credentials.name,credentials.password,credentials.name)
        print(st.success_connection)
        return db_connection    
    except SystemError as err:
        print(st.err + str(err))
        return None

def createTables(db):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) == 0):
            query_workers = ("""
                CREATE TABLE IF NOT EXISTS workers
                (id varchar(255) NOT NULL, 
                name varchar(255) NOT NULL,
                salary varchar(255) NOT NULL)
                ENGINE = InnoDB
            """)
            cursor.execute(query_workers)
            print(st.success_tables)
    except SystemError as err:
        db.rollback()
        print(st.err + str(err))

def getTables(db):
    cursor = db.cursor()
    tablesDatabase = []
    cursor.execute("SHOW TABLES;")
       
    if (cursor.rowcount != 0):
        tablesDatabase = [table[0] for table in cursor]

    return tablesDatabase

def insertData(db, key, name, salary):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) != 0):
            query_workers = ("""INSERT INTO workers(id,name,salary)
                VALUES ('{0}','{1}','{2}')
            """.format(key,name,salary))
            cursor.execute(query_workers)
            db.commit()
            return True
        else:
            return False
    except SystemError as err:
        db.rollback()
        print(err)
        return False

def showData(db):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) != 0):            
            cursor.execute("SELECT * FROM workers")
            workers_result = cursor.fetchall()
            return workers_result       
        else:
            print(st.message_tables)
            return False
    except SystemError as err:
        print(st.err + str(err))
        return False

def deleteData(db):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) != 0):
            query_workers = ("TRUNCATE TABLE workers;")
            cursor.execute(query_workers)
        else:
            print(st.message_tables)
            return False
    except SystemError as err:
        db.rollback()
        print(st.err + str(err))
        return False

def searchData(db, name):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) != 0):
            query = ("SELECT * FROM `workers` WHERE name" + "=%s")
            cursor.execute(query,(name))
            response = cursor.fetchall()
            return response
        else:
            print(st.message_tables)
            return False
    except SyntaxError as err:
        print(st.err + str(err))
        return False

def updateData(db, key, value):
    try:
        cursor = db.cursor()
        tablesDatabase = getTables(db)
        if(len(tablesDatabase) != 0):                     
            query = ("UPDATE workers SET name=%s WHERE id=%s")
            cursor.execute(query,(value,key))
            db.commit()
            return True
        else:
            print(st.message_tables)
            return False
    except SyntaxError as err:
        print(st.err + str(err))
        return False