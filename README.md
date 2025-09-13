# Flask Car Routes Lab

A simple Flask web application that manages car model information for Flatiron Cars.

## Features

- **Welcome Route** (`/`) - Displays company welcome message
- **Model Route** (`/<model>`) - Checks if a car model exists in our fleet

## Available Car Models

- Beetle
- Crossroads  
- M2
- Panique

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Running the Application

```bash
python server/app.py
```

The app will be available at `http://localhost:5000`

## API Endpoints

### GET /
Returns welcome message for Flatiron Cars.

**Response:** `"Welcome to Flatiron Cars"`

### GET /\<model>
Check if a specific car model exists in our fleet.

**Examples:**
- `/Beetle` → `"Flatiron Beetle is in our fleet!"`
- `/Honda` → `"No models called Honda exists in our catalog"`

## Testing

Run the test suite:
```bash
pytest server/testing/app_test.py
```
## Technologies Used

- Flask 2.3.3
- Python 3.8
- pytest (for testing)