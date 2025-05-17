"""create todos table

Revision ID: ad1c380734f8
Revises: 
Create Date: 2023-12-03 13:25:00.622096

"""

# Alembic-specific imports for managing schema changes
from typing import Sequence, Union
from alembic import op  # op = "operations", used to perform SQL schema commands
import sqlalchemy as sa  # SQLAlchemy, used for column types and more

# Alembic revision identifiers
revision: str = 'ad1c380734f8'  # Unique ID for this migration
down_revision: Union[str, None] = None  # There is no previous migration (this is the first one)
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # This function is run when you apply the migration (alembic upgrade)
    # It creates the todos table directly using raw SQL (not the SQLAlchemy table syntax)
    op.execute("""
    create table todos(
        id bigserial primary key,        -- Automatically incrementing unique ID
        name text,                       -- The name or title of the todo item
        completed boolean not null default false  -- Whether the task is done, defaults to false
    )
    """)

def downgrade():
    # This function is run when you rollback the migration (alembic downgrade)
    # It simply deletes the todos table
    op.execute("drop table todos;")


# -----------------------------------------------
# ALEMBIC MIGRATION EXPLAINED
# -----------------------------------------------

# 🆕 What is this file?
# This is an Alembic "migration script" — it defines what changes to make to the database schema.

# 🧠 What does upgrade() do?
# - It creates a new table called "todos" using raw SQL.
# - The table has 3 columns:
#     1. id (auto-incremented primary key)
#     2. name (text field for the todo item title)
#     3. completed (boolean, defaults to false)

# 🔄 What does downgrade() do?
# - It reverses the migration by dropping the "todos" table.

# 🛠 Why use raw SQL here instead of SQLAlchemy?
# - You *can* use SQLAlchemy's table definition tools (like op.create_table), 
#   but raw SQL works just as well — especially for simple tables.

# 🔁 When you run "alembic upgrade head", this script is executed.

# ✅ When you run "alembic downgrade -1", the downgrade() part is executed to undo the change.

# 🧱 This is your starting point for building database schemas using version control!
