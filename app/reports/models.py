from app import db


class ReportBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Daily(ReportBase):
    __tablename__ = 'reports_daily'

    title = db.Column(db.String(128),  nullable=False)

    def __repr__(self):
        return '<Daily %r>' % (self.title)