from django.contrib import admin
from .models import Book,Author,Address,Country
from django.utils.translation import gettext_lazy as _

# Register your models here.

class RatingRangeFilter(admin.SimpleListFilter):
    title = _('rating range')
    parameter_name = 'rating_range'

    def lookups(self, request, model_admin):
        return [
            ('1-2', _('1')),
            ('2-3', _('2')),
            ('3-4', _('3')),
            ('4+', _('4+')),
        ]

    def queryset(self, request, queryset):
        if self.value() == '1-2':
            return queryset.filter(rating__gte=1, rating__lt=2)
        elif self.value() == '2-3':
            return queryset.filter(rating__gte=2, rating__lt=3)
        elif self.value() == '3-4':
            return queryset.filter(rating__gte=3, rating__lt=4)
        elif self.value() == '4+':
            return queryset.filter(rating__gte=4)
        return queryset
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('author', RatingRangeFilter)
    list_display = ["title", "author", "rating"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "full_address"]


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)