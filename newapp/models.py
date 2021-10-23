from django.db import models

# customer table
class customer(models.Model):
    customer_id = models.AutoField(auto_created = True, primary_key = True)
    customer_name =  models.CharField(max_length = 60)
    age = models.IntegerField()
    height_cm = models.IntegerField()
    weight_kg =  models.FloatField()
    email = models.CharField(max_length = 40)
    phone_no = models.CharField(max_length = 20)

# order table
class order(models.Model):
    order_id = models.AutoField(auto_created = True, primary_key = True)
    food_id = models.IntegerField()
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    #delivery_id = models.ForeignKey(deliveryman,on_delete=models.CASCADE)
    food_quantity = models.IntegerField()
    food_category = models.CharField(max_length = 30)
    total_price_taka = models.IntegerField()
    order_location = models.CharField(max_length = 100)
    order_status = models.CharField(max_length = 30)

#delivery man table
class deliveryman(models.Model):
    delivery_id = models.IntegerField(primary_key = True)
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE)
    bill = models.IntegerField()
    order_location = models.CharField(max_length = 100)
    
#food table
class food(models.Model):
    food_id = models.IntegerField(primary_key = True)
    food_category = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30)
    price = models.IntegerField()

# chef table
class chef(models.Model):
    chef_id = models.IntegerField(primary_key = True)
    chef_name = models.CharField(max_length = 50)
    experience = models.CharField(max_length = 30)

# nutritionist table
class nutritionist(models.Model):
    nutritionist_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 30)
    experience = models.CharField(max_length = 25)
