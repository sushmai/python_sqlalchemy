from http.server import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endwith("/hello"):
                self.send_response(200)
                self.send_header("content_type", 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                self.write.write(output)
                print(output)
                return

        except IOError:
            self.send_error(404, 'File not found %s' % self.path)

            

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("web server is running on port %s", port)
        server.server_forever()

    except KeyboardInterrupt:
        print("^C entered, stopped web server")
        server.socket.close()


if __name__ == "__main__":
    main()
