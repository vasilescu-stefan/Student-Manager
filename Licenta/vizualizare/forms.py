from django import forms

class Pachet1(forms.Form):
    OPTIONS = [
        ('Calculabilitate, decidabilitate şi complexitate', 'Calculabilitate, decidabilitate şi complexitate'),
        ('Principii ale limbajelor de programare', 'Principii ale limbajelor de programare'),
        ('Algoritmi genetici', 'Algoritmi genetici'),
        ('Quantum Computing', 'Quantum Computing'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)


class Pachet2(forms.Form):
    OPTIONS = [
        ('Programare funcţională', 'Programare funcţională'),
        ('Introducere în criptografie', 'Introducere în criptografie'),
        ('Antreprenoriat și inovare în IT', 'Antreprenoriat și inovare în IT'),
        ('Sisteme embedded', 'Sisteme embedded'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)


class Pachet3(forms.Form):
    OPTIONS = [
        ('Introducere în .NET', 'Introducere în .NET'),
        ('Dezvoltarea sistemelor fizice utilizând microprocesoare', 'Dezvoltarea sistemelor fizice utilizând microprocesoare'),
        ('Rețele neuronale', 'Rețele neuronale'),
        ('Animaţie 3D: algoritmi şi tehnici fundamentale', 'Animaţie 3D: algoritmi şi tehnici fundamentale'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)


class Pachet4(forms.Form):
    OPTIONS = [
        ('Programare și modelare probabilistă', 'Programare și modelare probabilistă'),
        ('Introducere în realitatea mixtă', 'Introducere în realitatea mixtă'),
        ('Capitole speciale de sisteme de operare', 'Capitole speciale de sisteme de operare'),
        ('Tehnici de programare multiprocesor', 'Tehnici de programare multiprocesor'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)


class Pachet5(forms.Form):
    OPTIONS = [
        ('Programare bazată pe reguli', 'Programare bazată pe reguli'),
        ('Tehnici de programare pe platforme mobile', 'Tehnici de programare pe platforme mobile'),
        ('Aspecte computaţionale în teoria numerelor', 'Aspecte computaţionale în teoria numerelor'),
        ('Proiectarea jocurilor', 'Proiectarea jocurilor'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)

class Pachet6(forms.Form):
    OPTIONS = [
        ('Psihologia comunicării profesionale în domeniul IT', 'Psihologia comunicării profesionale în domeniul IT'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Interacțiune om-calculator', 'Interacțiune om-calculator'),
        ('Analiza reţelelor media sociale', 'Analiza reţelelor media sociale'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)


class Pachet7(forms.Form):
    OPTIONS = [
        ('Reţele Petri şi aplicaţii', 'Reţele Petri şi aplicaţii'),
        ('Smart Card-uri şi Aplicaţii', 'Smart Card-uri şi Aplicaţii'),
        ('Inginerie software specifică automobilelor', 'Inginerie software specifică automobilelor'),
        ('	Introducere în Internetul lucrurilor', '	Introducere în Internetul lucrurilor'),
    ]
    preference1 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference2 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference3 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)
    preference4 = forms.ChoiceField(choices=OPTIONS, widget=forms.Select)

