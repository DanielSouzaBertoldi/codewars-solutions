import re

def to_camel_case(text):
    return re.sub(r'([-_])([a-z]|[A-Z])', lambda pat: pat.group(2).upper(), text)