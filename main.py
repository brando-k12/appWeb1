#importacion de librerias
from flask import Flask,render_template
#creacion de objeto tipo flask

app = Flask(__name__)
#creacion de ruta a pagina principal
@app.route("/")
#cracion de funcion para llamar a index (pagina principal)
def index():

    return render_template("index.html")

#definir el servidor web
if __name__ == '__main__':
    #configuracion del puerto de escucha del servidor web
      app.run(port = 80,debug = True)




