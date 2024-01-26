from flask import Flask, jsonify,request
from flask_cors import CORS
import pyodbc
from waitress import serve

app = Flask(__name__)
CORS(app)
# Configuración de conexión a la base de datos
dsn_name = 'sql_consulta'
user = 'consulta'
password = 'Consulta_2017'
@app.route('/')
def index():
    return 'hello'

# Ruta para obtener datos desde la base de datos
@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    try:
        # Intenta establecer la conexión utilizando el DSN
        with pyodbc.connect(f'DSN={dsn_name};UID={user};PWD={password};FILEDSN=/etc/odbc.ini') as connection:
            # Conectar a la base de datos
            cursor = connection.cursor()
            # Obtener parámetros de la solicitud
            parametro1 = request.args.get('parametro1')
            parametro2 = request.args.get('parametro2')
            # Ejecutar la función
            cursor.execute("SELECT NOMBRE, TALLOS,CODPRO, REND_HR from dbo.fp_inf_rendimiento_clav2(?,?)" ,(parametro1,parametro2))
            # Obtener resultados
            resultados = cursor.fetchall()
            # Convertir resultados a una lista de diccionarios
            resultados_json = []
            print("Número de resultados:", len(resultados))
            for row in resultados:
                    resultados_json.append(dict(zip([column[0] for column in cursor.description], row)))
            # Cerrar la conexión
            connection.close()
            print(resultados_json)
            # Devolver resultados en formato JSON
            return jsonify(resultados_json)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    serve(app,host = '172.19.10.5',port="8087", threads=2)
