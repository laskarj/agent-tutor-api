import subprocess
import sys


def dev() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "uvicorn", "app.api.main:create_app", "--factory", "--reload", "--log-level", "debug"],
        check=False,
    )
    sys.exit(result.returncode)
