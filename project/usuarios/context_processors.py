from .models import Avatar

def avatar_context(request):
    avatar_url = None
    if request.user.is_authenticated:
        avatars = Avatar.objects.filter(user=request.user.id)
        if avatars.exists():
            avatar_url = avatars[0].imagen.url
    
    return {"avatar_url": avatar_url}
