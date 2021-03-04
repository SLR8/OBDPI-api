from django.db import models
from django.contrib.auth import get_user_model
from obd.decoders import fuel_pressure

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Yierra(models.Model):
    did = None

class OBD(models.Model):
    ELM_VERSION = models.CharField( max_length=50)
    ELM_VOLTAGE = models.IntegerField()
    yierra = models.ForeignKey(Yierra, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

class Vehicle(models.Model):
    vid = models.CharField(max_length=24)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_speed = models.IntegerField()
    hybrid_battery_pack_remaining_life = models.IntegerField()

    

class Engine(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete= models.CASCADE)

    engine_load = models.IntegerField() # percent
    engine_coolant_temperature = models.IntegerField() # Degrees celcius
    fuel_pressure =  models.IntegerField() # kilo Pascal
    engine_rpm = models.IntegerField()
    timing_advance = models.IntegerField()
    intake_air_temp = models.IntegerField()
    air_flow_rate = models.IntegerField() 
    throttle_position = models.IntegerField()
    engine_run_time = models.IntegerField()
    fuel_level_input = models.IntegerField()
    warmups_since_codes_cleared = models.IntegerField()
    barometric_pressure = models.IntegerField()
    ambient_air_temperature = models.IntegerField()
    commanded_throttle_actuator = models.IntegerField()
    time_run_with_MIL_on = models.IntegerField()
    time_since_trouble_codes_cleared = models.IntegerField()
    engine_fuel_rate = models.IntegerField()