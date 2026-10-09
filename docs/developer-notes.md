

## Developer Notes

As a developer you propably want to get the source code, copy the example configuration settings, and do an editable install:

```bash
git clone https://github.com/clamsproject/mmif-storage
cd mmif-storage
pip install -e .[dev]
```

Then you need to set up some environment variables for FastAPI and Flask. Copy `src/.env.sample` into `.env` and edit settings as needed. The most likely change is to `MMIF_STORAGE_DIR`, which now points to the small example storage directory that was created for the sake of the Docker example.

To check whether you can run the main module and see the paths in the storage:

```bash
cd src
python -m mmif_storage_api paths
```

```json
[
  "swt-detection/v8.6/d41d8cd98f00b204e9800998ecf8427e",
  "swt-detection/v8.6/d41d8cd98f00b204e9800998ecf8427e/smolvlm2-captioner/v1.0/d41d8cd98f00b204e9800998ecf8427e",
  "swt-detection/v8.6/d41d8cd98f00b204e9800998ecf8427e/smolvlm2-captioner/v1.0/d41d8cd98f00b204e9800998ecf8427e/spacy-wrapper/v2.3/5fe49d06725497b274b6eaaf0fe0c5d2"
]
```

With the local install you can also start the API with one of the following:

```bash
fastapi run mmif_storage/api.py
uvicorn mmif_storage.api:app
```

And to run the MMIF browser do:

```bash
flask run
```


### Building and installing

There is no pip-installable package on PyPI yet, but you can create a source archive and then install it. For building you run the following, which assumes that the Python build utility is installed:

```bash
python -m build
```

Then install anywhere by using the created archive:

```bash
pip install -r PATH_TO_ARCHIVE
```

<!--

TODO: the follopwing does not work anymore.

To run the MMIF browser in production:

```bash
gunicorn "mmif_storage:create_app()" -b 0.0.0.0:8001
```

The port number is used here because by default gunicorn runs on 8000, which may already be taken by the API. The browser then runs at [http://127.0.0.1:8001/www/](http://127.0.0.1:8001/www/).


Notes to self

To make the tests run at some point some changes were made to `mmif_storage.create_storage_example()`. The distribution package is now updated, but for development consider doing a local editable install of the package: `pip install -e ../mmif_storage`.

-->

