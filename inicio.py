




from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/mayor')
def mayor():
    return render_template('mayor.html')
@app.route('/sanmiguel')
def sanmiguel():
    return render_template('sami.html')


@app.route('/inc', methods=["POST"])
def resultado():
    n1 = int(request.form.get("n1"))
    n2 = int(request.form.get("n2"))
    mayor = 0
    mensaje = ''
    if n1 == n2:
        mayor = n1
        mensaje = "los dos numeros son iguales "
    if n1 > n2:
        mayor = n1
        mensaje = "el numero mayor es : "
      
        
    elif n2 > n1:
        mayor = n2
        mensaje= "el numero mayor es :"
    return render_template('mayor.html', mayor=mayor, text=mensaje)

@app.route('/enlace')
def enlace():
    dic = [
        {"url": "https://ugb.instructure.com", "texto": "Canvas UGB"},
        {"url": "https://estudiantes.ugb.edu.sv", "texto": "Portal Estudiante"},
        {"url": "https://www.ugb.edu.sv", "texto": "WEB UGB"},
        {"url": "https://biblioteca.ugb.edu.sv/", "texto": "Biblioteca UGB"},]

    return render_template('enlace.html', dic=dic)


    

if __name__ == '__main__':
    app.run(debug=True)