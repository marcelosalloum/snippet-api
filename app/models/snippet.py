from app import db, ma
from datetime import datetime, timedelta
from marshmallow import EXCLUDE
from werkzeug.security import generate_password_hash, check_password_hash


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    snippet = db.Column(db.String(1000000))
    expires = db.Column(db.DateTime)
    password_hash = db.Column(db.String(128))

    # PASSWORD
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Snippet:{self.id} {self.name}>'

class SnippetScheme(ma.ModelSchema):
    class Meta:
        model = Snippet
        fields = ('id', 'name', 'snippet', 'expires', '_links')
        unknown = EXCLUDE

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("api.get_snippet", id="<id>")}
    )
