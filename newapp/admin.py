from django.contrib import admin

#import table
from newapp.models import customer
from newapp.models import order
from newapp.models import deliveryman
from newapp.models import food
from newapp.models import chef
from newapp.models import nutritionist

#table view class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "customer_name", "age", "height_cm", "weight_kg", "email","phone_no")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id","food_id","customer_id","food_quantity","food_category","total_price_taka","order_location","order_status")

class DeliverymanAdmin(admin.ModelAdmin):
    list_display = ("delivery_id","order_id","customer_id","bill", "order_location")

class FoodAdmin(admin.ModelAdmin):
    list_display = ("food_id","food_category","name","price")

class ChefAdmin(admin.ModelAdmin):
    list_display = ("chef_id","chef_name","experience")

class NutritionistAdmin(admin.ModelAdmin):
    list_display = ("nutritionist_id","name","designation","experience")

#regester table
admin.site.register(customer,CustomerAdmin)
admin.site.register(order,OrderAdmin)
admin.site.register(deliveryman,DeliverymanAdmin)
admin.site.register(food,FoodAdmin)
admin.site.register(chef,ChefAdmin)
admin.site.register(nutritionist,NutritionistAdmin)