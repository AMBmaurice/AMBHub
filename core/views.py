from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def page_connexion(request):
    # Si l'utilisateur est déjà connecté, on l'envoie directement au hub
    if request.user.is_authenticated:
        return redirect('hub')

    if request.method == 'POST':
        identifiant = request.POST.get('username')
        mot_de_passe = request.POST.get('password')
        se_souvenir = request.POST.get('remember_me')
        
        # Vérification des identifiants dans la base de données
        user = authenticate(request, username=identifiant, password=mot_de_passe)
        
        if user is not None:
            login(request, user)
            
            if se_souvenir:
                # Conserve la session pendant 10 jours (864 000 secondes)
                request.session.set_expiry(864000)
            else:
                # La session expire dès la fermeture du navigateur
                request.session.set_expiry(0)
                
            return redirect('hub')
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect.")
            
    return render(request, 'login.html')

def page_hub(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    return render(request, 'hub.html')

def page_deconnexion(request):
    logout(request)
    return redirect('connexion')
