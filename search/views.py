from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pure_pagination.mixins import PaginationMixin
from rest_framework import generics, viewsets

from .models import Meibo
from .forms import SearchForm, UploadForm
from .serializers import MeiboSerializer

class IndexView(PaginationMixin, generic.ListView):
    model = Meibo
    paginate_by = 8

    def get_queryset(self):
        str = self.request.GET.get('keywords', None)
        q = Meibo.get_kensaku(str)
        return Meibo.objects.filter(q).order_by('simei_kana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)
        return context

class MeiboView(viewsets.ModelViewSet):
    serializer_class = MeiboSerializer
    queryset = Meibo.objects.all()

    def get_queryset(self):
        keywords = self.request.GET.get('keywords', None)
        q = Meibo.get_kensaku(keywords)
        return Meibo.objects.filter(q).order_by('simei_kana')

class MeiboListCreate(generics.ListCreateAPIView):
    serializer_class = MeiboSerializer

    def get_queryset(self):
        keywords = self.request.GET.get('keywords', None)
        q = Meibo.get_kensaku(keywords)
        return Meibo.objects.filter(q).order_by('simei_kana')

# ファイルのアップロード
class UploadView(generic.TemplateView):
    template_name = 'search/upload.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upload_form'] = UploadForm()
        return context

    # テーブルへのインポート関数
    def post(self, request, **kwargs):
        try:
            Meibo.from_csv(request.FILES['file'])
        except:
            return HttpResponse('失敗やアホ!')

        return redirect('../')