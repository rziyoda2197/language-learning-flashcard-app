import random

class VideoIdeaGenerator:
    def __init__(self):
        self.categories = {
            "tech": ["Python", "JavaScript", "React", "Angular", "Vue"],
            "gaming": ["Fortnite", "PlayerUnknown's Battlegrounds", "League of Legends", "Overwatch", "Call of Duty"],
            "travel": ["Paris", "Tokyo", "New York", "London", "Sydney"],
            "food": ["Pizza", "Sushi", "Tacos", "Burgers", "Salads"],
            "education": ["Python programming", "Data science", "Machine learning", "Web development", "Cybersecurity"]
        }

    def generate_idea(self):
        category = random.choice(list(self.categories.keys()))
        topic = random.choice(self.categories[category])
        return f"{category.capitalize()} video idea: {topic}"

generator = VideoIdeaGenerator()
print(generator.generate_idea())
```

```python
import random

class VideoIdeaGenerator:
    def __init__(self):
        self.categories = {
            "tech": ["Python", "JavaScript", "React", "Angular", "Vue"],
            "gaming": ["Fortnite", "PlayerUnknown's Battlegrounds", "League of Legends", "Overwatch", "Call of Duty"],
            "travel": ["Paris", "Tokyo", "New York", "London", "Sydney"],
            "food": ["Pizza", "Sushi", "Tacos", "Burgers", "Salads"],
            "education": ["Python programming", "Data science", "Machine learning", "Web development", "Cybersecurity"]
        }

    def generate_idea(self):
        category = random.choice(list(self.categories.keys()))
        topic = random.choice(self.categories[category])
        return f"{category.capitalize()} video idea: {topic}"

generator = VideoIdeaGenerator()
print(generator.generate_idea())
