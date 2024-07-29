import pandas as pd
from sqlalchemy import  create_engine

def create_connection(host,user,password,databse):
    connection_string = f"mysql+pymysql://{user}:{password}@{host}/{databse}"
    engine = create_engine(connection_string)
    return engine

def fetch_data(engine, query):
    with engine.connect() as connection:
        return pd.read_sql(query,connection)

def main():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password':'password123',
        'database': 'test'

    }

    engine = create_connection(
        user = db_config['user'],
        host=db_config['host'],
        password=db_config['password'],
        databse=db_config['database']
    )

    sql_query_employee = " SELECT * FROM employee"
    sql_query_manager = "SELECT * FROM manager"
    sql_query_department = "SELECT * FROM  department"

    df_employee = fetch_data(engine, sql_query_employee)
    df_manager = fetch_data(engine, sql_query_manager)
    df_department = fetch_data(engine, sql_query_department)
    print("employee dataframe:")
    print(df_employee)
    print("\n manager dataframe:")
    print(df_manager)
    print("\n department dataframe:")
    print(df_department)

if __name__ == "__main__":
    main()   




























"""
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password123',
    'database': 'test'
}

connection = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)

sql_query = "SELECT * FROM employee"

df = pd.read_sql(sql_query, connection)

connection.close()

print(df)
"""
