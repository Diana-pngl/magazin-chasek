from django.contrib import admin
from magazin_chasek import models

admin.site.register([models.Tovar, models.Polzovatel, models.Karzina])