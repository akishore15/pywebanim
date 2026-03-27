from .renderer import render_scene
from .html import generate_html
from .utils import save_html

def render_to_html(scene_file, scene_class, output="index.html"):
    video = render_scene(scene_file, scene_class)
    html = generate_html(video)
    save_html(html, output)
