import os
import django
import random

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Matching_Portal.settings")
django.setup()

from accounts.serializers import RegisterSerializer

names = [
    "Alice Smith","Bob Johnson","Charlie Brown","David Lee","Emma Wilson",
    "Frank Miller","Grace Taylor","Henry Anderson","Ivy Thomas","Jack White",
    "Karen Martin","Leo Harris","Mia Clark","Noah Lewis","Olivia Young",
    "Paul Walker","Quinn Hall","Ryan Allen","Sophia King","Tom Scott"
]

institutions = [
    "MIT","Stanford University","Carnegie Mellon","IIT Bombay","IIT Delhi",
    "Oxford University","Cambridge University","ETH Zurich","NUS Singapore","Tsinghua University"
]

domains = [
    "Machine Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Information Retrieval",
    "Databases",
    "Distributed Systems",
    "Artificial Intelligence"
]

keywords = [
    "deep learning","transformers","graph neural networks","vector search",
    "retrieval systems","data mining","reinforcement learning","large language models"
]

for i in range(50):
    data = {
        "email": f"reviewer{i}@test.com",
        "password": "StrongPass123!",
        "name": random.choice(names),
        "institution": random.choice(institutions),
        "department": random.choice(domains),
        "academic_position": random.choice([
            "Professor","Associate Professor","Assistant Professor","Research Scientist"
        ]),
        "research_interests": random.sample(keywords, 3)
    }

    serializer = RegisterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        print("Created:", data["email"])
    else:
        print("Error:", serializer.errors)