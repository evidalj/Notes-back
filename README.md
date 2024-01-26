
## Requirements
- Python 3.9.13

If you use PayCharm:
- Open the project
  - File/Open
  - When the IDE request the configuration of the virtual environment, select Python 3.9.13 version.
  - If you go to the integrated terminal of the IDE, the venv will be activated automatically.
If you don't use PayCharm:
  - Go to root project in a console.
  - execute the command `python -m venv project-env`.
  - activate the venv `project-env/Scripts/activate`. If you use Unix or macOS, execute `source project-env/Scripts/activate`.

### When you have configured the venv
execute `pip install "fastapi[all]" uvicorn[standard] sqlalchemy` to install the dependencies.
execute `uvicorn main:app` to raise local server

To test the API go to URL http://localhost:8000

Also, you can go to URL http://localhost:8000/docs test the API