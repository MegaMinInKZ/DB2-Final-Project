from django.db import models
class TOP_10(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    Image = models.URLField(max_length = 200)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})