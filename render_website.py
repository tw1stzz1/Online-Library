import json
from pathlib import Path
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from livereload import Server


parser = argparse.ArgumentParser(description='This code allows you to download books and their covers form tululu')
parser.add_argument('--book_parameters', default='books_parameters.json', help='Relative path to the file were you have information about books')
parser.add_argument('--html_template', default='template.html', help='Relative path to the html template file')
parser.add_argument('--folder_with_pages', default='pages', help='Relative path to the folder were your pages')
args = parser.parse_args()


def on_reload():
    with open(args.book_parameters, 'r', encoding='utf8') as my_file:
        books = json.load(my_file)

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html"])
    )
    template = env.get_template(args.html_template)

    page_books_limit = 20
    row_books_limit = 2

    books_pages = list(chunked(books, page_books_limit))
    pages_count = len(books_pages)

    for page_number, books_on_page in enumerate(books_pages, 1):
        sorted_books = list(chunked(books_on_page, row_books_limit))
        rendered_page = template.render(
            pages=pages_count,
            page_number=page_number,
            books=sorted_books
        )

        with open(f'{args.folder_with_pages}/index{page_number}.html', 'w', encoding='utf8') as file:
            file.write(rendered_page)


def main():
    Path(args.folder_with_pages).mkdir(parents=True, exist_ok=True)
    on_reload()
    
    server = Server()
    server.watch("template.html", on_reload)
    server.serve(root=".",  default_filename="pages/index1.html")


if __name__ == '__main__':
    main()
