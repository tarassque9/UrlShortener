from django.db import models

class UrlData(models.Model):
    url = models.URLField(max_length=200, unique=True)
    slug = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"
    
class UrlStatistic(models.Model):
    url = models.ForeignKey(UrlData, on_delete=models.CASCADE)
    request_time = models.DateTimeField(default=None, null=True)
    ip_address = models.GenericIPAddressField(protocol="IPv4", null=True)
    refferer = models.URLField(max_length=100, default='')