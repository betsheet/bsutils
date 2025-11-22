# BSUtils

Betsheet utilities package - A collection of utility classes and helpers for sports betting automation.

## Description

`bsutils` is a Python library that provides common utilities and data models for sports betting applications. It includes tools for managing bets, picks, bookmakers, users, database operations, logging, and fuzzy string matching.

## Features

- **Base Models**: Pydantic-based entities with MongoDB integration
- **Bet Management**: Data models for bet tracking and placement
- **Pick Models**: Structures for managing betting picks from multiple sources
- **Bookie Support**: Enumeration and credentials management for multiple bookmakers
- **User Management**: User and credentials models
- **Database**: MongoDB client wrapper for easy database operations
- **Logging**: Loguru-based logging with file rotation and compression
- **Fuzzy Matching**: String similarity tools for matching team names and events
- **Configuration**: JSON-based configuration loader

## Installation

### From GitHub

```bash
pip install git+https://github.com/betsheet/bsutils.git
```

### For development

```bash
git clone https://github.com/betsheet/bsutils.git
cd bsutils
pip install -e ".[dev]"
```

## Requirements

- Python >= 3.10
- pydantic >= 2.0.0
- pymongo >= 4.0.0
- loguru >= 0.7.0
- thefuzz >= 0.20.0
- typing-extensions >= 4.0.0

## Modules

### `base`
Base entity classes with Pydantic models and MongoDB ObjectId support.

### `bet`
Bet tracking and management with error handling.

### `pick`
Pick models supporting multiple sources (Betaminic, OddsNotifier, etc.) and sports.

### `bookie`
Bookmaker enumeration and credential management.

### `user`
User and authentication models.

### `database`
MongoDB client wrapper with common CRUD operations.

### `logger`
Configured Loguru logger with file rotation and multiple output streams.

### `fuzz`
Fuzzy string matching utilities for comparing team names and event participants.

### `config`
JSON configuration file loader.

### `utilities`
General utility functions including project root path detection.

## Usage Example

```python
from bsutils.bet.bet import Bet
from bsutils.bookie.bsbookie import BSBookieEnum
from bsutils.pick.pick import Pick
from bsutils.pick.util import BSSelection, BSMarketEnum, BSSelectionOptionEnum
from bsutils.logger.bslogger import BSLogger
from bsutils.database.bsmongo import BSMongo

# Initialize logger
logger = BSLogger("app.log", debug=True)
logger.info("Application started")

# Create a pick
pick = Pick(
    sport="Soccer",
    participants=["Real Madrid", "Barcelona"],
    selection=BSSelection(
        market=BSMarketEnum.RESULT,
        option=BSSelectionOptionEnum.HOME,
        value=None
    ),
    min_odds=2.5,
    stake_units=1.0
)

# Create a bet
bet = Bet(
    pick_id="507f1f77bcf86cd799439011",
    user_id="507f1f77bcf86cd799439012",
    bookie=BSBookieEnum.BET_365,
    stake=10.0
)

# Database operations
db = BSMongo("mongodb://localhost:27017", "betsheet")
db.insert_one("bets", bet.as_json())
```

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Format code:

```bash
black .
```

Type checking:

```bash
mypy .
```

## License

MIT

## Authors

BetSheet - betsheet@protonmail.com

## Repository

https://github.com/betsheet/bsutils
