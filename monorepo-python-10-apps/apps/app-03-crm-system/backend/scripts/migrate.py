from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.models.deal import Deal

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    print('Migration complete for app-03')
