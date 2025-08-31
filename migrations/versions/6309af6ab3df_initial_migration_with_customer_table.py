from alembic import op
import sqlalchemy as sa
from datetime import datetime

# Revision identifiers, used by Alembic.
revision = '6309af6ab3df'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('email', sa.String(300), nullable=False, unique=True),
        sa.Column('phone', sa.String(200), nullable=True),
        sa.Column('address', sa.String(200), nullable=False),
        sa.Column('password', sa.String(300), nullable=True)
    )

    op.create_table(
        'mechanic',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(150), nullable=False, unique=True),
        sa.Column('email', sa.String(300), nullable=False, unique=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('phone', sa.String(200), nullable=False),
        sa.Column('address', sa.String(200), nullable=False),
        sa.Column('hours_worked', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('password', sa.String(250), nullable=True),
        sa.Column('specialty', sa.String(100), nullable=True)
    )

    op.create_table(
        'service_ticket',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customer.id'), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('status', sa.String(50), nullable=False, server_default='open'),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('vehicle_id', sa.String(200), nullable=True),
        sa.Column('hours_worked', sa.Integer(), nullable=True, server_default='0'),
        sa.Column('repair', sa.String(500), nullable=True)
    )

    op.create_table(
        'inventory',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False, server_default='0')
    )

    op.create_table(
        'service_ticket_inventory',
        sa.Column('service_ticket_id', sa.Integer(), nullable=False),
        sa.Column('inventory_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['inventory_id'], ['inventory.id']),
        sa.ForeignKeyConstraint(['service_ticket_id'], ['service_ticket.id']),
        sa.PrimaryKeyConstraint('service_ticket_id', 'inventory_id')
    )

    op.create_table(
        'service_ticket_mechanic',
        sa.Column('service_ticket_id', sa.Integer(), nullable=False),
        sa.Column('mechanic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['mechanic_id'], ['mechanic.id']),
        sa.ForeignKeyConstraint(['service_ticket_id'], ['service_ticket.id']),
        sa.PrimaryKeyConstraint('service_ticket_id', 'mechanic_id')
    )

    with op.batch_alter_table('mechanic', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.create_unique_constraint(None, ['email'])
        
def downgrade():
    with op.batch_alter_table('mechanic', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    op.drop_table('service_ticket_mechanic')
    op.drop_table('service_ticket_inventory')
    op.drop_table('inventory')
    op.drop_table('service_ticket')
    op.drop_table('mechanic')
    op.drop_table('customer')  
