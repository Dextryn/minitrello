from database import SessionLocal
from crud import update_user, get_user_by_id

def main():
    db = SessionLocal()

    # BEFORE
    user = get_user_by_id(db, 1)
    print("Before:", user.email)

    # UPDATE
    update_user(
        db=db,
        user_id=1,
        email="newemail@example.com"
    )

    # AFTER
    user = get_user_by_id(db, 1)
    print("After:", user.email)

    db.close()

if __name__ == "__main__":
    main()
