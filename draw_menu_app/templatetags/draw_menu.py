import collections
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from django import template
from .. import models


register = template.Library()


@register.inclusion_tag('draw_menu_app/draw_menu.html', takes_context=True)
def draw_menu(context: Dict[str, Any], menu_name: str):
    """Draws menu by name"""
    selected_node = context.get('selected_node')

    nodes = models.MenuNode.objects.filter(menu__name=menu_name)
    nodes = nodes.select_related('parent_node')
    node_dict = {node.name: node for node in nodes}
    parent_dict: Dict[str, Optional[str]] = {}
    children_dict = collections.defaultdict(list)

    for node in nodes:
        if node.parent_node is not None:
            parent_name = node.parent_node.name
        else:
            parent_name = None
        
        parent_dict[node.name] = parent_name
        children_dict[parent_name].append(node.name)
    
    path = get_path(selected_node, parent_dict)

    return {
        'selected_node': selected_node,
        'path': frozenset(path),
        'node_dict': node_dict,
        'parent_dict': parent_dict,
        'children_dict': children_dict,
        'node_names': children_dict[None],
    }


def get_path(
    selected_node: Optional[str],
    parent_dict: Dict[str, Optional[str]]
) -> List[Optional[str]]:
    path = [selected_node]
    current_node = selected_node

    while current_node is not None:
        current_node = parent_dict.get(current_node)
        path.append(current_node)
    
    return path
