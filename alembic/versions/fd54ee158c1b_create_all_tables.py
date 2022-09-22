from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

revision = 'fd54ee158c1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column(
        'users',
        sa.Column('role', sa.Enum('teacher', 'student', name='role'), nullable=True)
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('courses',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=200), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)
    op.create_table('profiles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('bio', sa.Text(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('course_student',
                    sa.Column('student_id', sa.Integer(), nullable=False),
                    sa.Column('course_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
                    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('student_id', 'course_id')
                    )
    op.create_table('sections',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=200), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('course_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_sections_id'), 'sections', ['id'], unique=False)
    op.create_table('content_blocks',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=200), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
                    sa.Column('content', sa.Text(), nullable=True),
                    sa.Column('section_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.add_column(
        'content_blocks',
        sa.Column('type', sa.Enum('lesson', 'quiz', 'assignment', name='contenttype'), nullable=True)
    )
    op.create_index(op.f('ix_content_blocks_id'), 'content_blocks', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_content_blocks_id'), table_name='content_blocks')
    op.drop_table('content_blocks')
    op.drop_index(op.f('ix_sections_id'), table_name='sections')
    op.drop_table('sections')
    op.drop_table('course_student')
    op.drop_table('profiles')
    op.drop_index(op.f('ix_courses_id'), table_name='courses')
    op.drop_table('courses')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
