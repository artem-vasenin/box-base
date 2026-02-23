from app_home.models import Settings


def global_data(request):
    return {
        'site_settings': Settings.objects.first(),
    }