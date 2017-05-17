from django.conf import settings

def absolute_url(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            "http://{}{}".format(settings.INSTANCE_DOMAIN, function(*args, **kwargs))
        return wrapper
    return real_decorator


# def decorator(argument):
#     def real_decorator(function):
#         def wrapper(*args, **kwargs):
#             function(*args, **kwargs)
#         return wrapper
#     return real_decorator