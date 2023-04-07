from typing import Any
from typing import Dict
from typing import FrozenSet
from typing import Optional
from django import template
from .. import models


register = template.Library()


@register.inclusion_tag('draw_menu_app/draw_menu_node.html', takes_context=True)
def draw_menu_node(context: Dict[str, Any], node_name: str):
    path: FrozenSet[Optional[str]] = context['path']
    node_dict: Dict[str, models.MenuNode] = context['node_dict']
    parent_dict: Dict[str, Optional[str]] = context['parent_dict']
    children_dict: Dict[Optional[str], str] = context['children_dict']

    readable_name = node_dict[node_name].readable_name

    if node_name in path:
        children = children_dict[node_name]
    else:
        children = []

    return {
        'name': node_name,
        'readable_name': readable_name,
        'children': children,
        'path': path,
        'node_dict': node_dict,
        'parent_dict': parent_dict,
        'children_dict': children_dict,
    }
