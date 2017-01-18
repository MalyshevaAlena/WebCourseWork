from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from jinja2 import Environment, FileSystemLoader


PATH = "C:\\Users\\Алена\Desktop\WebCourseWork"
ENV = Environment(loader=FileSystemLoader(PATH))


def start(request):
    templ = ENV.get_template("pages/start.html")
    return Response(templ.render())

def gallery(request):
    templ = ENV.get_template("pages/gallery.html")
    return Response(templ.render())

def aboutsite(request):
    templ = ENV.get_template("pages/aboutsite.html")
    return Response(templ.render())

def news(request):
    templ = ENV.get_template("pages/news.html")
    return Response(templ.render())

def news1(request):
    templ = ENV.get_template("pages/news1.html")
    return Response(templ.render())
def news2(request):
    templ = ENV.get_template("pages/news2.html")
    return Response(templ.render())
def news3(request):
    templ = ENV.get_template("pages/news3.html")
    return Response(templ.render())

def trends(request):
    templ = ENV.get_template("pages/trends.html")
    return Response(templ.render())


def main():
    config = Configurator() #создаем конфиг приложения


    config.add_route('start', 'pages/start.html')
    config.add_route('trends', 'pages/trends.html')
    config.add_route('news', 'pages/news.html')
    config.add_route('news1', 'pages/news1.html')
    config.add_route('news2', 'pages/news2.html')
    config.add_route('news3', 'pages/news3.html')
    config.add_route('gallery', 'pages/gallery.html')
    config.add_route('aboutsite', 'pages/aboutsite.html')

    config.add_static_view('image', PATH + "/image")
    config.add_static_view('css', PATH + "/css")
    config.add_view(start, route_name='start')
    config.add_view(trends, route_name='trends')
    config.add_view(news, route_name='news')
    config.add_view(news1, route_name='news1')
    config.add_view(news2, route_name='news2')
    config.add_view(news3, route_name='news3')
    config.add_view(gallery, route_name='gallery')
    config.add_view(aboutsite, route_name='aboutsite')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()

if __name__ == "__main__":
    main()
