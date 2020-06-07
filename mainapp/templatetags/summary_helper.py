from django import template
import logging

register = template.Library()
@register.filter
def filter_usages_sum(usages,master):
    sum = 0
    for usage in filter_usages(usages, master):
        sum += usage.amount
    return sum

@register.filter
def filter_usages_count(usages, master):
    return len(filter_usages(usages, master))

@register.filter
def filter_usages(usages, master):
    filterd_usages = []
    for usage in usages:
        if usage.genre == master:
            filterd_usages.append(usage)

    return filterd_usages

@register.filter
def graph_data_generator(usages):
    return '[10,60,80]'

@register.filter
def graph_label_generator(usages):
    return "['いか','まぐろ','かんぱち']"