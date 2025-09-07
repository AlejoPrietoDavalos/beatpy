import pygame

from drum_machine.player import DrumMachinePlayer
from drum_machine.entities.pattern import DrumPattern

BLACK = (0, 0, 0)


class DrumMachineUI:
    """Encapsula el loop de pygame y la visualización."""

    def __init__(self, player: DrumMachinePlayer):
        self.player = player
        self.running = True
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 200

        pygame.init()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Drum Machine")
        self.clock = pygame.time.Clock()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self) -> None:
        self.screen.fill(BLACK)
        step = self.player.step
        pygame.draw.rect(
            self.screen,
            (0, 200, 0),
            pygame.Rect(20 + (step * 15), 80, 10, 10)
        )
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.player.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
