# SCORBOT API
### Initial python api for scorbot.com tournaments and teams registrations


### Installation

```bash
    git clone git@github.com:yarel2l/sbt_api_python.git
```

### Create virtual environment

```bash
    python3 -m venv venv
```

### Activate virtual environment

```bash
    source venv/bin/activate
```

### Install dependencies

```bash
    pip install -r modules/requirements.txt
```

### Migration

```bash
    python modules/manage.py migrate
```

### Create superuser

```bash
    python modules/manage.py createsuperuser
```

### Usage

```bash
    python modules/manage.py runserver
```

### Open browser

```bash
    http://localhost:8000
```
