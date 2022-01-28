from django.db import models

# Create your models here.
from online_lottery import settings
import requests
from django.db import models



class Outbox(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    statusCode = models.IntegerField()
    phone = models.CharField(max_length=15)
    text = models.CharField(max_length=255)
    messageId = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Outbox")
        verbose_name_plural = ("Outbox")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.messageId, self.status, self.text[:10])  # noqa: E501

    @staticmethod
    def send(phone_number, message):
        url = "https://api.sandbox.africastalking.com/version1/messaging"
        headers = {'ApiKey': 'b2562de741efd7f8e3ea27793682ccc2176795f1ab0f80d68256a40e8b94b2bd',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'}
        body = {'username': 'sandbox',
                'from': '8222',
                'message': message,
                'to': phone_number}
        response = requests.post(url=url, headers=headers, data=body)
        data = response.json().get('SMSMessageData').get('Recipients')[0]
        Outbox_object = Outbox(status=data['status'],
                               statusCode=data['statusCode'],
                               phone=data['number'],
                               text=message,
                               messageId=data['messageId'])
        Outbox_object.save()


