import json
from threading import Thread
from simulation import simulation
from flask import Flask, request, send_from_directory, render_template
from uuid import uuid4

from config import Config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/simulation', methods=('POST',))
def run_simulation():
    data = request.data
    config = Config.from_json(data)
    uuid = uuid4()

    thread = Thread(target=simulation, args=(config, uuid), daemon=True)
    thread.start()
    return json.dumps({"simulationId": str(uuid)})


@app.route('/simulation', methods=('GET',))
def simulation_get_results():
    uuid = request.args.get('simulationId')
    return_type = request.args.get('type')
    filepath = f'{uuid}.{return_type}'
    return send_from_directory(directory='plots', path=filepath, as_attachment=True)


app.run('146.59.12.7', 8080)
