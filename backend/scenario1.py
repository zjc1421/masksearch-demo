from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/topk_search', methods=['POST'])
def topk_search():
    data = request.json
    k = data.get('k')
    threshold = data.get('threshold')
    # return first k image_ids as example
    image_ids = list(range(1, int(k) + 1))
    return jsonify({'k': k, 'threshold': threshold, 'image_ids': image_ids})

@app.route('/api/augment', methods=['GET'])
def augment():
    # Dummy implementation
    return jsonify({'result': 2})

@app.route('/images/<image_id>')
def get_image(image_id):
    # Serve an image from the topk_results directory
    return send_from_directory('topk_results', f'image_{image_id}.jpg')

if __name__ == '__main__':
    app.run(debug=True)
