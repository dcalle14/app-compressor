from flask import Flask, render_template, request, redirect, url_for
from model.rle_compression import RLECompression
from controller.table_controller import TableController

# Initialize Flask application
app = Flask(__name__)

# Initialize RLE compression and table controller instances
rle = RLECompression()
table_controller = TableController()

@app.route('/')
def index():
    # Render the main page template
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    # Retrieve data from the form submission
    data = request.form['data']
    # Perform RLE compression on input data
    compressed_data = rle.compress(data)
    # Render template with compression result
    return render_template('index.html', result=compressed_data)

@app.route('/table', methods=['GET'])
def table():
    # Fetch table data from the table controller
    table_data = table_controller.get_data()
    # Render template with table data
    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    # Run Flask application in debug mode for development
    app.run(debug=True)
