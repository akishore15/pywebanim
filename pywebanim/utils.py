"""
pywebanim - Embed Manim animations into HTML
Copyright (C) 2026 Some Person

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
import os

def save_html(content, output_path):
    with open(output_path, "w") as f:
        f.write(content)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
