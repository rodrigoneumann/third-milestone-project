import os
from semgmtapp import create_app
from semgmtapp.config import Config

app = create_app()

if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"))