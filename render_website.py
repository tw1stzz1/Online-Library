from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

from livereload import Server, shell


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open("books_parameters.json", "r", encoding="utf8") as my_file:
        books_parameters = my_file.read()

    books = json.loads(books_parameters)

    rendered_page = template.render(
        books=books
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


on_reload()

server = Server()
server.watch('template.html', on_reload())
server.serve(root='.')