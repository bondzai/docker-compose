import io
import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from models_pb2 import SensorData

app = FastAPI()

# Allow CORS for localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_sensor_data(size):
    sensor_data = SensorData()
    for _ in range(size):
        data_point = sensor_data.data_points.add()
        data_point.sensor_id = random.randint(1, 10)
        data_point.temperature = round(random.uniform(20.0, 30.0), 2)
        data_point.humidity = round(random.uniform(40.0, 60.0), 2)
    return sensor_data

@app.get("/json/")
def json_endpoint():
    sensor_data = generate_sensor_data(size=20000)
    sensor_data_dict = {
        "data_points": [
            {
                "sensor_id": dp.sensor_id,
                "temperature": dp.temperature,
                "humidity": dp.humidity,
            }
            for dp in sensor_data.data_points
        ]
    }
    return JSONResponse(content=sensor_data_dict, media_type="application/json")

@app.get("/protobuf/")
def protobuf_endpoint():
    sensor_data = generate_sensor_data(size=20000)
    serialized_data = sensor_data.SerializeToString()
    return StreamingResponse(io.BytesIO(serialized_data), media_type="application/protobuf")
