import re


# Technical skills used by the analyzer
SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",

    # Python/Data
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",

    # Machine Learning / AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "tensorflow",
    "pytorch",
    "scikit-learn",

    # Data Analytics / BI
    "power bi",
    "tableau",
    "excel",
    "data analysis",
    "data visualization",

    # Web Development
    "html",
    "css",
    "react",
    "node.js",
    "flask",
    "django",
    "streamlit",

    # Tools / Cloud
    "git",
    "github",
    "docker",
    "aws",
    "azure",

    # Concepts
    "rest api",
    "api",
    "statistics",
    "data structures",
    "algorithms",
    "oop",
]


def extract_skills(text):
    """
    Extract technical skills from text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Handle skills containing special characters
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(set(found_skills))