import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'p2b.py':
            continue
        new_name = file.replace('pika', 'bilby').replace('Pika', 'Bilby').replace('PIKA', 'BILBY')
        if new_name != file:
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'p2b.py':
            continue
        path = os.path.join(root, file)
        with open(path, 'r') as f:
            print(path)
            content = f.read()
            new_content = content.replace('pika', 'bilby').replace('Pika', 'Bilby').replace('PIKA', 'BILBY')
        with open(path, 'w') as f:
            f.write(new_content)
