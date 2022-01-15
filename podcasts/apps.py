from django.apps import AppConfig


class PodcastsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # This automatically generates your primary key
    name = 'podcasts'
    verbose_name = "Podcasts"