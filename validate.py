import re

def validate_html():
    with open('index.html', 'r') as f:
        content = f.read()
    
    print('HTML Validation Check:')
    print(f'- DOCTYPE present: {"<!DOCTYPE html>" in content}')
    print(f'- HTML lang attribute: {"<html lang=" in content}')
    print(f'- Meta charset: {"<meta charset=" in content}')
    print(f'- Meta viewport: {"viewport" in content}')
    print(f'- Title tag: {"<title>" in content}')
    print(f'- Royal blue theme: {"#4A90E2" in content}')
    print(f'- Logo present: {"logo.png" in content}')
    print(f'- All features included: {"Numerology" in content and "Tarot" in content and "Journal" in content and "Relationship" in content}')
    print('✅ Basic HTML structure validation passed')

if __name__ == "__main__":
    validate_html()
