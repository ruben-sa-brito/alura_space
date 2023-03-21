from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha'
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'ex.: joao silva'
            }
        )
        
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite seu nome'
            }
        )
    )
    
    email = forms.EmailField(
        label = "Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'ex.: joaosilva@xpto.com'
            }
        )
        
    )
    
    senha_1 = forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'ex.: Digite sua senha'
            }
        )
        
    )
    
    senha_2 = forms.CharField(
        label = "Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'ex.: Digite sua senha novamente'
            }
        )
        
    )  
    
         