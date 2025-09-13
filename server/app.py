from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define the existing models array
existing_models = ['Beetle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    """Default route that returns a welcome message"""
    return "Welcome to Flatiron Cars"

@app.route('/<model>')
def model_route(model):
    """
    Route for specific car models
    Checks if the model exists in our fleet and returns appropriate message
    """
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(debug=True)
