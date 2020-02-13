import os
from seMgmtApp import create_app
from seMgmtApp.config import Config

app = create_app()

if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"))