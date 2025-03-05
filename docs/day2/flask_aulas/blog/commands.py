# Usar o flask CLI
from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    create_post,
    delete_post_by_slug
)
from flask.cli import AppGroup
import click
from datetime import datetime

""" Receber dados via linha de comando. """
post = AppGroup('post')


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    "Create a new post"
    new = create_post(title, content)
    click.echo(f"Post criado com sucesso: {new}")
    
@post.command("list")
def show_posts():
    "List all posts"
    post = get_all_posts()
    for post in post:
        click.echo(post)    
    
@post.command()
@click.argument("slug")
def get(slug):
    "Get post by slug"
    post = get_post_by_slug(slug)    
    click.echo(post or "Post Not Found 404")

# update_post_by_slug(slug: str, data: dict)
@post.command()
@click.argument("slug")
@click.option("--title", default=None, type=str)
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, title, content, published):
    "Update post by slug"
    data = {}
    if title:
        data['title'] = title
    if content:
        data['content'] = content
    if published:
        data['published'] = published
    
    result = update_post_by_slug(slug, data)
    if result:
        click.echo(f"Post {slug} Update")
    else:
        click.echo(f"Post {slug} Not Found")    

@post.command()
@click.argument("slug")
def delete(slug):
    "Delete post by slug"
    if post:
        delete_post_by_slug(slug)
        click.echo(f"Post {slug} Deleted")
    else:
        click.echo(f"Post {slug} Not Found")
    
def configure(app):
    app.cli.add_command(post)


    
