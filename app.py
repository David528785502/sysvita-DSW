from flask import Flask
from flask_cors import CORS
import os

from config import config
# Routes
from routes import Usuario

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Usuario.main, url_prefix='/api/usuarios')

    # Error handlers
    app.register_error_handler(404, page_not_found)

    # Obtener el puerto del entorno, si no está disponible, usar 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
