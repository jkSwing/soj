from enum import IntEnum, unique


@unique
class CheckerType(IntEnum):
    EXACTLY_SAME = 0
    DOUBLE = 1


@unique
class VerdictResult(IntEnum):
    AC = 0  # Accepted
    WA = 1  # Wrong Answer
    TLE = 1 << 1  # Time Limit Exceeded
    RE = 1 << 2  # Runtime Error
    MLE = 1 << 3  # Memory Limit Exceeded
    OLE = 1 << 4  # Output Limit Exceeded
    CE = 1 << 5  # Compile Error
    IE = 1 << 30  # Internal Error


@unique
class LanguageEnum(IntEnum):
    CPP = 1
    C = 2
    Java = 3
    Python2 = 4
    Python3 = 5
    Go = 6
    JavaScript = 7
