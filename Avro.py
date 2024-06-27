import fastavro

# Load your Avro schema
schema_path = 'schema.avsc'
with open(schema_path, 'r') as schema_file:
    schema = schema_file.read()

# Open your Avro file for validation
avro_file_path = 'data.avro'
with open(avro_file_path, 'rb') as avro_file:
    reader = fastavro.reader(avro_file, reader_schema=schema)

    # Iterate over records (if needed)
    for record in reader:
        # Do something with the validated record
        print(record)

print("Avro file validation against schema is successful.")
