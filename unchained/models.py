from app import db
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import exists


class UnchainedBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime,  default=db.func.current_timestamp())
    updated_at = Column(DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    @classmethod
    def exists(cls, key):
        _meta = getattr(cls, cls.__key_on__)
        return db.session.query(
            exists().where(_meta == key)).scalar()

    @classmethod
    def get(cls, key):
        if not cls.exists(key):
            raise DoesntExist()
        _params = {cls.__key_on__: key}
        return cls.query.filter_by(**_params).first()

    @classmethod
    def get_or_create(cls, obj, key):
        if cls.exists(key):
            return cls.get(key)
        _created = cls(**obj)
        db.session.add(_created)
        db.session.commit()
        return _created

    def __repr__(self):
        return '<%r %r>' % (self.__name__, getattr(self, self.__key_on__))
