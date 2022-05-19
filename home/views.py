from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import musicData

class ListView(generic.ListView):
    template_name = 'home/list.html'
    context_object_name = 'music_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # musics = musicData.objects.db_manager("music").all() # default以外のDB,データベースからオブジェクトを取得して
        musics = musicData.objects.db_manager("music").order_by('-id')[:5]
        
        return musics

