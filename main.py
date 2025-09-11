from dotenv import load_dotenv
from pgstudio.client import init_pygame, ClientPGS, ConfigClientPGS
from patterns.porcupine_tree import PorcupineTree
from scenes.drum_machine import DrumMachineScene
from configure_logging import configure_logging

load_dotenv()
configure_logging()


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
