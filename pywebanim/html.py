"""
pywebanim - Embed Manim animations into HTML
Copyright (C) 2026 Some Person

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
def generate_html(video_path, autoplay=True, loop=True):
    autoplay_attr = "autoplay" if autoplay else ""
    loop_attr = "loop" if loop else ""

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>pywebanim</title>
</head>
<body>
    <video controls {autoplay_attr} {loop_attr} width="800">
        <source src="{video_path}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""
