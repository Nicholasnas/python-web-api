from datetime import datetime
from unidecode import unidecode
from blog.database import mongo
import pymongo


def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({'published':published})
    return posts.sort('date', pymongo.DESCENDING)

def get_post_by_slug(slug: str) -> dict:
    "Modificar a url com slug no espaco adiciona '-' e "
    post = mongo.db.posts.find_one({"slug": slug})
    return post 

def update_post_by_slug(slug: str, data: dict) -> dict:
    # $set é um operador do MongoDB para atualizar um documento
    # se o titulo mudar preciso modificar o slug
    if data['title']:
        data['slug'] = criar_slug(data['title'])
        
    data['post_updated'] = datetime.now().strftime(rf"%d/%m/%Y %H:%M:%S")

    result = mongo.db.posts.update_one({"slug": slug}, {"$set": data})
    return result.upserted_id

def criar_slug(title:str) -> str:
    # TODO: Remover assentos -> Resolvido
    title = unidecode(title) # remover assentos
    slug = title.replace(' ', '-').replace('_', '-').lower() 
    return slug
    
def create_post(title:str, content: str, published:bool = True) -> str:
    "title, content, author, published = True"
    slug = criar_slug(title)

    # verificar se já existe o slug no banco de dados
    post = get_post_by_slug(slug)
    if post:
        raise ValueError("Slug já existe")
    #TODO: Preciso verificar se tal url ja esta sendo utilizada, como new
    
    # Criando um novo post  
    new_post = dict()
    new_post['title'] = title
    new_post['content'] = content
    new_post['slug'] = slug
    new_post['date'] = datetime.now().strftime(rf"%d/%m/%Y %H:%M:%S")
    new_post['published'] = published
    
    try:
        post = mongo.db.posts.insert_one(new_post)
    except Exception as e:
        raise ValueError(f"Erro ao inserir post: {e}")

    return slug

def delete_post_by_slug(slug: str) -> dict:
    result = mongo.db.posts.delete_one({"slug": slug})
    if result.deleted_count:
        return True
    return False

    