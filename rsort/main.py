import difflib
import os
from pathlib import Path
from typing import List, Optional

from typer import Exit, Option, Typer, echo

from rsort import __version__
from rsort.requirements import Requirements

app = Typer(invoke_without_command=True, help="Sort requirements with ease!")


def version_callback(value: bool):
    if value:
        echo(f"Awesome CLI Version: {__version__}")
        raise Exit()


@app.callback()
def sort(
    files: Optional[List[str]] = Option(None, help="Requirements file to be sorted"),
    check: bool = Option(False, "--check", help="Only check if needs to be sorted"),
    diff: bool = Option(False, "--diff", help="Only changes to be made"),
    version: bool = Option(None, "--version", callback=version_callback, is_eager=True),
):
    files = files or ["requirements.txt", "pyproject.toml"]
    need_format = []
    for path in files:
        if not Path(path).exists():
            continue
        with open(path, "r") as f:
            requirements = Requirements(f)
            original = requirements.content
            modified = requirements.sort()

        if original != modified:
            need_format.append(path)
            if diff:
                echo(
                    "".join(
                        difflib.unified_diff(
                            original.splitlines(True),
                            modified.splitlines(True),
                            fromfile=os.path.relpath(path),
                            tofile=os.path.relpath(path),
                        )
                    ),
                    err=True,
                )

            if not (check or diff):
                with open(path, "w") as f:
                    f.write(modified)
    if need_format:
        if check:
            echo(f"{len(need_format)} to be sorted:", err=True)
            for file in need_format:
                echo(f"- {file}", err=True)
            raise Exit(1)
