from DivarCore import app
from flask import render_template


@app.route("/", methods=["GET"])
def DivarStarterTemplate():
    """
    this view shows to that users that is first time visiting site and doesn't have any city;
    :return:
    """
    return render_template("DivarStarter/index.html")