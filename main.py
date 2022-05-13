from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import time, huawei_solar, pytz
import importlib
importlib.reload(huawei_solar)

# Variables to create the html document
hostName = "localhost"
serverPort = 8081

# Solar inverter variables module. Local IP y datetime from peninsular Spain
h = huawei_solar.HuaweiSolar(host="[INSERT_INVERTER_LOCAL_IP]")
input_power = h.get("input_power")
active_power = h.get("active_power")
power_meter_active_power = h.get("power_meter_active_power")
energy_consumption = active_power.value - power_meter_active_power.value

# Timezone variables
tz_ES = pytz.timezone('Europe/Madrid') 
datetime_ES = datetime.now(tz_ES)

class MyServer(BaseHTTPRequestHandler):

# Printing the web including Python variables
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Huawei Solar inverter Data</title>", "utf-8"))
        self.wfile.write(bytes("<meta http-equiv='refresh' content='10' />", "utf-8"))
        self.wfile.write(bytes("</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Input energy (registered by panels): {} {}</p>".format(str(input_power.value), str(input_power.unit)), "utf-8"))
        self.wfile.write(bytes("<p>Active energy (ready to be taken): {} {}</p>".format(str(active_power.value), str(active_power.unit)), "utf-8"))
        self.wfile.write(bytes("<p>Exported energy (discharged to be compensated): {} {}</p>". format(str(power_meter_active_power.value),str(power_meter_active_power.unit)), "utf-8"))
        self.wfile.write(bytes("<p>Energy consumption currently: {} {}</p>".format(str(energy_consumption), str(input_power.unit)), "utf-8"))
        self.wfile.write(bytes("<p>Date: %s</p>" % str(datetime_ES.strftime("%d/%m/%Y")), "utf-8"))
        self.wfile.write(bytes("<p>Time: %s</p>" % str(datetime_ES.strftime("%H:%M:%S")), "utf-8"))
        self.wfile.write(bytes("<p>Timezone: %s</p>" % tz_ES, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

# Starting server advice on terminal
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

# Stopping server advice on terminal
    webServer.server_close()
    print("Server stopped.")
