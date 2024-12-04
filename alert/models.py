from django.db import models
from decouple import config
from twilio.rest import Client

# Create your models here.
class Magnitude(models.Model):
    result = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        twilio_acc_sid = config('TWILIO_ACCOUNT_SID')
        twilio_auth_token = config('TWILIO_AUTH_TOKEN')
        twilio_phone_number = config('TWILIO_PHONE_NUMBER')

        client = Client(twilio_acc_sid, twilio_auth_token)

        # Send a message every time a Magnitude instance is saved
        message = client.messages.create(
            body=f'A {self.result} magnitude earthquake has been detected near you. Drop, Cover, and Hold On. Avoid windows and unstable structures. Stay safe and await official updates.',
            from_=twilio_phone_number,
            to='+639308783002'
        )

        print(f"Message sent with SID: {message.sid}")
        return super().save(*args, **kwargs)
