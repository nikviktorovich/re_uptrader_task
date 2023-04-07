from typing import Optional
from django.shortcuts import render


# Create your views here.

def draw_menu_view(request, selected_node: Optional[str] = None):
    return render(request, 'draw_menu_app/index.html', context={
        'selected_node': selected_node,
    })
