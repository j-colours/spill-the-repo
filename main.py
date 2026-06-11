#!/usr/bin/env python3

# Author: jcolours
# Date: 2026-06-11
# Description: ...

import click
import requests
import subprocess
from console import console


def main():
    codeberg = requests.get(
        "https://codeberg.org/api/v1/repos/j-colours/spill-the-repo",
    ).json()

    codeberg_search = requests.get(
        "https://codeberg.org/api/v1/repos/search?q=spill-the-repo"
    ).json()

    console.print(f"[yellow]Username Known Repo: {codeberg['owner']['login']}\n")
    console.print(f"[red]Search Repo: {codeberg_search['data'][0]['owner']['login']}")


if __name__ == "__main__":
    main()
