import os
from seMgmtApp import app

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "127.0.0.1"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)