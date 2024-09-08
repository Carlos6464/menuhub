from django.db import models

# Create your models here.
class Restaurant(models.Model):
    """Um objeto da classse Restaurant armazena informações
        sobre um restaurante."""
    name = models.CharField(max_length=45)
    
    def __str__(self):
        """Retorna uma representação em string do objeto."""
        return f"[Restaurant] name: {self.name}"


class MenuItem(models.Model):
    """Um objeto da classe MenuItem armazena informações sobre um
        item de um menu de um restaurante."""
    category = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __srt__(self):
        """Retorna uma representação em string do objeto."""
        return f"[MenuItem] description: {self.description[:50]}"
    
        