from manim import Scene, Axes, Dot, PURPLE, RED_C, config, BLUE, RED, Create, Line, FadeOut, YELLOW


class LinearFunction(Scene):
    def __init__(self, X, y, wb: list):
        super().__init__()
        self.X = X
        self.y = y
        self.wb = wb

    def construct(self):
        # Créer un système d'axes
        ax = Axes(
            x_range=[-6, 8, 1],  # Plage pour l'axe x
            y_range=[0, 12, 1],  # Plage pour l'axe y
            axis_config={"color": BLUE},
        )

        ([w1, w2], b) = self.wb[0]
        start_x = -5
        end_x = 5
        start_point = ax.c2p(start_x, -(w1 * start_x + b) / w2)
        end_point = ax.c2p(end_x, -(w1 * end_x + b) / w2)
        line = Line(start_point, end_point, color=YELLOW)

        dots = []
        for i, (x, y_coord) in enumerate(self.X):
            color = PURPLE if self.y[i][0] == 0 else RED_C
            dot = Dot(ax.c2p(x, y_coord), color=color)
            dots.append(dot)
        self.add(*dots)

        self.play(Create(ax), Create(line))
        self.wait(.1)

        for ([w1_new, w2_new], b_new) in self.wb[1:]:
            new_start_point = ax.c2p(start_x, -(w1_new * start_x + b_new) / w2_new)
            new_end_point = ax.c2p(end_x, -(w1_new * end_x + b_new) / w2_new)

            self.play(line.animate.put_start_and_end_on(new_start_point, new_end_point))
            self.wait(.1)


if __name__ == '__main__':
    config.media_width = "75%"
    # scene = LinearFunction(X, y, list_wb)
    # scene.render()
