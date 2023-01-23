from ask_everything_about_me.config import settings

service_name2url = {
    "twitter": settings.twitter_url,
    "facebook": settings.facebook_url,
    "linkedin": settings.linkedin_url,
}


def get_url(service_name):
    if service_name2url.get(service_name):
        return service_name2url[service_name]
    return f"URL of {service_name} is not found"
