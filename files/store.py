import os, html, pymysql
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "2.0"
SERVED_BY = os.environ.get('SERVED_BY', 'unknown')

def rows():
    c = pymysql.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                        password=os.environ['DB_PASS'], database=os.environ['DB_NAME'])
    with c.cursor() as cur:
        cur.execute("SELECT name, price FROM products ORDER BY name")
        data = cur.fetchall()
    c.close()
    return data

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = "".join("<tr><td>%s</td><td>$%.2f</td></tr>" % (n, p) for n, p in rows())
        footer = "<p><small>Cougar Curds storefront v%s &middot; served by %s</small></p>" % (VERSION, html.escape(SERVED_BY))
        page = "<h1>Cougar Curds — Price List</h1><table border=1 cellpadding=8>" + body + "</table>" + footer
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(page.encode())

ThreadingHTTPServer(('0.0.0.0', 8080), H).serve_forever()
