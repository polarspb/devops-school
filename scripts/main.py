from datetime import datetime

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
text = github.event.inputs.text1

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')
    f.write(f'# {text}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
