from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/index.html')
def index():
    return render_template("index.html")
    
@app.route('/gallery.html')
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)