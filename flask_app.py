import os
from app import create_app
from flask_swagger_ui import get_swaggerui_blueprint

config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Mechanic Shop"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)