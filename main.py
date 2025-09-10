from drum_machine.entities.pattern import DrumPatterns
from drum_machine.player import DrumMachinePlayer
from pgstudio.scene import SceneBase
from pgstudio.client import init_pygame, ClientPGS, ConfigClientPGS
from patterns.porcupine_tree import PorcupineTree


class DrumMachineScene(SceneBase):
    def __init__(self, *, name: str, drum_patterns: DrumPatterns):
        super().__init__(name=name)
        self.player = DrumMachinePlayer(drum_patterns=drum_patterns)

    def main(self) -> None:
        self.player.update()


def get_scenes():
    return {
        "drum_machine": DrumMachineScene(
            name="Drum Machine",
            drum_patterns=PorcupineTree.the_sound_of_the_muzak()
        )
    }


if __name__ == "__main__":
    init_pygame()
    cfg = ConfigClientPGS(app_name="BeatPy", resolution=(800, 600), fps=60)
    client = ClientPGS(cfg=cfg, scenes=get_scenes())
    client.main(first_scene="drum_machine")
