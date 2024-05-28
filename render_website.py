import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
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
    books_pages = list(chunked(books, 20))
    pages_count = len(books_pages)
    Path('pages').mkdir(parents=True, exist_ok=True)
    for page_number, books_on_page in enumerate(books_pages, 1):
        sorted_books = list(chunked(books_on_page, 2))
        rendered_page = template.render(
            pages=pages_count,
            page_number=page_number,
            books=sorted_books
        )

        with open(f'pages/index{page_number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


on_reload()

server = Server()
server.watch('template.html', on_reload())
server.serve(root='.')