from django.views.generic import FormView, TemplateView
from .forms import NewsLetterForm
from django.urls import reverse_lazy


class NewsLettersView(FormView):
    template_name = 'newsletter/subscribe.html'
    form_class = NewsLetterForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'newsletter/success.html'
