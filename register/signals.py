from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """

    :param sender: the user type that sent the signal (signal after registration to create a profile, to count logins)
    :param instance: the actual instance of the user.
    :param created: boolean that indicate whether the registration is done.
    :param kwargs: not used.
    :return:
    """
    if created:
        # if registration is done, then create also a profile by signal.
        Profile.objects.create(user=instance)


# similar, just receive the signal and create the user profile.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()