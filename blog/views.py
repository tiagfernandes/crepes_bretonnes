from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article
from .forms import ContactForm, ArticleForm


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article})


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    # return HttpResponse("""
    #     <html><body><h1>Bienvenue sur mon blog !</h1>
    #     <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p></body></html>
    # """)
    couleurs = {
        '#FF0000': 'rouge',
        '#ED7F10': 'orange',
        '#FFFF00': 'jaune',
        '#00FF00': 'vert',
        '#0000FF': 'bleu',
        '#4B0082': 'indigo',
        '#660099': 'violet',
    }
    return render(request, 'blog/home.html', {'date': datetime.now(), 'pseudo': "Test", 'couleurs': ""})


def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if id_article > 100:
        return redirect(list_articles, month=12, year=2010)

    return render(request, 'blog/article.html', {'id_article': id_article})


def list_articles_by_tag(request, tag):
    return HttpResponse(
        "<html><body>Vous avez demandé l'article tag {0} !</body></html>".format(tag)
    )


def list_articles(request, month, year):
    if month == '12' and year == '1900':
        return redirect(home)

    return HttpResponse(
        "<html><body>Vous avez demandé l'article du mois {0} année {1} !</body></html>".format(month, year)
    )


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())


def pourcentage(request, nombre1, nombre2):
    result = nombre1 / nombre2 * 100

    return render(request, 'blog/pourcentage.html', locals())


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())


def article_new(request):
    article = Article()
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/article.html', locals())
