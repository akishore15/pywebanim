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
