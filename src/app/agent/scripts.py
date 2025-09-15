import subprocess
import sys


def dev_console() -> None:
    """Run dev console command."""
    result = subprocess.run([sys.executable, "-m", "app.agent.cli", "console"], check=False)
    sys.exit(result.returncode)


def dev_mode() -> None:
    """Run dev command."""
    result = subprocess.run([sys.executable, "-m", "app.agent.cli", "dev"], check=False)
    sys.exit(result.returncode)
