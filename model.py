import psycopg2 as pg

def create_database():
    con = pg.connect(
        user='postgres',
        password='297520',
    )
    con.autocommit = True
    sql = 'CREATE DATABASE Mercado;'
    cursor = con.cursor()
    cursor.execute(sql)
    print('Criado')

def create_tables():
    con = pg.connect(
        database='mercado',
        user='postgres',
        password='297520'
    )
    cursor = con.cursor()
    sql = '''CREATE TABLE estoque(
        id SERIAL PRIMARY KEY,
        produto VARCHAR(255) NOT NULL,
        tipo INT
    );'''
    cursor.execute(sql)
    print('Table estoque Criado\n')

    sql = '''CREATE TABLE categoria(
        id SERIAL PRIMARY KEY,
        tipo VARCHAR(255) NOT NULL,
        qtde INT
    );'''
    cursor.execute(sql)
    print('Table categoria Criado\n')
    con.commit()

def inserir_produto(produto, categoria, qtde):
    con = pg.connect(
        database='mercado',
        user='postgres',
        password='297520',
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO estoque(produto, tipo, qtde) VALUES('%s', %d, %d);"%(produto, categoria, qtde))
    con.commit()
    buscar_categorias_id(produto)
    

def inserir_categoria(categoria):
    con = pg.connect(
        database='mercado',
        user='postgres',
        password='297520',
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO categoria(tipo) VALUEs('%s');"%(categoria))
    con.commit()

def buscar(produto):
    con = pg.connect(
        database='mercado',
        user='postgres',
        password='297520',
    )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM estoque WHERE LOWER(produto) LIKE LOWER('%s')"%(produto.lower()))
    lista = cursor.fetchall()
    return lista

def buscar_categorias():
    con = pg.connect(
        database='mercado',
        user='postgres',
        password='297520',
    )
    cursor = con.cursor()
    cursor.execute('SELECT tipo FROM categoria;')
    tipos = cursor.fetchall()
    return tipos

def buscar_categorias_id(categoria):
    con = pg.connect(
        database='mercado',
        user='postgres',
        password=297520
    )
    cursor = con.cursor()
    cursor.execute("SELECT id FROM categoria WHERE LOWER(tipo) = LOWER('%s')"%(categoria))
    id_categoria = cursor.fetchone()
    return id_categoria

try: 
    create_tables()
except:
    pass
