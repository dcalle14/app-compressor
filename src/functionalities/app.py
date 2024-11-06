from flask import Flask, render_template, request, redirect, url_for
from model.rle_compression import RLECompression
from controller.table_controller import ControladorTabla

app = Flask(__name__)

# Instancias de los modelos y controladores
rle = RLECompression()
tabla_controller = ControladorTabla()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    data = request.form['data']
    compressed_data = rle.compress(data)
    return render_template('index.html', result=compressed_data)

@app.route('/table', methods=['GET'])
def table():
    table_data = tabla_controller.get_data()
    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
