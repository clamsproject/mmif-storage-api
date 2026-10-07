"""

This init file does a few different kind of things:

- Import some names to the package toplevel.
- Create the flask app and register the single blueprint.
- Provide entry points for the project scripts that start the FastAPI and Flask
  servers.

"""


import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

from pydantic import BaseModel
from flask import Flask
import uvicorn

from mmif_storage import config
from mmif_storage.storage import StoragePath


load_dotenv()


# Default host name and ports
HOSTNAME = '0.0.0.0'
FLASK_PORT = 5000
FASTAPI_PORT = 8000


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from mmif_storage_api.www import bp as bp_www
    app.register_blueprint(bp_www)


def parse_arguments(api=True) -> argparse.Namespace:
    port = FASTAPI_PORT if api else FLASK_PORT
    host = HOSTNAME
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--dir', type=str, default=os.getcwd(),
        help="MMIF Storage directory, default is the current directory")
    argparser.add_argument(
        '--host',type=str, default=host, help=f'host name, default is {host}')
    argparser.add_argument(
        '--port', type=int, default=port, help=f"port number, default is {port}")
    args = argparser.parse_args(sys.argv[1:])
    if not Path(args.dir).is_dir():
        exit(f'Directory "{args.dir}" does not exist, exiting...')
    return args


def start_api():
    from mmif_storage_api.api import app as api_app
    args = parse_arguments(api=True)
    config.MMIF_STORAGE_DIR = args.dir
    uvicorn.run("mmif_storage_api.api:app", host=args.host, port=args.port)


def start_www():
    args = parse_arguments(api=False)
    config.MMIF_STORAGE_DIR = args.dir
    # TODO: should replace this with gunicorn
    create_app().run(host=args.host, port=args.port)
