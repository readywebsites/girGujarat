"""
TRAVEL FIRST HOLIDAYS — LOCAL FULL-STACK DEV SERVER & DRF API MOCK
Runs a lightweight development server on http://127.0.0.1:8000:
1. Serves static frontend files (HTML, CSS, JS, Assets).
2. Simulates Django REST Framework (DRF) endpoints:
   - POST /api/bookings/
   - POST /api/inquiries/
3. Accurately simulates DRF HTTP 201 Created responses and HTTP 400 validation error payloads.
"""

import http.server
import socketserver
import json
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get('PORT', 8000))
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

booking_counter = 100
inquiry_counter = 200

class DevAndDRFHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept, X-CSRFToken')
        self.end_headers()

    def do_POST(self):
        global booking_counter, inquiry_counter

        # Endpoint Routing
        if self.path in ['/api/bookings', '/api/bookings/']:
            self.handle_booking()
        elif self.path in ['/api/inquiries', '/api/inquiries/']:
            self.handle_inquiry()
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "detail": f"Route {self.path} not found on DRF mock server."
            }).encode('utf-8'))

    def handle_booking(self):
        global booking_counter
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception:
            self.send_drf_response(400, {"detail": "Invalid JSON payload."})
            return

        print("\n================ [DRF API: NEW BOOKING RECEIVED] ================")
        print(json.dumps(payload, indent=2))
        print("=================================================================\n")

        # Simulate Django Serializer Validation (e.g. if phone contains 0000000000)
        if payload.get("phone") == "0000000000":
            self.send_drf_response(400, {
                "phone": ["This test phone number is restricted by backend validation rules."]
            })
            return

        booking_counter += 1
        response_data = {
            "id": booking_counter,
            "status": "confirmed",
            "message": "Booking reservation logged successfully in database.",
            "data": payload
        }
        self.send_drf_response(201, response_data)

    def handle_inquiry(self):
        global inquiry_counter
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception:
            self.send_drf_response(400, {"detail": "Invalid JSON payload."})
            return

        print("\n================ [DRF API: NEW INQUIRY RECEIVED] ================")
        print(json.dumps(payload, indent=2))
        print("=================================================================\n")

        inquiry_counter += 1
        response_data = {
            "id": inquiry_counter,
            "status": "received",
            "message": "Custom tour inquiry received by travel desk.",
            "data": payload
        }
        self.send_drf_response(201, response_data)

    def send_drf_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))


if __name__ == '__main__':
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DevAndDRFHandler) as httpd:
        print(f"============================================================")
        print(f" Travel First Holidays Dev Server Running at:")
        print(f" http://127.0.0.1:{PORT}")
        print(f" Serving frontend & Mock DRF APIs (/api/bookings/, /api/inquiries/)")
        print(f" Press Ctrl+C to stop.")
        print(f"============================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()
