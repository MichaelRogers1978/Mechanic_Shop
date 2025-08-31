import os
from flask import Flask
from flask_migrate import upgrade
from your_app import create_app, db

app = create_app()

with app.app_context():
    allow_reset = os.getenv("ALLOW_DB_RESET", "false").lower() == "true"
    env = app.config.get("ENV", "production")

    if not allow_reset:
        print("DB reset skipped. ALLOW_DB_RESET not set to 'true'.")
        exit(0)

    if env != "development":
        print(f"Refusing to reset DB in '{env}' environment.")
        exit(1)

    print("Dropping all tables...")
    db.drop_all()
    db.create_all()
    upgrade()
    print("DB reset complete.")