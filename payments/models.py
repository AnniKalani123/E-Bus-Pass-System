from django.db import models
from myapp.models import Pass, User


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    pass_id = models.ForeignKey(Pass, related_name='Pass', on_delete=models.CASCADE,null=True, blank=True)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    pay_status = models.CharField(max_length=256, null=True, blank=True,)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.made_by.Username
        
