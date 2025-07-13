# core/urls_debug.py (no lo importes en producción)
from django.urls import get_resolver
for url in get_resolver().url_patterns:
    print(url)
