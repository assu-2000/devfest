import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # check for IAP email header
    iap_email = request.headers.get('X-Goog-Authenticated-User-Email')

    if iap_email:
        user_email = iap_email.replace('accounts.google.com:', '')
    else:
        # default user
        user_email = 'guest@devfest-kinshasa.com'

    return render_template('index.html', user_email=user_email)


if __name__ == '__main__':
    debug_mode = os.environ.get('GAE_ENV', 'local') == 'local'
    port = int(os.environ.get('PORT', 8080))
    host = '0.0.0.0' if os.environ.get('PORT') else '127.0.0.1'
    app.run(host=host, port=port, debug=debug_mode)