from django.shortcuts import render


posts = [
    {
        'author': 'Panfilo',
        'title': 'First Post',
        'content': 'This is my first post in my blog',
        'date_posted': 'May 25, 2020'
    }, 
    {
        'author': 'Chekera',
        'title': 'Second Post',
        'content': 'This is my second post in my blog',
        'date_posted': 'May 28, 2020'
    },
    {
        'author': 'Ruperto',
        'title': 'Third Post',
        'content': 'This is my third post in my blog',
        'date_posted': 'May 30, 2020'
    }
]


def home(request):
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html', {'title': 'About'})