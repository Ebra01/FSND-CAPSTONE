import os
from flaskr import create_app

app = create_app()

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=port)
