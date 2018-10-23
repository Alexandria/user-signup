from flask import Flask

app = Flask(__name__)
app.config['DEBUG']=True #port500

form = """
    <!DOCTYPE HTML>
    <html>
        <head>
        </head>
        <body>
            <h1> Sign Up information </h1>
            <form>
                <label>
                    Username:
                    <input type = "text" name = "user-name"  />
                </labe>


            </form>


        </body>

    </html>

"""
@app.route('/')
def showForm():
    return form


app.run()