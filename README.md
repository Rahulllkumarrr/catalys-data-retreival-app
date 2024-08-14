# catalys-data-retreival-app (Flask Data Retrieval and Processing)

## Overview

This project simulates a simplified version of a data retrieval and processing system. The application is built using Flask and provides API endpoints for fetching, processing, and retrieving data.

## Endpoints

1. **Data Retrieval**:

    - **Endpoint**: `/fetch-data`
    - Simulates fetching data from an external service using mock data.

2. **Data Retrieval**:
    - **Endpoint**: `/get-processed-data`
    - Returns the processed data stored in memory.

## Prerequisites

-   Python 3.11+

## Steps to Setup and Run Flask App

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Rahulllkumarrr/catalys-data-retreival-app.git
    ```

2. **Set Up a Virtual Environment**

    ```bash
    cd catalys-data-retreival-app
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **On Windows**

        ```bash
        venv\Scripts\activate
        ```

    - **On Linux/MacOS**

        ```bash
        source venv/bin/activate
        ```

4. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask App**

    ```bash
    flask run
    ```
