from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello,chudailllllllllllllllllllllllllllllllllllllll kuch bolllllllllllllllllllll yeh wala practical ho gyaaaaaaaaaaaa!"

if __name__ == "__main__":
    app.run()
