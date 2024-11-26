from app import create_app, db
from app.models import User, Post, Message, Notification, Task
import sqlalchemy as sa
import sqlalchemy.orm as so

app = create_app()  # This defines the 'app' variable that Flask expects.

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post,
            'Message': Message, 'Notification': Notification, 'Task': Task}
