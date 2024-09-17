from .models import ImageUpload
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ImageUpload(CreateView):
    template_name = 'imageupload/upload.html'
    model = ImageUpload
    fields = ('image',)
    success_url = reverse_lazy('top')