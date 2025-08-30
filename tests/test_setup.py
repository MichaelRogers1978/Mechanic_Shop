from alembic.config import Config
from alembic import command

def apply_migrations():
    alembic_cfg = Config("migrations/alembic.ini")
    command.upgrade(alembic_cfg, "head")