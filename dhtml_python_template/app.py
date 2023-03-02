from http.server import BaseHTTPRequestHandler, HTTPServer
from string import Template
from urllib.parse import parse_qs

# Load the HTML template from a file
with open('page.html', 'r') as file:
    html_template = Template(file.read())

# Define the HTTP request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Generate the dynamic content
        title = "This is my title"
        content = "This is an example of using Python and HTML together without a framework."
        sum = "Sum will be here"
        product = "Product"


        # Render the HTML template with the dynamic content
        html = html_template.substitute(title=title, content=content, sum=sum, product=product)

        # Send the HTML response to the browser
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        # Extract the values of the two input fields
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)
        num1 = int(data['num1'][0])
        num2 = int(data['num2'][0])

        # Generate the dynamic content
        title = "Python HTML example"
        content = "The results"
        sum = num1 + num2
        product = num1 * num2
        sum = f"The sum of {num1} and {num2} is {sum}."
        product = f"The product of {num1} and {num2} is {product}."

        # Render the HTML template with the dynamic content
        html = html_template.substitute(title=title, content=content,sum=sum,product=product)

        # Send the HTML response to the browser
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

# Start the HTTP server
if __name__ == '__main__':
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f' HTTP server started run localhost:{port}...')
    httpd.serve_forever()
