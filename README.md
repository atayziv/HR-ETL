# ETL Service

## How do I get set up?

### Install Python and Poetry

You can download the Python installer from the Python site's [downloads page](https://www.python.org/downloads/).

Poetry is a Python packaging and dependency management tool. To install it, please follow the instructions
in [Poetry's documentation](https://python-poetry.org/docs/#installation). It is strongly recommended using the `curl`
installing method.

By default, poetry creates all its virtual environments in a fixed dedicated directory on the local computer. It is
recommended to change this behavior, and make poetry create a virtual environment for each project in its root directory
in a directory named `.venv`. this is done with the following command (needed to be run only once after poetry's
installation):

```sh
poetry config virtualenvs.in-project true
```

### Clone this repository

Go to the (https://github.com/atayziv/HR-ETL.git) in github, click on the Clone
button in the top right corner, and copy the `git clone` command to clone this repository wherever you want.

After the cloning is done, enter the app's root folder. You could use:

```sh
cd HR-ETL
```

### Configure local environment variables

- To run this app locally, _before_ starting the app, you should configure the environment variables detailed in
  the `Environment Variables` section. Check your IDE's documentation to find how to configure it.
- In VSCode, it is recommended using a settings file placed at the app's root folder in `.vscode/settings.json`. There,
  setting environment variables per terminal is possible using the `"terminal.integrated.env.osx"` key, with a key-value
  JSON object as a value (assuming macOS is used, as `osx` stands for it).

### Install dependencies

Run the following command (and all poetry's commands) in the app's root folder:

```sh
poetry install
```

- It creates a virtual environment with all the packages detailed in the `pyproject.toml` file, in the dependencies
  sections.
- After that, all the commands that depends on the installed packages should be run from inside this virtual
  environment. To do that, simply run `poetry shell`, and make sure the virtual environment's directory name is written
  in the beginning of the terminal command.
- For ease of use, it is recommended to configure your IDE to automatically use this virtual environment.
- In VSCode, this can be done by adding the following setting (assuming the virtual environment is created in the app's
  root directory): `"python.defaultInterpreterPath": "./.venv/bin/python"`.

### Start application in development mode

The following command runs the app in the development mode (don't forget to run it in the virtual environment):

```sh
python hr_etl
```

After that, the server will be available on port 8000 of the local machine.

### Run tests

The following command runs all the app's tests, linters and security checks (don't forget to run it in the virtual
environment):

```sh
tox
```

## Project's structure explained

By alphabetical order, for convenience.

### `hr_etl`

Contains all the source code files, written in Python files (`*.py`).

#### `data_models`

- Contains the shape definitions (=interfaces) of the objects used in the app.
- All the models should extend the `SharedBaseModel` class.
- When using this project as a boilerplate, you should replace the `example` models with yours, and you can add more
  models as you wish.

#### `clients`

- Contains all the accesses to external services and data needed for the services.
- When using this project as a boilerplate, you should replace the `example` client with yours, and you can add more
  clients as you wish.

#### `services`

- Contains all the logic needed for the routers.
- Each service should never access external services and data. These accesses should be placed in a matching client,
  from the `clients` folder.
- When using this project as a boilerplate, you should replace the `example` service with yours, and you can add more
  services as you wish.

#### Files in `hr_etl`'s root

- `__main__.py`: The entry point of the app when it is run locally for development purposes.
- `config.yaml`: The app's main configuration file.
- `constants.py`: The app's main constant settings.
- `containers.py`: All the dependencies that should be injected to the app.

### `tests`

Contains all the tests code files, written in Python files (`*.py`), with the pytest framework. For more information,
please check [pytest's documentation](https://docs.pytest.org/).

#### `test_data`

Contains all the files needed for the tests.

#### `unit`

Contains all the unit tests, arranged in folders corresponding to the source code's hierarchy.

### `README.md`

This file :)

### `poetry.lock` + `pyproject.toml`

Configuration files of the project with Poetry.

`pyproject.toml` contains general info about the project,the dependencies of the project and more tools' configurations.

`poetry.lock` is auto-generated and should be committed. It should not be modified manually.

### Assumes

1. The input json file will be by the path to json file given into config.yaml file.
2. If got the same employee_id , means its the same person in the list twice
3. We don't want to insert emplyess with 'Unkown' depatrment to our DB.
4. "Concatenate `first_name` and `last_name` into a new field called `full_name`" :
   means NEW field , NOT INSTEAD.
5. Same last comment for 'age'.
