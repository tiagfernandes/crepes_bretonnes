from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('auteur', 'categorie', 'slug')  # Exclura les champs nommés « auteur », « categorie » et « slug »


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    envoyeur = forms.EmailField(label="Votre adresse e-mail", widget=forms.TextInput(attrs={'class': "form-control"}))
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")

        return message  # Ne pas oublier de renvoyer le contenu du champ traité
