from flask import Flask

from flask_qrcode import QRcode  # For use to generate QR Codes


def create_application():
    app = Flask(__name__)

    # Initializations
    QRcode(app)

    # blueprint for non-auth parts of app
    from .home.routes import home as main_blueprint
    from .api.routes import api as api_blueprint

    # Register non Auth Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


