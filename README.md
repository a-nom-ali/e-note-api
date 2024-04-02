# e-note-api

A RESTful API for managing and suggesting emoji sequences, with AI-powered features for enhancing digital communication.

## Overview

The e-note-api is designed to facilitate the integration of emoji-based notation systems into various platforms, leveraging AI to suggest emoji sequences and manage user and team interactions.

## Features

- User authentication and registration.
- AI-powered suggestions for emoji sequences.
- CRUD operations for managing emoji sequences.
- Team and project management endpoints.
- Support for SQL databases with an initial setup for SQLite/MariaDB.
- Pagination and filtering for list endpoints.
- User/team-based access control for sequences.
- Enhanced search capabilities.

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional)

### Installation

Clone the repository:

```bash
git clone https://github.com/a-nom-ali/e-note-api.git
cd e-note-api
```

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory and add the necessary configurations as key-value pairs:

```env
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///your-database.db
```

### Running the Application

Run the Flask application:

```bash
flask run
```

The API should now be accessible at `http://localhost:5000`.

## Documentation

For more detailed API documentation, refer to the `docs` directory.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
