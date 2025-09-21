from enum import Enum

class TargetLabel(Enum):
    COCA_COLA = 0
    SPRITE = 1
    BOTTLED_WATER = 2

TARGET_LABELS = {
    "可乐": TargetLabel.COCA_COLA,
    "雪碧": TargetLabel.SPRITE,
    "瓶装水": TargetLabel.BOTTLED_WATER
}