from app import db, ma
from datetime import datetime, timedelta
from marshmallow import EXCLUDE


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    snippet = db.Column(db.String(1000000), index=True, unique=True)
    expires = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Snippet:{self.id} {self.name}>'

class SnippetScheme(ma.ModelSchema):
    class Meta:
        model = Snippet
        fields = ('id', 'name', 'snippet', 'expires')
        unknown = EXCLUDE

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("api.get_user", id="<id>")}
    )

# - POST request to create the snippet: 'name', 'snippet', 'expires'
#       - The request to store the snippet should be replied to with a response that 
#       includes the URL where the snippet can be read.
# - GET
#       - Snippets expiry should be extended when they are accessed.
