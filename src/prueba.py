from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

@app.route('/')
def index():
    dsn_name = 'sql_consulta'  # Reemplaza con el nombre de tu DSN
    user = 'consulta'
    password = 'Consulta_2017'
    parametro = '20240122'
    try:
        # Intenta establecer la conexión utilizando el DSN
        with pyodbc.connect(f'DSN={dsn_name};UID={user};PWD={password};FILEDSN=/etc/odbc.ini') as connection:
            # Realiza operaciones con la conexión aquí
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM dbo.fp_inf_rendimiento_clav2({parametro},{parametro})')
            # Obtener resultados
            resultados = cursor.fetchall()
            # Convertir resultados a una lista de diccionarios
            resultados_json = []
            print("Aun no hay error")
            for row in resultados:
                resultados_json.append(dict(zip([column[0] for column in cursor.description], row)))
            print("Aun no hay error")
            # Cerrar la conexión
            connection.close()
            print("Aun no hay error")
            # Devolver resultados en formato JSON
            print(resultados_json)
            return jsonify(resultados_json)
    except pyodbc.Error as e:
        return f'Error de conexión: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)