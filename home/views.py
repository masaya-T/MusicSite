from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import musicData, menueData

class MusicListView(generic.ListView):
    template_name = 'home/list.html'
    musics=0
    menue_data=0
    # context_object_name = 'music_list'

    
    def get_queryset(self):
        """Return the last five published questions."""
        # musics = musicData.objects.db_manager("music").all() # default以外のDB,データベースからオブジェクトを取得して
        self.musics = musicData.objects.db_manager("music").order_by('-id')[:5]
        self.menue_data = menueData()
        artists=[]
        for i in musicData.objects.db_manager("music").order_by('-id'):
            artists.append(i.artist)
        self.menue_data.all_artist=list(set(artists))
        self.menue_data.now_song=musicData.objects.db_manager("music").order_by('-id')[0]
        return self.musics,self.menue_data

    def get_context_data(self, **kwargs):
        context = super(MusicListView, self).get_context_data(**kwargs)
        context['music_list'] = self.musics
        context['now_song'] = self.menue_data.now_song

        return context