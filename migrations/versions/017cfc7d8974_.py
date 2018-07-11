"""empty message

Revision ID: 017cfc7d8974
Revises: 29424b81dc04
Create Date: 2018-07-11 22:35:43.940013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017cfc7d8974'
down_revision = '29424b81dc04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('collection', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_collection_id'), 'collection', ['id'], unique=False)
    op.create_table('cuisine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cuisine', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cuisine_id'), 'cuisine', ['id'], unique=False)
    op.create_table('dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('dish', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dish_id'), 'dish', ['id'], unique=False)
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(asdecimal=True), nullable=True),
    sa.Column('longitude', sa.Float(asdecimal=True), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('Category', sa.Integer(), nullable=True),
    sa.Column('featured', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_restaurant_id'), 'restaurant', ['id'], unique=False)
    op.create_table('association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('dish_id', sa.Integer(), nullable=True),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.Column('cuisine_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collection.id'], ),
    sa.ForeignKeyConstraint(['cuisine_id'], ['cuisine.id'], ),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_association_id'), 'association', ['id'], unique=False)
    op.create_table('restaurant_amenity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('home_delivery', sa.Boolean(), nullable=True),
    sa.Column('private_dining_area_available', sa.Boolean(), nullable=True),
    sa.Column('kid_friendly', sa.Boolean(), nullable=True),
    sa.Column('table_reservation_required', sa.Boolean(), nullable=True),
    sa.Column('table_booking_recommended', sa.Boolean(), nullable=True),
    sa.Column('wheelchair_accessible', sa.Boolean(), nullable=True),
    sa.Column('buffet', sa.Boolean(), nullable=True),
    sa.Column('wifi', sa.Boolean(), nullable=True),
    sa.Column('live_entertainment', sa.Boolean(), nullable=True),
    sa.Column('live_music', sa.Boolean(), nullable=True),
    sa.Column('live_sports_screening', sa.Boolean(), nullable=True),
    sa.Column('valet_parking', sa.Boolean(), nullable=True),
    sa.Column('parking', sa.Boolean(), nullable=True),
    sa.Column('group_meal', sa.Boolean(), nullable=True),
    sa.Column('smoking_area', sa.Boolean(), nullable=True),
    sa.Column('desserts_and_bakes', sa.Boolean(), nullable=True),
    sa.Column('full_bar_available', sa.Boolean(), nullable=True),
    sa.Column('serves_jain_food', sa.Boolean(), nullable=True),
    sa.Column('vegetarian_only', sa.Boolean(), nullable=True),
    sa.Column('serves_non_veg', sa.Boolean(), nullable=True),
    sa.Column('nightlife', sa.Boolean(), nullable=True),
    sa.Column('city_view', sa.Boolean(), nullable=True),
    sa.Column('brunch', sa.Boolean(), nullable=True),
    sa.Column('sunday_roast', sa.Boolean(), nullable=True),
    sa.Column('gastro_Pub', sa.Boolean(), nullable=True),
    sa.Column('beer', sa.Boolean(), nullable=True),
    sa.Column('outdoor_seating', sa.Boolean(), nullable=True),
    sa.Column('takeaway', sa.Boolean(), nullable=True),
    sa.Column('alcohol', sa.Boolean(), nullable=True),
    sa.Column('seating', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('restaurant_id')
    )
    op.create_index(op.f('ix_restaurant_amenity_id'), 'restaurant_amenity', ['id'], unique=False)
    op.create_table('restaurant_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('image_type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_restaurant_image_id'), 'restaurant_image', ['id'], unique=False)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('breakfast', sa.Boolean(), nullable=True),
    sa.Column('lunch', sa.Boolean(), nullable=True),
    sa.Column('dinner', sa.Boolean(), nullable=True),
    sa.Column('cafe', sa.Boolean(), nullable=True),
    sa.Column('lounge', sa.Boolean(), nullable=True),
    sa.Column('family', sa.Boolean(), nullable=True),
    sa.Column('bars', sa.Boolean(), nullable=True),
    sa.Column('nightlife', sa.Boolean(), nullable=True),
    sa.Column('street_stalls', sa.Boolean(), nullable=True),
    sa.Column('pocket_friendly', sa.Boolean(), nullable=True),
    sa.Column('diet', sa.Boolean(), nullable=True),
    sa.Column('luxury', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('restaurant_id')
    )
    op.create_index(op.f('ix_tag_id'), 'tag', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_id'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_restaurant_image_id'), table_name='restaurant_image')
    op.drop_table('restaurant_image')
    op.drop_index(op.f('ix_restaurant_amenity_id'), table_name='restaurant_amenity')
    op.drop_table('restaurant_amenity')
    op.drop_index(op.f('ix_association_id'), table_name='association')
    op.drop_table('association')
    op.drop_index(op.f('ix_restaurant_id'), table_name='restaurant')
    op.drop_table('restaurant')
    op.drop_index(op.f('ix_dish_id'), table_name='dish')
    op.drop_table('dish')
    op.drop_index(op.f('ix_cuisine_id'), table_name='cuisine')
    op.drop_table('cuisine')
    op.drop_index(op.f('ix_collection_id'), table_name='collection')
    op.drop_table('collection')
    # ### end Alembic commands ###
