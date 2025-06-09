from dotenv import load_dotenv
load_dotenv()
import os

# Debug prints for validation
print("Loaded DB USER from .env:", os.environ.get("DATABASE_USER"))
print("Loaded DB PASSWORD from .env:", os.environ.get("DATABASE_PASSWORD"))

from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# Alembic config object
config = context.config

# Use full DATABASE_URL directly from .env
# Fallback to constructing manually if needed
if os.environ.get("DATABASE_URL"):
    config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])
else:
    config.set_main_option(
        "sqlalchemy.url",
        f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}"
    )

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set to your models' Base.metadata if autogenerate is needed
target_metadata = None

def run_migrations_offline() -> None:
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

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
