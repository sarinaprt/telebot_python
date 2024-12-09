from mysql.connector import connection, Error



def insert_USER(cid,first_name,last_name=None,created=None,updated_at=None,status=None):
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn = connection.MySQLConnection(**config)
    cur=conn.cursor()
    SQL_QUERY = "INSERT INTO USER (cid,first_name, last_name, created, updated_at, status) VALUES (%s, %s, %s, %s, %s, %s)ON DUPLICATE KEY UPDATE cid=values(cid),first_name=values(first_name),updated_at=values(updated_at)"
    cur.execute(SQL_QUERY, (cid,first_name, last_name, created, updated_at, status))    
    # ID=cur.lastrowid  ایدی اخرین نفری که جون بشه رو با پرینت نشون میده

    conn.commit()      # اعمال تغییرات در پایگاه داده
    cur.close()
    conn.close()
    print("insert u")
# sql_qiery="insert into customer(first_name,last_name,email,point,created_at,updated_at,status)values(%s,%s,%s,%s,%s,%s,%s)"
# cur.execute (sql_qiery,(first_name,last_name,email,point,created_at, updated_at , status))





def insert_product(product_name,discription=None,MID=None,cATEGORY=None,price=None,point_p=None):
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn = connection.MySQLConnection(**config)
    cur=conn.cursor()
    sql_query = "INSERT INTO products_mo (product_name,discription,MID,cATEGORY,price,point_p) VALUES ( %s, %s, %s, %s, %s, %s)"
    cur.execute(sql_query, (product_name,discription,MID,cATEGORY,price,point_p))    
    conn.commit()
    print("gk")    
    cur.close()
    conn.close()



def insert_sell_row(cid,qty,sum_price):
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn = connection.MySQLConnection(**config)
    cur=conn.cursor()
    sql_query = "INSERT INTO sell (cid,qty,sum_price) VALUES (%s,%s,%s)"
    cur.execute(sql_query, (cid,qty,sum_price))    
    conn.commit()    
    cur.close()
    conn.close()  
    
def insert_movie_ratings(product_name,cid,RATING):   
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn = connection.MySQLConnection(**config)
    cur=conn.cursor()
    sql_query = "INSERT INTO movie_rating (product_name,cid,RATING) VALUES (%s,%s,%s)"
    cur.execute(sql_query, (product_name,cid,RATING))    
    conn.commit()    
    cur.close()
    conn.close()   
    
 
# def insert_movie_categories(category_name):  نوع فیلم
#     config={'user':'root','password':'password','host':'localhost','database':'database'}
#     conn=mysql.connector.connect(**config )
#     cur=conn.cursor()
#     sql_query = "INSERT INTO movie_categories (category_name) VALUES (%s)"
#     cur.execute(sql_query, (category_name))    
#     conn.commit()    
#     cur.close()
#     conn.close()   
        
 
    
# def insert_movie_category_relations(PRODUCT_ID,category_id):
#     config={'user':'root','password':'password','host':'localhost','database':'database'}
#     conn=mysql.connector.connect(**config )
#     cur=conn.cursor()
#     sql_query = "INSERT INTO movie_category_relations (PRODUCT_ID,category_id) VALUES (%s,%s)"
#     cur.execute(sql_query, (PRODUCT_ID,category_id))    
#     conn.commit()    
#     cur.close()
#     conn.close()


# def insert_watch_history(PRODUCT_ID,CID,watch_date):   تاریخ چه فرد
#     config={'user':'root','password':'password','host':'localhost','database':'database'}
#     conn=mysql.connector.connect(**config )
#     cur=conn.cursor()
#     sql_query = "INSERT INTO watch_history (PRODUCT_ID,CID,watch_date) VALUES (%s,%s,%s)"
#     cur.execute(sql_query, (PRODUCT_ID,CID,watch_date))    
#     conn.commit()    
#     cur.close()
#     conn.close()


    
if __name__=='__main__':
    insert_USER()
    insert_product()
    insert_sell_row()
    # insert_movie_ratings()
    # insert_movie_categories()
    # insert_movie_category_relations()
    # insert_watch_history()