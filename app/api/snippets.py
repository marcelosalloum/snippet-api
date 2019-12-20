from app import db
from marshmallow import fields
from app.api import bp
from app.models import Snippet, SnippetScheme
from flask import abort, g, jsonify, request, make_response
from app.api.errors import bad_request, forbidden_error


@bp.route('/snippets/<int:id>', methods=['GET'])
def get_snippet(id):
    snippet = Snippet.query.get_or_404(id)
    snippet_schema = SnippetScheme()
    return jsonify(snippet_schema.dump(snippet))


# - POST request to create the snippet: 'name', 'snippet', 'expires'
#       - The request to store the snippet should be replied to with a response that 
#       includes the URL where the snippet can be read.
# - OK: GET
#       - Snippets expiry should be extended when they are accessed.
