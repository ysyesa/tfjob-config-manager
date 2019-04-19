from flask import Flask
from flask import request
from flask import jsonify
import subprocess
from ConfigManager import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    return jsonify("The ConfigurationListener is working.")


@app.route("/modify", methods=["POST"])
def modify():
    filename = "/app/out/" + request.form["filename"]
    tfjob_name = request.form["tfjob_name"]
    tfjob_master_replica = request.form["tfjob_master_replica"]
    tfjob_master_image = request.form["tfjob_master_image"]
    tfjob_worker_replica = request.form["tfjob_worker_replica"]
    tfjob_worker_image = request.form["tfjob_worker_image"]
    tfjob_ps_replica = request.form["tfjob_ps_replica"]
    tfjob_ps_image = request.form["tfjob_ps_image"]

    if filename is None or tfjob_name is None or tfjob_master_replica is None or tfjob_master_image is None or \
            tfjob_worker_replica is None or tfjob_worker_image is None or tfjob_ps_replica is None or \
            tfjob_ps_image is None:
        return jsonify("Please complete all arguments needed!")

    config_manager = ConfigManager(filename)
    config_manager.set_tfjob_name(tfjob_name)
    config_manager.set_tfjob_master_replica(tfjob_master_replica)
    config_manager.set_tfjob_master_image(tfjob_master_image)
    config_manager.set_tfjob_worker_replica(tfjob_worker_replica)
    config_manager.set_tfjob_worker_image(tfjob_worker_image)
    config_manager.set_tfjob_ps_replica(tfjob_ps_replica)
    config_manager.set_tfjob_ps_image(tfjob_ps_image)
    config_manager.generate_config_file()

    return jsonify("Configuration generated and applied.")
