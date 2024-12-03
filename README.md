# Winter Supplement Rules Engine

This repository contains the solution for implementing a rules engine to determine eligibility and calculate the Winter Supplement benefit.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Setting Up the Environment](#setting-up-the-environment)
4. [Running and Testing the Rules Engine](#running-and-testing-the-rules-engine)
   - [Option 1: Using the Web App MQTT Topic ID](#option-1-using-the-web-app-mqtt-topic-id)
   - [Option 2: Running Locally Without the Web App](#option-2-running-locally-without-the-web-app)
5. [General Testing Instructions](#general-testing-instructions)
6. [Project Structure](#project-structure)

---

## Overview

The Winter Supplement Rules Engine assesses a client’s eligibility for the Winter Supplement benefit and calculates the appropriate amount based on predefined criteria. This project utilizes an event-driven architecture and MQTT for communication.

---

## Prerequisites

- Python 3.8+

---

## Setting Up the Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rezabanitaba/REQ117214-ISL-21R
   cd REQ117214-ISL-21R
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Edit the `.env` file**:
   - Open the `.env` file located in the project root directory.
   - Add the MQTT topic ID:
     ```plaintext
     MQTT_TOPIC_ID=<topic-id>
     ```

   ⚠️ If the web app works as expected, use its dynamically generated topic ID. For local testing, use any arbitrary string.

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running and Testing the Rules Engine

You can test the rules engine using one of the two options below:

### Option 1: Using the Web App MQTT Topic ID

1. **Run the rules engine**:
   ```bash
   python main.py
   ```

2. **Locate the MQTT topic ID**:
   - Open the web app and note the generated MQTT topic ID (e.g., `e78ffe1b-debd-4401-a886-b984a0c4b2d0`).

3. **Update the `.env` file**:
   - Open `.env` and update the topic ID:
     ```plaintext
     MQTT_TOPIC_ID=e78ffe1b-debd-4401-a886-b984a0c4b2d0
     ```

4. **Restart the rules engine**:
   ```bash
   python main.py
   ```

5. **Test integration**:
   - Use the web app to send input data to the MQTT topic. The rules engine will process the data and publish results to the output topic.

---

### Option 2: Running Locally Without the Web App

If the web app is unavailable or you want to simulate its behavior locally:

1. **Run the rules engine**:
   ```bash
   python main.py
   ```

2. **Publish mock data**:
   - Open another terminal and run:
     ```bash
     python publish.py
     ```
   - This publishes example data to the MQTT topic:
     ```json
     {
         "id": "test123456",
         "numberOfChildren": 3,
         "familyComposition": "single",
         "familyUnitInPayForDecember": true
     }
     ```

3. **View results**:
   - Check the logs in the `main.py` terminal or monitor the output topic using [MQTT Explorer](https://mqtt-explorer.com/).

---

## General Testing Instructions

To run all unit tests for the project:

1. Navigate to the `tests` directory:
   ```bash
   cd tests
   ```

2. Run the tests using `pytest`:
   ```bash
   pytest --cache-clear
   ```

This will execute all tests and display the results.

---

## Project Structure

```plaintext
project/
├── rules_engine/
│   ├── __init__.py    
│   ├── engine.py         # Rules engine implementation
├── tests/
│   ├── __init__.py
│   ├── test_engine.py    # Unit tests for rules engine
│   ├── test_mqtt.py      # Unit tests for MQTT
├── main.py               # Main file for the MQTT rules engine
├── publish.py            # Script for publishing mock data to MQTT
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables
├── README.md             
```
