#!/bin/bash

export PYTHONPATH=/caravel:$PYTHONPATH

if [ ! -f /caravel/caravel.db ]; then
# Create an admin user
fabmanager create-admin --app caravel --username "$username" --password "$password" --firstname "$firstname" --lastname "$lastname" --email "$email"

# Initialize the database
caravel db upgrade

# Create default roles and permissions
caravel init

# Load some data to play with
caravel load_examples
fi

caravel runserver
