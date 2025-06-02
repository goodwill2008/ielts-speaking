import json
import random

def run_trainer():
    print("🎙️ Welcome to IELTS Speaking Trainer!")
    with open("data/questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    q = random.choice(questions)
    print(f"\n❓ Question: {q}")
    input("\nPress Enter to simulate answering... 🎤")
    print("\n✅ Answer recorded! (Simulation)\nGood job!")
