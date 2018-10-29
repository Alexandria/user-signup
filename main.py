from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True #port5000

form = """
    <!DOCTYPE HTML>
    <html>
        <head>
                <style>
                    .error {{ color: red; }}
                </style>
        </head>
        <body>
            <h1> Sign Up </h1>
            <form  method = 'POST'>
                <label>
                    Username:
                    <input type = "text" name = "user" value = '{user}' />
                </labe>
                    <p class = "error">{uname_error}</p>
                <br/>
                <label>
                    Password:
                    <input type = "text" name = "password" value = '{password}' />
                </labe>
                <br/>
                </labe>
                     <p class = "error">{password_error}</p>
                <label>
                <label>
                    Verify Password:
                    <input type = "text" name = "password-verify"  value = '{verify_pword}' />
                </labe>
                     <p class = "error">{verify_error}</p>
                <label>
                <br/>
                    Email:
                    <input type = "text" name = "email" value = '{email}'  />
                </labe>
                    <p class = "error">{email_error}</p>

                    <input type = 'submit' name = 'submit' value = 'Sign Up'>


            </form>


        </body>

    </html>

"""
@app.route('/')
def showForm():
    return form.format(user='', uname_error = '',
     password='', verify_pword='', password_error = ''
     , email='', email_error='' , verify_error = '')

@app.route('/', methods=['POST'])
def validate():
    user = request.form.get('user')
    password = request.form.get('password')
    verify_pword = request.form.get('password-verify')
    email = request.form.get('email')
   
    uname_error = ''
    verify_error = ''
    password_error = ''
    email_error = ''

    # Checking to make sure there are no blank areas
    
    if user is "":
        uname_error = "Please enter a username."
    if password is "":
        password_error = "Please enter a password."
    if verify_pword is "":
        verify_error += " Please verify your password"
  
    # cheacking to make sure all submission is valid    
    if len(user) < 3 or len(user) > 20:
        uname_error = "Please verify your user name is greater than 3 characters and less than 20."
    for char in user:
         if char == " " :
            uname_error += " User name can not have any spaces." 
            break
    
    if len(password) < 3 or len(user) > 20:
        password_error = "Please verify your password is greater than 3 characters and less than 20."
        password = ''
        verify_pword = ''
    for char in password:
         if char == " " :
            password_error += " Your password can not have any spaces." 
            password = ''
            verify_pword = ''
            break

    # We are verifying that the password and password verify both match
    if password != verify_pword:
        verify_error = "Password does not match"
        password = ''
        verify_pword = ''

    # verifying the email address. 
    if "@" not in email or "." not in email:
        email_error = "Please enter a valid email address"
    for char in email:
         if char == " " :
            email_error += " Your password can not have any spaces." 
            break
    if not email_error and not uname_error and not password_error and not verify_error:
        name = user
        return redirect('/done?name={0}'.format(name))

    

    return form.format(user = user, uname_error = uname_error , password =password
    , verify_pword= verify_pword , password_error = password_error, verify_error = verify_error
    , email = email, email_error = email_error)

@app.route('/done')
def welcome():
    name = request.args.get('name')
    return "<h1>Welome, {0}</h1>".format(name)

app.run()