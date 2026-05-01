from app.db.database import Base, engine
from app.db import models
# 임시
Base.metadata.create_all(bind=engine)