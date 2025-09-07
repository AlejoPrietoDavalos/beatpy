import pygame as pg

DEFAULT_FPS = 60

class Clock:
    _instance = None
    FPS_ALLOWED = frozenset({30, 60})
    fps: int = None
    pgclock = pg.time.Clock()

    def __new__(cls, fps: int = DEFAULT_FPS):
        cls.assert_fps(fps)
        if not isinstance(cls._instance, cls):
            cls._instance = super(Clock, cls).__new__(cls)
            cls.fps = fps
        return cls._instance

    def tick(self) -> int:
        """ TODO: Esto retorna el número de ns que tardó en ejecutar?"""
        return self.pgclock.tick(self.fps)
    
    @classmethod
    def assert_fps(cls, fps: int) -> None:
        assert fps in cls.FPS_ALLOWED, f"fps inválido: {fps}"
