import re
from flask import Flask, jsonify, render_template

app =Flask(__name__)

def is_scientific_number(value):
    
   pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)[eE][+-]?\d+$'
   return re.match(pattern, value) is not None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    number = request.form.get('number', '')
    valid = is_scientific_number(number)
    return jsonify({'number': number, 'valid': valid})

if __name__ == '__main__':
    app.run(debug=False, debug_log=True)
    
