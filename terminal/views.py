import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Build the absolute path to contents.py based on the current file's location
CONTENTS_FILE_PATH = os.path.join(os.path.dirname(__file__), 'contents.py')

@csrf_exempt
def execute_contents_file(request):
    if request.method == 'POST':
        print("Checking path:", CONTENTS_FILE_PATH)  # Debugging line

        if not os.path.exists(CONTENTS_FILE_PATH):
            return JsonResponse({"error": f"contents.py file not found on the server at {CONTENTS_FILE_PATH}"}, status=404)

        try:
            # Read the contents of contents.py
            with open(CONTENTS_FILE_PATH, 'r') as file:
                script_content = file.read()

            # Send the content as JSON to Flask for execution
            response = requests.post('http://localhost:5000/execute_script', json={"script_content": script_content})
            return JsonResponse(response.json(), status=response.status_code)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
