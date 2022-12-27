from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def form_page():
    return '''<form action=/add> 
     <input type="submit" name="s"
     value = "кнопка">
     </form>'''
@app.route("/add")
def add_page():
    temp=request.args["s"]
    return f"Нажали {temp}"
app.run()
