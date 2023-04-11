from pure_flask import app

if __name__ == "__main__":
    app.run()

# run with
# gunicorn --bind 0.0.0.0:62000 app_gunicorn:app

