import cv2
import numpy as np
from ultralytics import YOLO
from kafka import KafkaConsumer, KafkaProducer

VIDEO_STREAM = "VIDEO_STREAM"

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
    print("Listening to topic: ", topic)
    for msg in consumer:
        frame = np.frombuffer(msg.value, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        if frame is not None:
            # Run YOLO11 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True)
            print(results)
            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLO11 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else: 
            print("Frame is None")

if __name__ == "__main__":
    main()
    