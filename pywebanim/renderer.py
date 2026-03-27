"""
pywebanim - Embed Manim animations into HTML
Copyright (C) 2026 Some Person

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
import subprocess
import os

def render_scene(scene_file, scene_class, quality="low"):
    quality_flag = {
        "low": "-pql",
        "medium": "-pqm",
        "high": "-pqh"
    }.get(quality, "-pql")

    cmd = [
        "manim",
        quality_flag,
        scene_file,
        scene_class
    ]

    subprocess.run(cmd, check=True)

    # Manim default output path guess
    video_dir = "media/videos"
    return find_latest_video(video_dir)


def find_latest_video(directory):
    latest_file = None
    latest_time = 0

    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".mp4"):
                path = os.path.join(root, f)
                mtime = os.path.getmtime(path)
                if mtime > latest_time:
                    latest_time = mtime
                    latest_file = path

    return latest_file
