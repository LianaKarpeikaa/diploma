from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def as_list(cls):
        return [item.value for item in cls]


class PetStatus(Enum):
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'

    def __str__(self) -> str:
        return str.__str__(self)


