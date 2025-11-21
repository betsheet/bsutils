import pathlib


def get_project_root_path() -> str:
    current_path = pathlib.Path(__file__).resolve().parent
    for p in [current_path] + list(current_path.parents):
        if (p / ".git").exists():
            return str(p)
    raise Exception("Error getting project root directory")