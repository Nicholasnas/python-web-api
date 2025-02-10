from database import conn
from pathlib import Path


# Blog estatico 

cursor = conn.cursor()

fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post;").fetchall()

# Juntando dados com os campos
posts = [dict(zip(fields, post)) for post in results]
print(posts)

# Criar pasta de destino do site
site_dir = Path('site')

site_dir.mkdir(exist_ok=True)

# Criar um função capaz de criar uma url
# criar usando um slug

def get_post_url(post): # usando o title
    slug = post['title'].lower().replace(' ', '-')
    return f'{slug}.html'


# Renderizar a pagina index.html
index_template = Path('list.template.html').read_text()
index_page = site_dir / Path('index.html')

post_list = [
    f"<li> <a href='{get_post_url(post)}'>{post['title']} </a> </li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list='\n'.join(post_list)))


# Renderizar as paginas individuais

for post in posts:
    post_template = Path('post.template.html').read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(
        post_template.format(post=post)
    )


print('Site gerado com sucesso!')