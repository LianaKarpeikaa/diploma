# from enum import Enum
#
#
# class BaseEnum(Enum):
#
#     @classmethod
#     def as_list(cls):
#         return [item.value for item in cls]
#
# 
# class Status(str, BaseEnum):
#     """
#     Status of [ets
#     """
#     Available: str = "available"
#     NotAvailable: str = "not-available"
#
#     def __str__(self) -> str:
#         return str.__str__(self)
#
#
