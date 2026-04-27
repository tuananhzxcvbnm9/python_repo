from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models.user import User
from app.models.report import Report
from app.core.security import hash_password

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    db=SessionLocal()
    try:
        if not db.query(User).filter(User.email=='admin@example.com').first():
            db.add(User(email='admin@example.com', hashed_password=hash_password('admin123'), role='admin'))
        if not db.query(Report).first():
            db.add(Report(name='Report Sample', status='active'))
        db.commit()
        print('Seed complete for app-10')
    finally:
        db.close()
