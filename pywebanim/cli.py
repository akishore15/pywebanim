"""
pywebanim - Embed Manim animations into HTML
Copyright (C) 2026 Some Person

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
import argparse
from .renderer import render_scene
from .html import generate_html
from .utils import save_html

def main():
    parser = argparse.ArgumentParser(description="pywebanim CLI")

    parser.add_argument("scene_file", help="Path to scene.py")
    parser.add_argument("scene_class", help="Scene class name")
    parser.add_argument("--output", default="index.html")
    parser.add_argument("--quality", default="low")

    args = parser.parse_args()

    video_path = render_scene(
        args.scene_file,
        args.scene_class,
        args.quality
    )

    html = generate_html(video_path)
    save_html(html, args.output)

    print(f"✅ HTML generated at {args.output}")
