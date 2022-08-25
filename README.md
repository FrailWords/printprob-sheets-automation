## Before you run, download the client secret JSON

Download the `client_secret.json` file into the project root directory from Bridges2 node at the following location: 

```bash
/data/sheets-automation/client_credentials.json
```

## Usage

Run script:
```bash
./add_uuid.sh <estc_number> <uuid>
```

The UUID will be added to the column 'S' in the row matching this specific ESTC number.

E.g. 
```bash
./add_uuid.sh T115764 6c150fe3-b5fe-47aa-9a7d-59b31d51ef45"
```

