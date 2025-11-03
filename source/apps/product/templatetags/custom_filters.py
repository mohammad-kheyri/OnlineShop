from django import template

register = template.Library()

@register.filter
def get_item_name(items, key):
    """
    Retrieve the name matching the given key (id) from the list of category, brand, or color dictionaries.
    """
    for item in items:
        # Try category, brand, or color based on what's in the dictionary
        obj = item.get('category') or item.get('brand') or item.get('color')
        if obj and str(obj.id) == str(key):
            return obj.name
    return ''
