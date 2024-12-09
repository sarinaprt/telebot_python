
from mysql.connector import connection, Error

def drop_create_database(project_robat):
    config = {'user': 'root','password': 'password','host': 'localhost'}
    try:
        conn = connection.MySQLConnection(**config)
        cur = conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {database}")
        cur.execute(f"CREATE DATABASE {database}")
        # تأیید تغییرات
        conn.commit()  
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn.is_connected():
            conn.close()






def USER():
    # config={'user':'root','password':'belive_god1527','host':'localhost','database':'project_robat'}
    # conn=mysql.connector.connect(usedr='root',password='paaword',host='localhost')
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS USER (
        cid          BIGINT  UNSIGNED NOT NULL PRIMARY KEY ,
        first_name   VARCHAR(50) NOT NULL,
        last_name    VARCHAR(60) ,
        created      DATETIME DEFAULT CURRENT_TIMESTAMP, 
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        status        ENUM('active', 'inactive', 'banned') DEFAULT 'active');""")          
    
    conn.commit()  
    print("user")
    cur.close()
    conn.close() 


   

def product():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products_mo (
    product_id       INT AUTO_INCREMENT PRIMARY KEY,
    product_name     VARCHAR(100) NOT NULL,
    discription      text,
    MID              INT UNSIGNED, 
    cATEGORY         ENUM('وحشت', 'علمی تخیلی', 'اکشن', 'کمدی', 'درام', 'وسترن', 'فانتزی', 'جنگی', 'خانوادگی', 'جنایی', 'عاشقانه', 'انیمیشن', 'معمایی و رازآلود', 'حماسی و تاریخی', 'ماجراجویی', 'پیشنهاد برای شما'),
    price            DECIMAL(10,2),  
    point_p          TINYINT UNSIGNED CHECK(point_p BETWEEN 1 AND 10)
)""")
    
    conn.commit()
    print("product")
    cur.close()
    conn.close() 
    
    
def sell_row():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sell(
    sell_id       INT AUTO_INCREMENT PRIMARY KEY,
    product_id    INT  ,
    cid           BIGINT UNSIGNED,
    qty           SMALLINT NOT NULL,
    sum_price      int NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products_mo(product_id) ,
    FOREIGN KEY(cid) REFERENCES USER(cid) 
)""")
    
    conn.commit() 
    print("sell_row")
    cur.close()
    conn.close() 
    
  
def movie_ratings():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS movie_rating (         
    rat_ID        INT AUTO_INCREMENT PRIMARY KEY,
    cid           BIGINT UNSIGNED,
    product_id    INT,
    RATING        INT CHECK(RATING BETWEEN 1 AND 10),
    FOREIGN KEY(cid) REFERENCES USER(cid) ,
    FOREIGN KEY(product_id) REFERENCES products_mo(product_id) 
)""")
        
    conn.commit()  
    print("movie_ratings")
    cur.close()
    conn.close() 
    

def movie_categories ():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS movie_categories (
        category_id      INT AUTO_INCREMENT PRIMARY KEY,
        category_name    VARCHAR(255) NOT NULL
)""")
    conn.commit()  
    print("movie_categories")
    cur.close()
    conn.close() 



def movie_category_relations ():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS movie_category_relations (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    PRODUCT_ID    INT,
    category_id   INT,
    FOREIGN KEY (product_id) REFERENCES products_mo(product_id),
    FOREIGN KEY (category_id) REFERENCES movie_categories(category_id)
)""")
    
    conn.commit() 
    print("movie_category_relations") 
    cur.close()
    conn.close() 

   
def watch_history ():
    config ={'user':'root', 'password':'password','host':'localhost','database':'database'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS watch_history (
    id_HISTORY           INT AUTO_INCREMENT PRIMARY KEY,
    CID                  BIGINT UNSIGNED,
    product_id           INT,
    watch_date           DATETIME,
    FOREIGN KEY (CID) REFERENCES user(CID),
    FOREIGN KEY (product_id) REFERENCES products_mo(product_id)
)""")
    
    conn.commit() 
    print("watch_history") 
    cur.close()
    conn.close() 
    
    
if __name__ == '__main__':
    database = 'database'  
    drop_create_database(database)
    USER()
    product()
    sell_row()
    movie_ratings()
    movie_categories ()
    movie_category_relations ()
    watch_history ()
      
# این کد فقط یک بار اولش نوشته میشه





















