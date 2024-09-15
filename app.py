from flask import Flask
from routes.entregas import entrega_blueprint

app = Flask(__name__)

# Registrar as rotas
app.register_blueprint(entrega_blueprint, url_prefix='/api/entregas')

if __name__ == '__main__':
    app.run(debug=True)