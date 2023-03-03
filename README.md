# robusta-playbook
[tool.poetry]
name = "robusta_playbooks"
version = "0.0.1"
description = ""
authors = ["Arik Alon <arikalon1@users.noreply.github.com>"]

[tool.black]
line-length = 120
target-version = ['py37']

[tool.isort]
line_length = 120
multi_line_output = 3
include_trailing_comma = true

[tool.poetry.dependencies]
python = "^3.7.1"
CairoSVG = "^2.5.2"
Flask = "^2.0.2"
prometheus-api-client = "^0.4.2"
pygal = "^3.0.0"
tinycss = "^0.4"
cssselect = "^1.1.0"
rsa = "^4.8"
humanize = "^3.13.1"

[tool.poetry.dev-dependencies]
robusta-cli = "^0.8.9"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"