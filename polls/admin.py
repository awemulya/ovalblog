from django.contrib import admin

from models import Question,Choice , Manufacturer , Product

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Question',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter= ('question_text', 'pub_date')
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)


class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ('country',)
	list_filter = ('country',)
	search_fields = ('country',)

admin.site.register(Manufacturer , ManufacturerAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name' , 'price' , 'manufacturer' , 'release_date',)
	list_filter = ('name' , 'price' , 'manufacturer' , 'release_date',)
	search_fields = ('name',)
admin.site.register(Product , ProductAdmin)