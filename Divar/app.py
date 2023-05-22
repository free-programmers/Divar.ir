from DivarCore import app
from DivarConfig import APP_RUNNER_CONFIG


@app.route("/")
def index():
    return "Hello world"

print("hello")
if __name__ == "__main__":
    app.run(**APP_RUNNER_CONFIG)
