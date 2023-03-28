from manim import *


class DotProduct(Scene):
    def construct(self):
        hypetext = Tex("Dot Product Lore")
        tex = MathTex("\\vec{P}\cdot{}\\vec{Q}=\lVert\\vec{P}\\rVert\lVert\\vec{Q}\\rVert\\cos{\\theta}")
        self.add(hypetext)
        self.play(Transform(hypetext, tex))
        self.wait(.5)

        # show the pic of the triangle we are going to use to prove this shi
        vect_P = Line(start = [0, 0, 0], end = [2, .5, 0], stroke_color = YELLOW).add_tip()
        vect_P_name = MathTex("\\vec{P}").next_to(vect_P, DOWN, buff=.1).set_color(YELLOW)

        vect_Q = Line(start = [0, 0, 0], end = [1, 2, 0], stroke_color = RED).add_tip()
        vect_Q_name = MathTex("\\vec{Q}").next_to(vect_Q, LEFT, buff=.1).set_color(RED)

        self.play(FadeOut(hypetext), run_time = .4)
        self.play(GrowFromPoint(vect_P, point = vect_P.get_start()), Write(vect_P_name), 
                  GrowFromPoint(vect_Q, point = vect_Q.get_start()), Write(vect_Q_name), run_time = .5)
        self.wait(.2)

        vect_Q_minus_P = Line(start = vect_P.get_end(), end = vect_Q.get_end(), stroke_color = GREEN).add_tip()
        Q_minus_P_name = MathTex("\\vec{Q}-\\vec{P}").next_to(vect_Q_minus_P, RIGHT, buff=.1).set_color(GREEN)
        self.play(GrowFromPoint(vect_Q_minus_P, point = vect_Q_minus_P.get_start()),
                  Write(Q_minus_P_name), run_time = .5)
