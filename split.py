import re

text = """Artificial Intelligence (AI) is transforming industries across the world. AI is used in healthcare. Many companies invest heavily in AI research. As AI continues to evolve, professionals with AI skills are in high demand."""

sentences = re.split(r"[.!?]+", text)
#sentences = [s for s in sentences if s.strip()]

words = re.split(r"\s+", text.strip())

print("Sentences:", sentences)
print("Total Sentences:", len(sentences))

print("\nWords:", words)
print("Total Words:", len(words))