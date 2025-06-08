from flask import Flask, render_template, request

app = Flask(__name__)

def lower_triangle(n):
    return '\n'.join(['* ' * (i + 1) for i in range(n)])

def upper_triangle(n):
    return '\n'.join(['  ' * i + '* ' * (n - i) for i in range(n)])

def pyramid(n):
    return '\n'.join([' ' * (n - i - 1) + '* ' * (i + 1) for i in range(n)])

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'lower': '', 'upper': '', 'pyramid': ''}
    n = None

    if request.method == 'POST':
        try:
            n = int(request.form.get('number'))
            result['lower'] = lower_triangle(n)
            result['upper'] = upper_triangle(n)
            result['pyramid'] = pyramid(n)
        except ValueError:
            n = None

    return render_template('index.html', result=result, n=n)

if __name__ == '__main__':
    app.run(debug=True)
