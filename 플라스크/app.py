from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'hello'

def main():
    app.run(host='0.0.0.0', debug=False, port=5001)

if __name__ == '__main__':
    main() 