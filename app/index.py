import json
from http.server import BaseHTTPRequestHandler
import urllib.parse
[{"name":"mC","marks":62},{"name":"Is7RzS","marks":29},{"name":"0z3ukrSb","marks":91},{"name":"auNW","marks":52},{"name":"azRwfHFk","marks":7},{"name":"derTX","marks":46},{"name":"ZFVdQ6","marks":75},{"name":"FcZr5mCQy","marks":17},{"name":"mnJicTx","marks":91},{"name":"QvqjNG0Gp5","marks":76},{"name":"iUUzMFddTg","marks":50},{"name":"RQPgf","marks":88},{"name":"0m","marks":87},{"name":"qtbp5uNF","marks":51},{"name":"ttVrnKGbKS","marks":93},{"name":"s","marks":94},{"name":"x2NfCA2s","marks":32},{"name":"P0Ax","marks":30},{"name":"tUMu0pNJ","marks":32},{"name":"JULJ","marks":45},{"name":"qAtVUq3UW","marks":39},{"name":"u3Cf","marks":18},{"name":"MzWlJGY4y1","marks":5},{"name":"klyw9Ty","marks":47},{"name":"lA8ov","marks":62},{"name":"DAX","marks":81},{"name":"aQbqyd","marks":37},{"name":"V","marks":62},{"name":"206","marks":19},{"name":"m","marks":91},{"name":"w","marks":90},{"name":"SXZYMdgP","marks":91},{"name":"4zo9cq7","marks":7},{"name":"cjXDS","marks":0},{"name":"kxjNTRs3","marks":89},{"name":"0Xv4r","marks":4},{"name":"UEIqqZUpp","marks":11},{"name":"wCvqM","marks":85},{"name":"F5UXyP8XPo","marks":28},{"name":"sQT","marks":85},{"name":"uvgB4CzrKA","marks":3},{"name":"mihOJG","marks":49},{"name":"LCCeKc","marks":49},{"name":"77r5DWy1","marks":39},{"name":"r9","marks":53},{"name":"hkOWO7hbS5","marks":13},{"name":"X5oPazNe","marks":33},{"name":"fw8bR","marks":39},{"name":"V0qZlRkJ","marks":32},{"name":"aTGz6HdLv","marks":67},{"name":"F","marks":61},{"name":"y","marks":69},{"name":"zyCTnIbsAp","marks":80},{"name":"mlwgCRH","marks":59},{"name":"aChzCf","marks":9},{"name":"EeMpsL","marks":42},{"name":"e17eeC2Bx","marks":3},{"name":"5ta3k2u46N","marks":63},{"name":"PdgUZZZ","marks":7},{"name":"oAAhy","marks":50},{"name":"kNyu6rlm","marks":91},{"name":"yrzyElB","marks":35},{"name":"6APa1p","marks":22},{"name":"ut0y","marks":5},{"name":"tKPdL","marks":81},{"name":"kqIH","marks":46},{"name":"Hj","marks":43},{"name":"y4MaJXG","marks":25},{"name":"H","marks":70},{"name":"QBKpDxz","marks":2},{"name":"Z","marks":41},{"name":"diQgApAS","marks":68},{"name":"8YRsPI","marks":23},{"name":"QYs0D","marks":18},{"name":"HeLf","marks":73},{"name":"xvv8fDHDB","marks":9},{"name":"8TdAUm","marks":43},{"name":"5KuX0H48uv","marks":82},{"name":"dytwC4Ry","marks":80},{"name":"rkK","marks":22},{"name":"bgre3TI2D","marks":95},{"name":"bVJU","marks":60},{"name":"KVRph","marks":60},{"name":"grsOE","marks":77},{"name":"tZ","marks":32},{"name":"cLyEgrNH9W","marks":86},{"name":"5","marks":50},{"name":"6Xsb6gR","marks":60},{"name":"En","marks":21},{"name":"Jz7PlX","marks":44},{"name":"Mx0E44a","marks":79},{"name":"W515","marks":65},{"name":"PQjNqcRhO","marks":48},{"name":"8MSWSJgyGq","marks":12},{"name":"AI88a2","marks":67},{"name":"tyYaHUj","marks":67},{"name":"t1W6","marks":85},{"name":"0j6kWAzj","marks":17},{"name":"82","marks":92},{"name":"jHYjmZREh","marks":50}]


# Handler class to process incoming requests
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)

        # Get 'name' parameters from the query string
        names = query.get('name', [])

        # Load data from the JSON file
        data = load_data()

        # Prepare the result dictionary
        result = {"marks": []}
        for name in names:
            # Find the marks for each name
            for entry in data:
                if entry["name"] == name:
                    result["marks"].append(entry["marks"])

        # Send the response header
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS for any origin
        self.end_headers()

        # Send the JSON response
        self.wfile.write(json.dumps(result).encode('utf-8'))
    
