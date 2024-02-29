from flask import Flask, render_template, request

app = Flask(__name__)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        try:
            temperature = float(request.form['temperature'])
            convert_from = request.form['convert_from']
            convert_to = request.form['convert_to']

            if convert_from == 'fahrenheit' and convert_to == 'celsius':
                result = fahrenheit_to_celsius(temperature)
                result_unit = "Celsius"
            elif convert_from == 'celsius' and convert_to == 'fahrenheit':
                result = celsius_to_fahrenheit(temperature)
                result_unit = "Fahrenheit"
            else:
                result = temperature
                result_unit = convert_from.title()

            return render_template('index.html', temperature=temperature, result=result, result_unit=result_unit)

        except ValueError:
            error_message = "Invalid input. Please enter a valid number."
            return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
