from enum import Enum as enum


class Status(enum):
    WAITING = "WAITING"
    CANCELED = "CANCELED"
    OUT = "OUT"
    DONE = "DONE"