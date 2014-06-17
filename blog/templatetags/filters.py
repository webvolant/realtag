from django import template

register = template.Library()

@register.filter
def create_range(value, start_index=1):
	return range(start_index, value+start_index)

@register.filter
def create_range2(value, start_index=0):
	return range(start_index, value+start_index)