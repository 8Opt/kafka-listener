import cv2
import numpy as np
from ultralytics import YOLO
from kafka import KafkaConsumer, KafkaProducer

VIDEO_STREAM = "VIDEO_STREAM"

# TODO: Add ultralytics YOLO for detection
model = YOLO("yolov8n.pt")
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"]
)

def normalize_result(result: dict):
    return {
        "boxes": result["boxes"].xyxy.tolist(),
        "classes": result["boxes"].cls.tolist(),
        "scores": result["boxes"].conf.tolist()
    }


def send_result(topic: str, result: dict):
    producer.send(topic=topic, value=result)
    producer.flush()

def main(
    topic: str = VIDEO_STREAM,
    bootstrap_servers: list[str] = ["localhost:9092"]
):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers
    )
    for msg in consumer:
        frame = np.frombuffer(msg.value, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        results = model(frame)
        send_result = {
            "frame": frame.tolist(),
            "results": normalize_result(results)
        }
        send_result("DETECTED", send_result)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
    