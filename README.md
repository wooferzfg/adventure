# Adventure

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/wooferzfg/adventure/main.svg)](https://results.pre-commit.ci/latest/github/wooferzfg/adventure/main) [![Build Status](https://github.com/wooferzfg/adventure/workflows/Render%20video/badge.svg)](https://github.com/wooferzfg/adventure/actions)

[Watch the Video](https://drive.google.com/file/d/1iJS4TJbPBRrE8XmbwaIRFkGORYoogUVW/view?usp=drivesdk)

## Build Instructions

1. [Install poetry](https://python-poetry.org/docs/)
2. [Install dependencies for Manim](https://docs.manim.community/en/stable/installation.html)
3. Install dependencies: `poetry install`
4. Activate virtual environment: `poetry shell`
5. Render: `manim -p scene.py -q h AllScenes`
