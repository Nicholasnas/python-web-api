from jinja2 import Environment, FileSystemLoader
import re
import json

class Camelo:
    def __init__(self, template_folder="templates"):
        self.url_map :list = [] # roteamendo de urls
        self.template_folder = template_folder
        self.env = Environment(loader=FileSystemLoader(self.template_folder))

    def route(self, rule:str, method:str = "GET", template=None):
        def decorator(view):
            # apenas registrando a rota
            self.url_map.append(
                (rule, method, view, template))
            return view
        return decorator
    
    def render_template(self, template_name, **context):
        template = self.env.get_template(template_name)
        return template.render(**context).encode('utf-8')
        
    def __call__(self, environ, start_response):
        body = b'Content Not Found'
        status = "404 Not Found"
        # Processar o request
        path = environ['PATH_INFO'] # informação do path
        request_method = environ['REQUEST_METHOD']
        content_type = "text/html"
        
        # Resolver as URLS - expressoes regulares
        for rule, method, view, template in self.url_map:
            match = re.match(rule, path)
            if match:
                if method != request_method:
                    continue
                view_args = match.groupdict()
                if method == "POST":
                    view_args["form"] = cgi.FieldStorage(
                        fp=environ["wsgi.input"],
                        environ=environ,
                        keep_blank_values=1,
                    )
                view_result = view(**view_args)

                if isinstance(view_result, tuple):
                    view_result, status, ctype = view_result
                else:
                    status = "200 OK"

                if template:
                    body = self.render_template(template, **view_result)
                elif (
                    isinstance(view_result, dict)
                    and ctype == "application/json"
                ):
                    body = json.dumps(view_result).encode("utf-8")
                else:
                    body = str(view_result).encode("utf-8")

        start_response(status, [("Content-type", ctype)])
        return [body]
    
    def run(self, host="0.0.0.0", port=8000):
        from wsgiref.simple_server import make_server
        server = make_server(host, port, self)  
        print(f"Running on {host}:{port}")
        server.serve_forever()
        
            



