import psycopg2;
import pandas as pd;
import matplotlib.pyplot as plt;


conn = psycopg2.connect(
    dbname="tubasededatos",
    user="tusuario",
    password="tucontra",
    host="tuhost",
    port="tupuerto"
)


query = '''
    SELECT ProductName, SUM(Price * Quantity) as Rentable
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    Group BY od.ProductID, ProductName
    ORDER BY Rentable DESC
    LIMIT 8
'''

# Aca mostramos los datos en consola con pandas
top_products = pd.read_sql_query(query, conn);
print(top_products)

#Aca vamos a usar matplot
# "X" los datos del eje X
# "Y" los datos del eje Y
# "Kind" el tipo de grafico
top_products.plot(x="productname", y="rentable", kind="bar", figsize=(10,5), legend=False);


plt.title("Los productos mas rentables");
plt.xlabel("Products:");
plt.ylabel("Rentabilidad:");
plt.xticks(rotation=90);
plt.show();



#Empleados

query2 = '''
    SELECT FirstName || ' ' || LastName as NombreCompleto, COUNT(*) as TotalOrders
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY e.EmployeeID, FirstName, LastName
    ORDER BY TotalOrders DESC
'''
tabla_empleados = pd.read_sql_query(query2, conn);
print(tabla_empleados)

# Grafico de empleados
tabla_empleados.plot(x="nombrecompleto", y="totalorders", kind="bar", figsize=(10,5), legend=False);


plt.title("Los Empleados mas activos");
plt.xlabel("Nombres:");
plt.ylabel("Ordenes Totales:");
plt.xticks(rotation=90);
plt.show();

conn.close();