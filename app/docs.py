from flask_swagger_ui import get_swaggerui_blueprint

def register_swagger(app):
    swagger_url = "/static/swagger.json"
    api_url = "/static/swagger.json"
    
    swaggerui_bp = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config = app.config["SWAGGER"]
    )
    app.register_blueprint(swaggerui_bp, url_prefix = swagger_url)