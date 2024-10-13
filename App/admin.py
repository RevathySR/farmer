from django.contrib import admin


from App.models import Advertisement, blog, comment, crop, userProfile,product

# Register your models here.
admin.site.register(crop)
admin.site.register(blog)
admin.site.register(userProfile)
admin.site.register(comment)
admin.site.register(product)
admin.site.register(Advertisement)