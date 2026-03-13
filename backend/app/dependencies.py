from datetime import datetime
from MiniTrello.backend.app.models import User

def get_current_user():
    """Fake current user for testing purposes"""
    return User(
        user_id=21,
        email="maxsommerville22@gmail.com",
        first_name="Max",
        last_name="Sommerville",
        password_hash="password123",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )