import json
from database import conn
from pathlib import Path
from database import conn
from jinja2 import Environment, FileSystemLoader
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import cgi 
env = Environment(loader=FileSystemLoader('./templates'))


def add_new_post(post:dict):
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        post
    )
    conn.commit()

def get_posts_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")
    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id=?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;").fetchall()

    return [dict(zip(fields, post)) for post in results]


def render_template(template_name, **context):
    template = env.get_template(template_name)

    return template.render(**context).encode('utf-8')

# frameworks tem sistemas de roteamento de urls
def application(environ, start_response):
    body = b'Content Not Found'
    status = "404 Not Found"
    # Processar o request
    # informação do path
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    content_type = "text/html"
    # fazer o proprio roteamento 
    if path == "/" and method == "GET":
        posts = get_posts_from_database()
        body = render_template(
            'list.template.html',
            post_list = posts
        )
        status = "200 OK"

    elif path.split("/")[-1].isdigit() and method == "GET":
        # Verificar se o ultimo valor é string
        post_id = path.split('/')[-1]
        post = get_posts_from_database(post_id)[0]
        body = render_template(
            f'post.template.html',
            post=post
        )
        status = '200 OK'

    elif path == '/new' and method == "GET":
        body = render_template(
            'form.template.html'
        )
        status = '200 OK'
    elif path == '/new' and method == "POST":
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=1 # manter o campo vazio
        )
        post = {item.name: item.value  for item in form.list}
        #Adicionar ao banco de dados
        add_new_post(post)

        body = b"New post created with sucess!"
        status = '201 Created'

    elif path == "/api" and method =="GET":
        posts = get_posts_from_database()
        status = "200 OK"
        body = json.dumps(posts).encode("utf-8") # serializar para json
        content_type = "application/json"
        
    # Criar o response
    headers = [('Content-type', content_type)]
    start_response(status, headers)
    return [body]



from camelo import Camelo

app = Camelo()
app.config()


@app.route('/')
def index():
    posts = get_posts_from_database()
    return render_template(
        'list.template.html',
        post_list = posts
    )

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()

