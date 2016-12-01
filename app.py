from bottle import Bottle, request
import sys


app = Bottle()


@app.route(['/hello', '/'])
def hello():
    return "Hello World!"


@app.route('/search', method='GET')
def search_request():
    log('search')
    log(dict(request.query))
    item_id = request.query.get('item_id')
    sku_id = request.query.get('sku_id')
    log('item_id:%s, sku_id:%s' % (item_id, sku_id))
    return "Hello World!"


@app.route(['/_ah/health', '/_ah/start'])
def _ah_health():
    return "ok"


def log(msg):
    sys.stdout.write(str(msg) + "\n")
    sys.stdout.flush()


if __name__ == '__main__':
    log('aaa,')
    # waiting request
    app.run(host='0.0.0.0', port=8080, debug=True)
    log('test')

