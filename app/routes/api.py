"""Routes pertaining to the built-in API"""
from app import app
from app.util import wiki_api
from flask import request, jsonify

@app.route('/api/wiki_topic')
def random():
    number_of_sentences = int(request.args.get('rows', 5))
    def get_page():
        try:
            return wiki_api.read_random_from_topic()
        except:
            return get_page()
        
    content = [get_page() for x in xrange(0, number_of_sentences)]
    return jsonify({'results': content})
