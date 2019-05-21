# text_colors version 0.8.3
[![Netlify Status](https://api.netlify.com/api/v1/badges/416b8ca3-82db-470f-9adf-a6d06264ca75/deploy-status)](https://app.netlify.com/sites/mystifying-keller-ab5658/deploys)  ![Azure DevOps builds](https://img.shields.io/azure-devops/build/skeptycal0275/skeptycal/1.svg?color=blue&label=Azure%20DevOps&style=popout) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask.svg?color=Yellow&label=Python&style=popout) ![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?label=%40skeptycal&style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?style=social)
Last update: 05-21-2019 | 11:49:05
---
## The obligatory Python training module to add CLI ANSI color and other escape code formatting features.
```bash

###############################################################################
# text_colors : The obligatory Python training module to add CLI ANSI color and other escape code formatting features. (version 0.8.3)
#
# author    - Michael Treanor  <skeptycal@gmail.com>
# copyright - 2019 (c) Michael Treanor
# license   - MIT <https://opensource.org/licenses/MIT>
# github    - https://www.github.com/skeptycal
#
# Usage: text_colors {demo|version|help}

#   Parameters:
#       demo, -d, --demo        -- examples of features
#       version, -v, --version  -- display version information
#       help, -h, --help        -- display usage and information

###############################################################################
#
# (There seems to be a tradition, in the spirit of 'Hello World,' to write some code that makes use of ANSI codes to color the CLI output. Since I have been working with BASH scripts, and now PHP / Python, it seems like a fun thing to do!)
#
# Importing this module gives access to the following:
#   - py_shell() - Returns string containing current python shell name.
#   - FG_DICT - dictionary of ANSI foreground color codes
#   - BG_DICT - dictionary of ANSI background color codes
#   - FLAGS_DICT - dictionary of ANSI formatting codes
#   - color_encode() - Returns encoded ANSI text string from components.
#   - color_print() - Print using ANSI color codes.
#   - color_gradient() - Print using a calculated ANSI color gradient.
#   - color_cycle() - Print by cycling through an ANSI color range.
###############################################################################




```
---
```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── bak
│   ├── README.md.bak
│   ├── codecov.yml.bak
│   ├── pipfile.bak
│   └── requirements.txt.bak
├── codecov.yml
├── requirements.txt
├── setup.py
└── text_colors.py

1 directory, 11 files
```
