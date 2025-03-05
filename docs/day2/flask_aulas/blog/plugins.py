""" Registrar qualquer tipo de plugins """

from mistune import markdown
from flask import Flask


def configure(app:Flask):
    # Adicionar a opção de formatar um mardown {{mardown(text)}} html to mk
    app.add_template_global(markdown)
    
    # {{data | format_date}}
    app.add_template_filter(lambda date: date.split(" ")[0], "format_date")