import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Add the parent folder to Python path so we can import app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Load settings from .env file using your Pydantic config
from config import Settings
from database import Base  # Make sure Base comes from your main SQLAlchemy setup

# ✅ Try to load and validate .env settings
try:
    settings = Settings()
except Exception as e:
    print("❌ Failed to load settings from .env:", e)
    raise

# ✅ Dynamically build the PostgreSQL connection string using environment settings
connection_url = f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

# ✅ Show the connection URL in terminal for debugging (safe in local dev only)
print("🔌 Alembic is using this DB URL:", connection_url)

# ✅ Load Alembic config from alembic.ini
config = context.config

# ✅ Inject the connection string into Alembic config
config.set_main_option("sqlalchemy.url", connection_url)

# ✅ Setup logging from alembic.ini if defined
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set the metadata that Alembic uses for autogenerating migrations
target_metadata = Base.metadata

# 🚀 Function for running migrations in 'offline' mode (generates SQL file only)
def run_migrations_offline() -> None:
    """Run migrations without connecting to the actual database."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# 🚀 Function for running migrations in 'online' mode (connects and applies migrations)
def run_migrations_online() -> None:
    """Run migrations with an active database connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# ▶️ Choose offline or online migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
