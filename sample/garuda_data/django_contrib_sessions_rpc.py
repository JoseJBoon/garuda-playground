# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ GARUDA DOCS
from garuda.django.contrib.sessions.models import Session  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_session(*args, **kwargs):
    try:
        return Session.objects.get(*args, **kwargs)
    except Session.DoesNotExist:
        return None


def read_sessions_filter(*args, **kwargs):
    return Session.objects.filter(*args, **kwargs)


def create_session(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Session.objects.create(*args, **kwargs)


def update_session(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Session.objects.filter(id=id).update(*args, **kwargs)


def delete_session(id):
    return Session.objects.get(id=id).delete()