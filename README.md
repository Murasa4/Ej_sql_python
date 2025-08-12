# Ej_sql_python

# 🧠 Ejercicio de funciones con python y postgresql

## 📋 Descripción
Practicando un ejercicio con SQL (en Postgresql) + Python, con conexion a la base de datos, creando funciones, en este caso creamos un grafico donde muestra productos mas vendidos y empleados mas activos, use una base de datos de ejemplo de la pagina wikiversity
URL: https://en.wikiversity.org/wiki/Database_Examples/Northwind

---

## 🗂️ Utilizado

- Python
- Visual Studio Code
- Postgresql(PgAdmin)
- Biblotecas: Pandas, Psycopg2, Matplotlib 

---

## ⚙️ Conectar la DB en python:
-- Importe en este caso psycopgh2

```bash
conn = psycopg2.connect(
    dbname="tubasededatos",
    user="tusuario",
    password="tucontra",
    host="tuhost",
    port="tupuerto"
)
