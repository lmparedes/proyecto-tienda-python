# Steps
# Store Project

#Este proyecto consiste en una herramienta de línea de comandos (CMD) que permite gestionar
 un sistema ABM simple

#Comandos a ser ejecutados 
```
1. Agregar categoría
python app.py agregar_categoria "Nombre de la categoría" --descripcion "Texto opcional"

2. Editar categoría
python app.py editar_categoria ID --nombre "Nuevo nombre" --descripcion "Nueva descripción"

3. Eliminar categoría
python app.py eliminar_categoria ID

4. Listar categorías
python app.py listar_categorias

ABM de PRODUCTOS
1. Agregar producto
python app.py agregar_producto CATEGORIA_ID "Nombre" --descripcion "Texto" --precio 100 --stock 10

2. Editar producto

Puedes modificar uno o varios campos:

python app.py editar_producto ID --categoria_id 2 --nombre "Nuevo nombre" --descripcion "Nueva desc" --precio 30 --stock 100

3. Eliminar producto
python app.py eliminar_producto ID

4. Listar productos
python app.py listar_productos

--filtros
Filtrar por categoría:
python app.py filtrar_productos --categoria_id 3

Filtrar por rango de precio:
python app.py filtrar_productos --precio_min 300 --precio_max 600

Filtrar por texto (nombre o descripción):
python app.py filtrar_productos --texto "smartph"

Filtrar combinando criterios:
python app.py filtrar_productos --categoria_id 2 --texto "tele" --precio_max 600

--exportar csv

Exportar todo:
python app.py exportar_csv

Exportar productos de una categoría:
python app.py exportar_csv --categoria_id 2

Exportar por rango de precio:
python app.py exportar_csv --precio_min 300 --precio_max 600

Exportar filtrando por texto:
python app.py exportar_csv --texto "smartph"

Exportar a un archivo con nombre personalizado:
python app.py exportar_csv --archivo filtrado_tienda.csv

```