"""Run gh-space-shooter with a pink theme.

gh-space-shooter has no color options, but every color comes from
RenderContext.darkmode(). This script swaps that for a pink palette,
then runs the normal command line, so it takes the same arguments:

    python pink_space_shooter.py <username> --output game.gif --strategy random
"""

from gh_space_shooter.cli import app
from gh_space_shooter.game.render_context import RenderContext


def pink() -> RenderContext:
    return RenderContext(
        cell_size=12,
        cell_spacing=3,
        padding=40,
        background_color=(26, 15, 22),   # deep plum night sky
        grid_color=(46, 27, 38),         # empty days
        enemy_colors={                   # more contributions = brighter pink
            1: (122, 46, 72),
            2: (184, 69, 107),
            3: (251, 111, 146),
            4: (255, 179, 198),
        },
        ship_color=(255, 229, 236),      # blush white
        bullet_color=(255, 214, 165),    # peach, also used for explosions
    )


RenderContext.darkmode = staticmethod(pink)

if __name__ == "__main__":
    app()
