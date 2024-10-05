from __future__ import annotations

import os
import subprocess

ws = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../../'
))

gen_tasks_path = os.path.join(ws, '_generated/tools/tasks')
tasks_path = os.path.join(ws, 'tools/tasks')
venv_path = os.path.join(gen_tasks_path, 'venv')

def c(command: str | list[str], cwd=None, env=None) -> None:
    subprocess.check_call(command, shell=True, cwd=cwd, env=env, text=True)
