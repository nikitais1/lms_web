from django.apps import AppConfig
from django.db.models.signals import post_save


class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        post_save.connect(signals.handle_course_save)