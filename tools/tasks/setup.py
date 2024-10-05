#!/usr/bin/env python3

# Set's up python virtual env with dependencies for use in other tasks.
# Also check's if environment looks valid.

import os

from common import c, gen_tasks_path, tasks_path

venv_path = os.path.join(gen_tasks_path, 'venv')


def main():
    if not os.path.exists(venv_path):
        c(f'python3 -m venv {venv_path}')

    c(f". {os.path.join(gen_tasks_path, 'venv/bin/activate')} && pip install -r {os.path.join(tasks_path, 'requirements.txt')}")


if __name__ == '__main__':
    raise SystemExit(main())
