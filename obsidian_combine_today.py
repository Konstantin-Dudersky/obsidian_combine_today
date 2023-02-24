#!/usr/bin/python3

import datetime as dt
from dataclasses import dataclass, field
from pathlib import Path

# check this settings ----------------------------------------------------------

VAULTS: list[str] = [
    "/home/konstantin/documents/obsidian/obsidian-home",
    "/home/konstantin/documents/obsidian/obsidian-work",
]

TARGET_FILE: str = "/home/konstantin/desktop/today_tasks.md"

FOLDER_CALENDAR: str = "calendar"
NOTE_NAME_FORMAT = r"%Y-%m-%d.md"


# ------------------------------------------------------------------------------

ERROR_VAULT_NOT_EXIST: str = "Vault not exist, path: {path}"
NOTE_TEMPLATE = """# {vault_name}

{note_content}
"""


def check_path(path: Path) -> None:
    if not path.exists():
        raise ValueError(ERROR_VAULT_NOT_EXIST.format(path=path))


def create_today_note_name() -> str:
    today: dt.datetime = dt.datetime.now()
    return today.strftime(NOTE_NAME_FORMAT)


def read_note_from_vault(note_path: Path) -> str:
    try:
        check_path(note_path)
    except ValueError:
        return "*Заметка не создана*"
    with open(note_path, "r", encoding="utf8") as note:
        return note.read()


def concat_notes(notes: list[str]) -> str:
    return "\n\n".join(notes)


@dataclass
class Vault:
    vault_path: Path
    vault_name: str = field(init=False)
    calendar_path: Path = field(init=False)
    note_path: Path = field(init=False)
    note_content: str = field(init=False)

    def __post_init__(self):
        check_path(self.vault_path)
        self.vault_name = self.vault_path.name
        self.calendar_path = self.vault_path / FOLDER_CALENDAR
        check_path(self.calendar_path)
        self.note_path = self.calendar_path / create_today_note_name()
        self.note_content = NOTE_TEMPLATE.format(
            vault_name=self.vault_name,
            note_content=read_note_from_vault(self.note_path),
        )


def create_vaults(vaults_str: list[str]) -> list[Vault]:
    vault_paths: list[Path] = [Path(path) for path in vaults_str]
    return [Vault(vault_path=vault) for vault in vault_paths]


def main() -> None:
    vaults: list[Vault] = create_vaults(VAULTS)
    target_file_content = concat_notes([vault.note_content for vault in vaults])
    with open(TARGET_FILE, "w", encoding="utf8") as target_file:
        target_file.write(target_file_content)


if __name__ == "__main__":
    main()
