from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.


def index(request):

    return render(request, 'main/base_layout.html')


books_list = [
    {
        'ISBN': 0,
        'title': 'book-1',
        'author': "Mahmoud",
        'publisher': 'EL Nasr',
        'price': 200,
        'description': " A brief description of the book's content BOOK-1 ",
    },
    {
        'ISBN': 1,
        'title': 'book-2',
        'author': "Ahmed",
        'publisher': 'EL Nasr',
        'price': 400,
        'description': " A brief description of the book's content BOOK-2 ",
    },
    {
        'ISBN': 2,
        'title': 'book-3',
        'author': "Omar",
        'publisher': 'EL Nasr',
        'price': 1000,
        'description': " A brief description of the book's content BOOK-3 ",
    },
    {
        'ISBN': 3,
        'title': 'book-4',
        'author': "Khaled",
        'publisher': 'EL Nasr',
        'price': 1500,
        'description': " A brief description of the book's content BOOK-4 ",
    },
    {
        'ISBN': 4,
        'title': 'book-5',
        'author': "Lolo",
        'publisher': 'EL Nasr',
        'price': 3000,
        'description': " A brief description of the book's content BOOK-5 ",
    },
    {
        'ISBN': 5,
        'title': 'book-6',
        'author': "KOKO",
        'publisher': 'EL Nasr',
        'price': 1800,
        'description': " A brief description of the book's content BOOK-6 ",
    },
    {
        'ISBN': 6,
        'title': 'book-7',
        'author': "SOSO",
        'publisher': 'EL Nasr',
        'price': 100,
        'description': " A brief description of the book's content BOOK-7 ",
    }
]


def _get_book(book_id):
    for book in books_list:
        if 'ISBN' in book and book['ISBN'] == book_id:
            return book
    return None


def book_list(request):
    my_context = {'book_list': books_list}
    # template_loader > book/templates/
    return render(request, 'book/book_list.html', context=my_context)


def book_add(request):

    return render(request, 'book/book_add.html')


def book_detail(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    # return HttpResponse(book_object)
    my_context = {
        'book_ISBN': book_object.get('ISBN'),
        'book_title': book_object.get('title'),
        'book_author': book_object.get('author'),
        'book_description': book_object.get('description'),
        'book_publisher': book_object.get('publisher'),
        'book_price': book_object.get('price')

    }

    return render(request, 'book/book_details.html', context=my_context)


def book_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    if books_list:
        books_list.remove(book_object)
    return redirect('book:book-list')


def book_edit(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    return render(request, 'book/book_edit.html', context=book_object)


def book_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    for book in books_list:
        if book == book_object:
            book['name'] = f"Update {book_object['name']}"

    return redirect('book:book-list')
