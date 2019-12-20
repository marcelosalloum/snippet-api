from app import db, ma
from datetime import datetime, timedelta
from marshmallow import EXCLUDE


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    snippet = db.Column(db.String(1000000))
    expires = db.Column(db.DateTime)

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
