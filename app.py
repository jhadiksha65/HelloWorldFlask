from flask import Flask

app = Flask(__name__)

print("User Authentication Feature Branch")

@app.route("/")
def home():
return "Main Branch Version and Feature Branch Version"

if __name__ == "__main__":
    app.run(debug=True)