#!/usr/bin/env bash

if [ $# -lt 2 ]
then
    echo "Missing arguments"
    echo "Usage: ./add_uuid.sh <estc_number> <uuid>"
    echo "Example: ./add_uuid.sh T115764 6c150fe3-b5fe-47aa-9a7d-59b31d51ef45"
    echo "The UUID will be added to the column 'S' in the row matching this specific ESTC number."
    exit 1
fi

poetry run chewfiles --estc_number ${1} --uuid ${2}