from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment Application'
 
    def ready(self):
        import payment.signals
