from dominion.pathfinder import DominionPathfinder

pathfinder = DominionPathfinder()
task = "Identify the next breakthrough in consumer coffee machines."

# MOCK LLM OUTPUT (5 Divergent Ideas)
mock_llm_json = """
[
  {"id": 1, "hypothesis": "AI-Driven Barista (Personalized profiles)", "initial_score": 92},
  {"id": 2, "hypothesis": "Molecular Coffee Printer (No beans)", "initial_score": 60},
  {"id": 3, "hypothesis": "Hyper-Portable Nitro Cold Brew Capsule", "initial_score": 88},
  {"id": 4, "hypothesis": "Drone-Delivered Hot Coffee", "initial_score": 40},
  {"id": 5, "hypothesis": "Edible Coffee Cups", "initial_score": 55}
]
"""

report = pathfinder.explore_ambiguity(task, mock_llm_json)

print(f"--- DOMINION REPORT ---")
print(f"Task: {report['task']}")
print(f"Paths Explored: 5")
print(f"Paths Killed: {report['pruned_count']}")

print("\n[SURVIVING PATHS]")
for path in report['best_paths']:
    print(f"PATH {path['id']} ({path['initial_score']}): {path['hypothesis']}")

# EXPECTED OUTPUT:
# Surviving: Path 1 (AI) and Path 3 (Nitro).
# Killed: Path 2, 4, 5 (Scores < 88).

