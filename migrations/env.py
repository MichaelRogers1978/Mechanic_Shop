import os
import sys
from logging.config import fileConfig
from os.path import join, dirname

from sqlalchemy import engine_from_config, pool
from alembic import context

# Load the Alembic config
config = context.config

# Interpret the config file for Python logging.
config_path = join(dirname(__file__), '..', 'alembic.ini')
fileConfig(config_path)

# Ensure your app is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your app and models
from app import db
from app.models import Customer, Mechanic, ServiceTicket, Inventory  # Add all models here

# Set target metadata for 'autogenerate' support
target_metadata = db.metadata

# Get the DB URL from your app config or environment
db_url = os.getenv('DATABASE_URL')
if not db_url:
    raise RuntimeError("DATABASE_URL environment variable not set.")
config.set_main_option('sqlalchemy.url', db_url)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
