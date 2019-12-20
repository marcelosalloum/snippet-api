from app import db
from app.api import bp
from app.api.errors import bad_request, error_response
from app.models import Snippet, SnippetScheme
from datetime import datetime
from dateutil.parser import parse
from flask import abort, g, jsonify, request, make_response, url_for
from marshmallow import fields


@bp.route('/snippets/<int:id>', methods=['GET'])
def get_snippet(id):
    snippet = Snippet.query.get_or_404(id)

    now = datetime.utcnow()
    if snippet.expires < now:
        return error_response(status_code=403, message="This resource has expired and is no longer available")

    snippet_schema = SnippetScheme()
    return jsonify(snippet_schema.dump(snippet))


@bp.route('/snippets', methods=['POST'])
def create_snippet():
    data = request.get_json() or {}

    # Validation
    if 'name' not in data or 'snippet' not in data or 'expires' not in data:
        return bad_request("The fields 'name', 'snippet' and 'expires' are mandatory!")

    try:
        parse(data['expires'])
    except:
        return bad_request("The 'expires' field couldn't be parsed to a valid datetime. To prevent this, make sure to adopt a widely known datetime format, like ISO 8601 (YYYY-MM-DDTHH:MM:SS.mmmmmm)")

    # Object creation
    snippet_scheme = SnippetScheme()
    snippet = Snippet()
    snippet_scheme.load(data, instance=snippet, partial=True)
    db.session.add(snippet)
    db.session.commit()

    # Response
    response = jsonify(snippet_scheme.dump(snippet))
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_snippet', id=snippet.id)
    return response


# - OK: POST request to create the snippet: 'name', 'snippet', 'expires'
#       - OK: The request to store the snippet should be replied to with a response that
#       includes the URL where the snippet can be read.
# - OK: GET
#       - OK: Resources would be inaccessible after expired
#       - Snippets expiry should be extended when they are accessed.
