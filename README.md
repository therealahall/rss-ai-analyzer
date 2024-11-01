# RSS analyzer utilizing AI and ML
![Workflow](https://github.com/therealahall/rss-ai-analyzer/actions/workflows/test.yml/badge.svg)

I wanted to get a better understanding of how to leverage technology such as AI and ML and broaden my understanding of Python at the same time, hence this project. The idea is that I want to be able to pass in an RSS feed of some sort, have it identify commonalities across the feed and then, leveraging AI, give me a brief summary of the content the website provides.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository
```bash
git clone https://github.com/therealahall/rss-ai-analyzer
```
2. Install dependencies
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
3. Build docker containers
```bash
docker compose build
```

## Usage
To run the project, run
```bash
python src/app.py https://www.example.org/rss.xml
```

## Testing
Its best to run testing inside of docker itself
```bash
docker compose run --rm test
```

## Contributing
Since this is a project that I'm using to learn, I am not accepting contributions of Pull Requests at this time

## License
See [COPYING](./COPYING) for full license
```monospace
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.
```
