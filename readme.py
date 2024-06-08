class Developer:
    def __init__(self):
        self.info = "Full stack? Maybe some day."
        self.pronouns = "he/him"
        self.learning_languages = ["Python", "JavaScript", "HTML", "CSS", "C"]
        self.areas = ["Web Development", "Game Development", "Cybersecurity"]

if __name__ == "__main__":
    developer = Developer()

    print(developer.info)
    print(f"Pronouns: {developer.pronouns}")
    print(f"Languages I'm learning: {', '.join(developer.learning_languages)}")
    print(f"Areas: {', '.join(developer.areas)}")

    # ... I love Python :)