import json

from drum_machine.entities.pattern import DrumPattern
from drum_machine.player import DrumMachinePlayer
from pgstudio.scene import SceneBase
from pgstudio.client import init_pygame, ClientPGS, ConfigClientPGS


def get_pattern(path: str) -> DrumPattern:
    with open(path, "r") as f:
        data = json.load(f)
    return DrumPattern(**data)


class DrumMachineScene(SceneBase):
    def __init__(self, *, name: str):
        super().__init__(name=name)
        self.pattern = get_pattern("porcupine_tree_the_sound_of_muzak.json")
        self.player = DrumMachinePlayer(pattern=self.pattern)

    def main(self) -> None:
        self.player.update()


def get_scenes():
    return {
        "drum_machine": DrumMachineScene(name="Drum Machine")
    }


if __name__ == "__main__":
    init_pygame()
    cfg = ConfigClientPGS(app_name="BeatPy", resolution=(800, 600), fps=60)
    client = ClientPGS(cfg=cfg, scenes=get_scenes())
    client.main(first_scene="drum_machine")
