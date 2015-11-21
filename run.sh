#!/bin/bash

if [ ! -f /panoramix/panoramix.db ]; then
# Create an admin user
fabmanager create-admin --app panoramix --username "$username" --password "$password" --firstname "$firstname" --lastname "$lastname" --email "$email"

# Initialize the database
panoramix db upgrade

# Create default roles and permissions
panoramix init
fi

export PYTHONPATH=/panoramix:$PYTHONPATH
panoramix runserver