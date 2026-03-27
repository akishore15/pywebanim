"""
pywebanim - Embed Manim animations into HTML
Copyright (C) 2026 Some Person

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
from .renderer import render_scene
from .html import generate_html
from .utils import save_html

def render_to_html(scene_file, scene_class, output="index.html"):
    video = render_scene(scene_file, scene_class)
    html = generate_html(video)
    save_html(html, output)
