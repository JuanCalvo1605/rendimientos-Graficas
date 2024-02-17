from flask import Flask, jsonify,request
from flask_cors import CORS
import pyodbc
from waitress import serve

app = Flask(__name__)
CORS(app)
# Configuración de conexión a la base de datos
server = '172.19.10.11'
database = 'ANDES'
username = 'consulta'
password = 'Consulta_2017'
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
@app.route('/')
def index():
    return 'hello '

# Ruta para obtener datos desde la base de datos
@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    try:
        # Conectar a la base de datos
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        # Obtener parámetros de la solicitud
        parametro1 = request.args.get('parametro1')
        parametro2 = request.args.get('parametro2')
        # Ejecutar la función
        cursor.execute("SELECT NOMBRE, REND_HR, CODPRO from dbo.fp_inf_rendimiento_clav2(?,?)" ,(parametro1,parametro2))
        # Obtener resultados
        resultados = cursor.fetchall()
        # Convertir resultados a una lista de diccionarios
        resultados_json = []
        for row in resultados:
            resultados_json.append(dict(zip([column[0] for column in cursor.description], row)))
        # Cerrar la conexión
        connection.close()

        # Devolver resultados en formato JSON
        return jsonify(resultados_json)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    serve(app,host = '172.19.10.8',port="8087", threads=2)