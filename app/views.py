from django.views.generic import CreateView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from app.models import File, Category, Tag
from app.forms import SearchForm


class IndexView(TemplateView):
    template_name = "index.html"


class CreateFileView(CreateView):
    model = File
    fields = ['name', 'content', 'category', 'tag']
    success_url = reverse_lazy("index_view")

    def get_context_data(self, **kwargs):
        context = super(CreateFileView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context


class SearchFileView(FormView):
    template_name = 'search.html'
    form_class = SearchForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        search = form.cleaned_data["search"].lower()
        search = form.save(commit=False)
        return super().form_valid(form)

    def search(self, form):
        pass
