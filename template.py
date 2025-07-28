import os
from pathlib import Path

project_name = "aydie_genai"

list_of_files = [
    # Root directory files
    ".github/workflows/.gitkeep", # For GitHub Actions CI/CD
    
    # Main source directory
    f"{project_name}/__init__.py",
    f"{project_name}/genai.py",
    f"{project_name}/exceptions.py",
    f"{project_name}/utils.py",
    
    # Providers sub-package
    f"{project_name}/providers/__init__.py",
    f"{project_name}/providers/base_provider.py",
    f"{project_name}/providers/gemini_provider.py",
    f"{project_name}/providers/openai_provider.py",
    f"{project_name}/providers/claude_provider.py",
    f"{project_name}/providers/groq_provider.py",
    f"{project_name}/providers/deepseek_provider.py",
    f"{project_name}/providers/mistral_provider.py",

    # Other project files
    "tests/__init__.py",        
    "tests/test_genai.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]


print(f"--- Setting up project structure for: {project_name} ---")

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Created directory: {filedir} for the file: {filename}")
        
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            if filename == "__init__.py":
                f.write("This file makes the directory a Python package.\n")
            
            elif filename == "README.md":
                f.write(f"# {project_name}\n\nA unified library for generative AI models.\n")
            
            pass
        print(f"Created empty file: {filepath}")
        
    else:
        print(f"{filename} already exists. Skipping.")
        
print(f"--- Project setup complete for: {project_name} ---")