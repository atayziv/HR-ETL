# Fast API Server #

This folder contains a template of a RESTful API service served on a web server. It uses a uvicorn server, written in
Python with the FastAPI framework.

## Environment Variables ##

* `FASTAPI_SERVER_ROOT_PATH` (optional. default: empty string): The prefix of the fastapi-server when it is hosted on a
  proxy, with first slash only (e.g. "/api"). If no proxy is used, set it with an empty string.

## How do I get set up? ##

### Install Python and Poetry ###

You can download the Python installer from the Python site's [downloads page](https://www.python.org/downloads/).

Poetry is a Python packaging and dependency management tool. To install it, please follow the instructions
in [Poetry's documentation](https://python-poetry.org/docs/#installation). It is strongly recommended using the `curl`
installing method.

For optimal results, make sure you install the following versions:

* **Python**: >=3.9.6, <3.10.0
* **Poetry**: >=1.4.2

By default, poetry creates all its virtual environments in a fixed dedicated directory on the local computer. It is
recommended to change this behavior, and make poetry create a virtual environment for each project in its root directory
in a directory named `.venv`. this is done with the following command (needed to be run only once after poetry's
installation):

```sh
poetry config virtualenvs.in-project true
```

In order for Poetry to be able to access the Artifactory, add the following environment variables:

* `POETRY_HTTP_BASIC_ARTI_USERNAME`: Your Artifactory username.
* `POETRY_HTTP_BASIC_ARTI_PASSWORD`: Your Artifactory API Key.

And configure poetry to trust the Artifactory's host by running this command:

```sh
poetry config certificates.arti.cert false
```

### Clone this repository ###

Go to the [Templates home page](https://bitbucket.org/originai/templates/src/master/) in bitbucket, click on the Clone
button in the top right corner, and copy the `git clone` command to clone this repository wherever you want.

After the cloning is done, enter the app's root folder. You could use:

```sh
cd fastapi-server
```

### Configure local environment variables ###

* To run this app locally, *before* starting the app, you should configure the environment variables detailed in
  the `Environment Variables` section. Check your IDE's documentation to find how to configure it.
* In VSCode, it is recommended using a settings file placed at the app's root folder in `.vscode/settings.json`. There,
  setting environment variables per terminal is possible using the `"terminal.integrated.env.osx"` key, with a key-value
  JSON object as a value (assuming macOS is used, as `osx` stands for it).

### Install dependencies ###

Run the following command (and all poetry's commands) in the app's root folder:

```sh
poetry install
```

* It creates a virtual environment with all the packages detailed in the `pyproject.toml` file, in the dependencies
  sections.
* After that, all the commands that depends on the installed packages should be run from inside this virtual
  environment. To do that, simply run `poetry shell`, and make sure the virtual environment's directory name is written
  in the beginning of the terminal command.
* For ease of use, it is recommended to configure your IDE to automatically use this virtual environment.
* In VSCode, this can be done by adding the following setting (assuming the virtual environment is created in the app's
  root directory): `"python.defaultInterpreterPath": "./.venv/bin/python"`.

### Start application in development mode ###

The following command runs the app in the development mode (don't forget to run it in the virtual environment):

```sh
python fastapi_server
```

After that, the server will be available on port 8000 of the local machine.

### Run tests ###

The following command runs all the app's tests, linters and security checks (don't forget to run it in the virtual
environment):

```sh
tox
```

For the integration tests it uses `docker` and `docker-compose`, so those should be installed in order for the tests to
pass. You can download it from the Docker site's [install page](https://docs.docker.com/engine/install/).

The installer of docker-compose is bundled in the Docker installer.

For optimal results, make sure you install the following versions:

* **Docker**: >=20.10.5
* **docker-compose**: >=1.28.5, <2.0.0

### Start application in production mode ###

In production, the application runs on a docker container. You should have docker installed to run these commands.

```sh
docker build . -t fastapi-server \
  --build-arg ARTIFACTORY_PROXY=<Optional. Default is "jf.originai.co"> \
  --build-arg ECO_ARTIFACTORY_PROXY=<Optional. Default is "jf.originai.co/docker"> \
  --build-arg ARTI_USERNAME=<Your Artifactory username> \
  --build-arg ARTI_PASSWORD=<Your Artifactory password or API key> \
  --build-arg ARTI_PROTOCOL=<Optional. Default is "https"> \
  --build-arg ARTI_PYPI_REPO=<Optional. Default is "jf.originai.co/artifactory/api/pypi/pypi/simple">
```

```sh
docker run -p 5000:5000 fastapi-server
```

After that, the server will be available on port 5000 of the local machine.

### What to do to use this template for a new project ###

1. Copy fastapi-server content to your new repository folder
2. Change the name of the folder "fastapi_server" with your module name (instead of whitespaces use underscores (`_`).
3. Replace all `fastapi-server` in the project with your module name (instead of whitespaces use hyphens (`-`))
4. Replace all `fastapi_server` in the project with your module name (instead of whitespaces use underscores (`_`))
5. Change the `ExampleRoute`, `ExamplesService`, `ExamplesClient`, `ExampleRequest` & `ExampleResponse` classes to mach
   your case.

## Project's structure explained ##

By alphabetical order, for convenience.

### `fastapi_server` ###

Contains all the source code files, written in Python files (`*.py`).

#### `api` ####

* Contains all the server's services.
* `server.py` is the main file that spin's up the FastAPI instance and calls all the routers.

##### `routers` ######

* Contains all the server's routers.
* Each router should always contain as few logic as possible. All the routers specific logic should be placed in a
  matching service, from the `services` folder.
* When using this project as a boilerplate, you should replace the `example` router with yours, and you can add more
  routers as you wish.

##### `static` ######

* Contains the static web files (JavaScripts and CSS) needed to serve the swagger docs.
* These files should not be modified manually.

#### `data_models` ####

* Contains the shape definitions (=interfaces) of the objects used in the app.
* All the models should extend the `SharedBaseModel` class.
* When using this project as a boilerplate, you should replace the `example` models with yours, and you can add more
  models as you wish.

#### `clients` ####

* Contains all the accesses to external services and data needed for the services.
* When using this project as a boilerplate, you should replace the `example` client with yours, and you can add more
  clients as you wish.

#### `services` ####

* Contains all the logic needed for the routers.
* Each service should never access external services and data. These accesses should be placed in a matching client,
  from the `clients` folder.
* When using this project as a boilerplate, you should replace the `example` service with yours, and you can add more
  services as you wish.

#### Files in `fastapi_server`'s root ####

* `__main__.py`: The entry point of the app when it is run locally for development purposes.
* `config.yaml`: The app's main configuration file.
* `constants.py`: The app's main constant settings.
* `containers.py`: All the dependencies that should be injected to the app.
* `utils.py`: Some general utilities for the app. Please, avoid using this file for specific and single usage utilities.

### `tests` ###

Contains all the tests code files, written in Python files (`*.py`), with the pytest framework. For more information,
please check [pytest's documentation](https://docs.pytest.org/).

#### `integration` ####

Contains all the integration tests, which use a `docker-compose.yml` file to spin up the server, and test it.

#### `test_data` ####

Contains all the files needed for the tests.

#### `unit` ####

Contains all the unit tests, arranged in folders corresponding to the source code's hierarchy.

### `.coveragerc` ###

Configuration file of the `coverage` library. For more information, please
check [Coverage's documentation](https://coverage.readthedocs.io/en/coverage-5.5/config.html).

### `.dockerignore` + `Dockerfile` ###

Files used for deploying the app in production. For more details, please check
the `Start application in production mode` section of this page.

### `.pylintrc` ###

Configuration file of Pylint. For more information, please
check [Pylint's documentation](https://pylint.pycqa.org/en/latest/user_guide/options.html).

### `README.md` ###

This file :)

### `poetry.lock` + `pyproject.toml` ###

Configuration files of the project with Poetry.

`pyproject.toml` contains general info about the project,the dependencies of the project and more tools' configurations.

`poetry.lock` is auto-generated and should be committed. It should not be modified manually.

### `tox.ini` ###

Configuration file of Tox. For more information, please
check [Tox's documentation](https://tox.wiki/en/latest/config.html).
