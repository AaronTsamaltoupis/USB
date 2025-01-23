from flask import Flask


app = Flask(__name__)
app.config["DEBUG"]=True

@app.route("/name/<name>")

def index(name):
    if name.lower() == "michael":
        return(f'hello {name} old mf', 200)
    else:
        return("not found", 404)



if __name__ == "__main__":
    app.run()



