import os
import re
from collections import deque
from typing import List, Optional, TextIO


def _rotate_empty_lines(lines: List[str]) -> List[str]:
    deque_lines = deque(lines)
    deque_lines.rotate(-1 * lines.count(""))
    return list(deque_lines)


def _format_output(lines: List[str]) -> str:
    return "\n".join(lines) + "\n"


class Requirements:
    extension: Optional[str] = None

    def __new__(cls, file: TextIO):
        extension = os.path.splitext(file.name)[1]
        for subclass in cls.__subclasses__():
            if not hasattr(cls, "extension"):
                raise TypeError(
                    f"Class {subclass.__name__} should have 'extension' attr."
                )
            if subclass.extension == extension:
                return super().__new__(subclass)
        raise RuntimeError("Subclass for file extension not found.")

    def __init__(self, file: TextIO):
        self.file = file
        self.content = file.read()

    def sort(self) -> str:
        raise NotImplementedError


class TxtRequirements(Requirements):
    extension = ".txt"

    def sort(self) -> str:
        output = _rotate_empty_lines(sorted(self.content.splitlines()))
        return _format_output(output)


class TomlRequirements(Requirements):
    extension = ".toml"
    deps_re = r"\[.*-?dependencies\]"

    def sort(self) -> str:
        lines = self.content.splitlines()
        start_range = None
        for i, line in enumerate(lines.copy()):
            if re.match(r"\[.*\]", line) and start_range:
                lines[start_range:i] = sorted(lines[start_range:i])
                lines[start_range:i] = _rotate_empty_lines(lines[start_range:i])
                start_range = None
            if re.match(self.deps_re, line):
                start_range = i + 1
        return _format_output(lines)
