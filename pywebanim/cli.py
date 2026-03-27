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
