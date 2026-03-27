from manim import *

class MyScene(Scene):
    def construct(self):
        text = Text("Hello from pywebanim!")
        self.play(Write(text))
        self.wait()
