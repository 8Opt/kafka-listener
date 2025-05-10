# kafka-listener

The Kafka Listener is a component of the Kafka Learning Project that utilizes AI models to process data from Kafka topics. It performs object detection tasks and writes the results to new Kafka topics for further analysis.

## Overview

The Kafka Listener is designed to:

- Consume messages from specific Kafka topics.
- Apply AI models for object detection (e.g., human, car).
- Write detection results to designated Kafka topics.

## Features

- **AI Integration**: Seamlessly integrates AI models for real-time data processing.
- **Scalability**: Supports multiple models and topics for diverse detection tasks.
- **Result Publishing**: Efficiently writes detection results to Kafka topics.

## Getting Started

### Prerequisites

- Apache Kafka must be installed and running.
- Ensure the Kafka cluster is properly configured and accessible.
- AI models must be trained and available for integration.


### Configuration

- Configure the listener settings in `config.json`:
  - Specify the Kafka broker addresses.
  - Set the topics to consume and publish results to.
  - Integrate AI models for detection tasks.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.