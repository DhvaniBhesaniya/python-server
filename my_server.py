# from flask import Flask, send_from_directory, abort, render_template_string
# import os

# app = Flask(__name__)
# BASE_DIR = os.path.abspath("/home/abc")

# @app.route('/files/<path:filename>', methods=['GET'])
# def download_file(filename):
#     try:
#         return send_from_directory(BASE_DIR, filename, as_attachment=True)
#     except FileNotFoundError:
#         abort(404)

# @app.route('/')
# def list_files():
#     files = []
#     for root, dirs, files_list in os.walk(BASE_DIR):
#         for file in files_list:
#             files.append(os.path.relpath(os.path.join(root, file), BASE_DIR))
#     files_html = '<br>'.join(f'<a href="/files/{file}">{file}</a>' for file in files)
#     return render_template_string("""
#     <!doctype html>
#     <title>File Server</title>
#     <h1>Files in {{ directory }}</h1>
#     <div>{{ files_html | safe }}</div>
#     """, files_html=files_html, directory=BASE_DIR)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
# 
# 
# 
# 
# 
# 


# dhvani@inventyv:~$ sudo ufw disable
# [sudo] password for dhvani: 
# Firewall stopped and disabled on system startup
# dhvani@inventyv:~$ sudo ufw enable
# Firewall is active and enabled on system startup
# dhvani@inventyv:~$ sudo ufw allow 9000/tcp
# Rule added
# Rule added (v6)
# dhvani@inventyv:~$

#  python3 -m http.server 9000 --bind 0.0.0.0



#---------------------------------------------------------------------


# from http.server import BaseHTTPRequestHandler, HTTPServer

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b'Hello, World!')

# def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
#     server_address = ('', 5001)
#     httpd = server_class(server_address, handler_class)
#     print(f'Starting httpd server on port 5001')
#     httpd.serve_forever()

# if __name__ == '__main__':
#     run()






# ---------------------------------------------
# ---------------------------------------------

# for windows


# If you're using Windows and want to access your HTTP server from your phone, here's how to do it:

# 1. Start the HTTP Server:
# Open Command Prompt.
# Navigate to the directory you want to serve files from.
# Run the command:
# bash
# Copy code
# python3 -m http.server 9000
# This will start the server on port 9000.
# 2. Find Your PC's Local IP Address:
# Open Command Prompt and run:
# bash
# Copy code
# ipconfig
# Look for the IPv4 Address under the network adapter you are using (e.g., Wi-Fi). It will look something like 192.168.1.10.
# 3. Check Firewall Settings:
# The Windows Firewall might block connections to port 9000. To allow traffic on that port:
# Open Windows Defender Firewall from the Control Panel.
# Click on Advanced settings.
# In the left pane, click on Inbound Rules, then in the right pane, click on New Rule….
# Choose Port and click Next.
# Select TCP and enter 9000 in the Specific local ports field.
# Choose Allow the connection and click Next.
# Ensure all profiles (Domain, Private, Public) are checked, then click Next.
# Name the rule something like "Python HTTP Server Port 9000" and click Finish.
# 4. Access the Server from Your Phone:
# Ensure your phone is connected to the same Wi-Fi network as your PC.
# Open a web browser on your phone.
# In the address bar, type:
# text
# Copy code
# http://<your-pc-ip-address>:9000
# Replace <your-pc-ip-address> with the actual IP address you found earlier (e.g., http://192.168.1.10:9000).
# Hit enter, and you should be able to access the files served by the HTTP server on your phone.
# 5. Check Network Connectivity:
# If you have trouble, try pinging your PC from your phone using a network utility app to ensure they can communicate.
# 6. Troubleshooting:
# If it still doesn't work, try disabling the Windows Firewall temporarily to see if that resolves the issue:
# Open Windows Defender Firewall.
# Click on Turn Windows Defender Firewall on or off.
# Turn off the firewall for both Private and Public networks, then test the connection again.