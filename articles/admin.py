from django.contrib import admin
<<<<<<< HEAD

=======
from .models import Maqola
@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display=['id','title']
    class Meta:
        model=Maqola
>>>>>>> fc755d3 (blog_site a)
# Register your models here.
