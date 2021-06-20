from SQL_Query import create_table_queries, drop_table_queries
import psycopg2 as pg


def create_db():
    """
        Return connection and cursor to sparkify DB
    """
    # connect to defualt database
    con = pg.connect(
        'dbname=udacity host=127.0.0.1 user=postgres password=admin')
    con.set_session(autocommit=True)
    cur = con.cursor()

    # create sparkify database
    cur.execute('drop database if exists sparkifydb')
    cur.execute(
        "create database sparkifydb with encoding'utf-8';")

    cur.close()
    con.close()

    # connect to sparkify database
    con = pg.connect(
        'host=127.0.0.1 dbname=sparkifydb user=postgres password=admin')
    cur = con.cursor()

    return cur, con


def drop_tables(cur, con):
    """
    Drop each existing table from Sparkify database.
    """
    for query in drop_table_queries:
        cur.execute(query)
        con.commit()


def create_tables(cur, con):
    """
    Create tables in sparkify database.
    """
    for query in create_table_queries:
        cur.execute(query)
        con.commit()


def main():
    cur, con = create_db()
    drop_tables(cur, con)
    create_tables(cur, con)
    con.close()


if __name__ == "__main__":
    main()
