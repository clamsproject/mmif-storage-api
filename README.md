# MMIF Storage API

Code to interact with a set of MMIF files via a FastAPI web service or a Flask web server. It is built upon the Python interface to MMIF files at [https://github.com/clamsproject/mmif-storage](https://github.com/clamsproject/mmif-storage), see the README file in that repository for a short description of what a MMIF Storage directory looks like.


### Requirements and installation

This requires Python version 3.12 or higher. Installation is a simple pip-install:

```bash
pip install mmif-storage-api
```

The examples below assume you have a MMIF storage directory conveniently laying around. If you do not, you can create an example directory with a script from the `mmif-storage` package:

```bash
create-storage-example -d DIRECTORY
```


### Web API

To start the FastAPI web service:

```bash
start_api --dir DIRECTORY --host HOSTNAME --port PORT
```

All options are optional, the default directory is your current working directory and the default host and port are `0.0.0.0` and `8000`. You get erratic behavior including perhaps some server errors if you start the API from a directory that is not a MMIF Storage directory or when the argument that you hand in is not a MMIF Storage directory. 

Once started, the root of the API is available at [http://127.0.0.1:8000](http://127.0.0.1:8000). You can also load the page with all available routes at [http://127.0.0.1:8000/routes](http://127.0.0.1:8000/routes) and access the Swagger UI interface at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

See the [API examples document](https://github.com/clamsproject/mmif-storage/blob/v0.2.0.rc3/docs/api-examples.md) for example API calls.


### Web Browser

To start the MMIF Storage browser do:

```bash
start_www --dir DIRECTORY --host HOSTNAME --port PORT
```

The defaults are the same except that the default port is `5000`. As with the web service API, expect weird behavior if you use a directory that is not a MMIF Storage directory.

With the default settings, point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).


### Containerization

This requires access to the source code and Docker or Podman to build the image:

```bash
docker build -f Containerfile -t mmif-storage-api .
```

You probably want to add a version number and use something like `-t mmif-storage-api:0.1.0` to make the version explicit.

Starting the container:

```bash
docker run --rm -d -v DIRECTORY:/data -p 8000:8000 mmif-storage-api
```

The value for `DIRECTORY` has to be an absolute path, the example below uses the example storage and the `$PWD` shell environment variable:

```bash
create-storage-example -d tmp-storage
docker run --rm -d -v $PWD/data/tmp-storage:/data -p 8000:8000 mmif-storage-api
```

It is the responsibilty of the developer to use the correct local storage directory so it can be used in the container. Also, the developer may have to replace the first port in the port mapping depending on local circumstances.
