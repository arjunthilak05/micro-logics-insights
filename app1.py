from flask import Flask, request, jsonify, render_template
import requests
import json

# Configuration
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "3bd1ead8-3c39-4415-b564-9948b440f14f"
FLOW_ID = "90bcf4a6-2172-4f59-89d3-71ce066524c6"
APPLICATION_TOKEN = "AstraCS:txkIACSbZmdhZZIMupCZOdBh:5ea8ad8a92a152769e0ce5b52e0efe61966dd6f5a0333904e213df30e9a7317c"

app = Flask(__name__)

def run_flow(message: str):
    """Run the LangFlow API and return the processed results"""
    # The complete API endpoint URL for this flow
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    
    # Request payload configuration
    payload = {
        "input_value": message,  # The input value to be processed by the flow
        "output_type": "chat",   # Specifies the expected output format
        "input_type": "chat"     # Specifies the input format
    }
    
    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {APPLICATION_TOKEN}"  # Authentication token
    }
    
    try:
        # Send API request
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        result = response.json()     # Process the response
        
        # Extract text result if possible
        text_response = "Sorry, I couldn't process your request."
        
        outputs = result.get("outputs", [])
        if outputs and len(outputs) > 0:
            first_output = outputs[0].get("outputs", [])
            if first_output and len(first_output) > 0:
                text_response = first_output[0].get("results", {}).get("message", {}).get("text", "No results found")
        
        return {"success": True, "response": text_response}
    
    except requests.exceptions.RequestException as e:
        app.logger.error(f"HTTP Request failed: {e}")
        return {"success": False, "error": f"Request error: {str(e)}"}
    except json.JSONDecodeError as e:
        app.logger.error(f"Error decoding JSON response: {e}")
        return {"success": False, "error": "Invalid response from API"}
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process chat messages and return AI response"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({"success": False, "error": "No message provided"}), 400
        
        # Process the message through Langflow
        result = run_flow(message)
        
        return jsonify(result)
    
    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {e}")
        return jsonify({"success": False, "error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)