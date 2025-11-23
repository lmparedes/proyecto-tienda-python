# app.py
import argparse
from db import get_connection

# ---------------- CATEGORÍAS ----------------
def agregar_categoria(nombre, descripcion):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s) RETURNING id;",
            (nombre, descripcion)
        )
        conn.commit()
        print(f"Categoría creada con ID {cursor.fetchone()[0]}")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def editar_categoria(id, nombre=None, descripcion=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if nombre:
            cursor.execute("UPDATE categorias SET nombre=%s WHERE id=%s;", (nombre, id))
        if descripcion:
            cursor.execute("UPDATE categorias SET descripcion=%s WHERE id=%s;", (descripcion, id))
        conn.commit()
        print("Categoría actualizada.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_categoria(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM categorias WHERE id=%s;", (id,))
        conn.commit()
        print("Categoría eliminada.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def listar_categorias():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nombre, descripcion, created_at, updated_at FROM categorias;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# ---------------- PRODUCTOS ----------------
def agregar_producto(categoria_id, nombre, descripcion, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO productos (categoria_id, nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
            (categoria_id, nombre, descripcion, precio, stock)
        )
        conn.commit()
        print(f"Producto creado con ID {cursor.fetchone()[0]}")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def editar_producto(id, categoria_id=None, nombre=None, descripcion=None, precio=None, stock=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if categoria_id:
            cursor.execute("UPDATE productos SET categoria_id=%s WHERE id=%s;", (categoria_id, id))
        if nombre:
            cursor.execute("UPDATE productos SET nombre=%s WHERE id=%s;", (nombre, id))
        if descripcion:
            cursor.execute("UPDATE productos SET descripcion=%s WHERE id=%s;", (descripcion, id))
        if precio is not None:
            cursor.execute("UPDATE productos SET precio=%s WHERE id=%s;", (precio, id))
        if stock is not None:
            cursor.execute("UPDATE productos SET stock=%s WHERE id=%s;", (stock, id))
        conn.commit()
        print("Producto actualizado.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE id=%s;", (id,))
        conn.commit()
        print("Producto eliminado.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def listar_productos():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT p.id, p.nombre, p.descripcion, p.precio, p.stock, c.nombre AS categoria, p.created_at, p.updated_at
            FROM productos p
            JOIN categorias c ON p.categoria_id = c.id;
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# ---------------- CLI ----------------
def main():
    parser = argparse.ArgumentParser(description="Gestión de Categorías y Productos")
    subparsers = parser.add_subparsers(dest="comando")

    # ----- Categorías -----
    parser_agregar_cat = subparsers.add_parser("agregar_categoria")
    parser_agregar_cat.add_argument("nombre")
    parser_agregar_cat.add_argument("--descripcion", default="")

    parser_editar_cat = subparsers.add_parser("editar_categoria")
    parser_editar_cat.add_argument("id", type=int)
    parser_editar_cat.add_argument("--nombre")
    parser_editar_cat.add_argument("--descripcion")

    parser_eliminar_cat = subparsers.add_parser("eliminar_categoria")
    parser_eliminar_cat.add_argument("id", type=int)

    subparsers.add_parser("listar_categorias")

    # ----- Productos -----
    parser_agregar_prod = subparsers.add_parser("agregar_producto")
    parser_agregar_prod.add_argument("categoria_id", type=int)
    parser_agregar_prod.add_argument("nombre")
    parser_agregar_prod.add_argument("--descripcion", default="")
    parser_agregar_prod.add_argument("--precio", type=float, default=0)
    parser_agregar_prod.add_argument("--stock", type=int, default=0)

    parser_editar_prod = subparsers.add_parser("editar_producto")
    parser_editar_prod.add_argument("id", type=int)
    parser_editar_prod.add_argument("--categoria_id", type=int)
    parser_editar_prod.add_argument("--nombre")
    parser_editar_prod.add_argument("--descripcion")
    parser_editar_prod.add_argument("--precio", type=float)
    parser_editar_prod.add_argument("--stock", type=int)

    parser_eliminar_prod = subparsers.add_parser("eliminar_producto")
    parser_eliminar_prod.add_argument("id", type=int)

    subparsers.add_parser("listar_productos")

    args = parser.parse_args()

    # ----- Ejecutar comandos -----
    if args.comando == "agregar_categoria":
        agregar_categoria(args.nombre, args.descripcion)
    elif args.comando == "editar_categoria":
        editar_categoria(args.id, args.nombre, args.descripcion)
    elif args.comando == "eliminar_categoria":
        eliminar_categoria(args.id)
    elif args.comando == "listar_categorias":
        listar_categorias()
    elif args.comando == "agregar_producto":
        agregar_producto(args.categoria_id, args.nombre, args.descripcion, args.precio, args.stock)
    elif args.comando == "editar_producto":
        editar_producto(args.id, args.categoria_id, args.nombre, args.descripcion, args.precio, args.stock)
    elif args.comando == "eliminar_producto":
        eliminar_producto(args.id)
    elif args.comando == "listar_productos":
        listar_productos()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
