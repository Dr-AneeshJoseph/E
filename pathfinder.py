import os
import json
from .tree.branching import TreeManager

class DominionPathfinder:
    def __init__(self):
        self.tree = TreeManager()
        
        # Load Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'tot_kernel.md')
        with open(prompt_path, 'r') as f:
            self.base_prompt = f.read()

    def explore_ambiguity(self, task: str, raw_llm_json: str):
        """
        Takes the LLM's divergent thoughts and prunes them.
        """
        try:
            # 1. Parse Branches
            hypotheses = json.loads(raw_llm_json)
            
            # 2. Prune (Keep top 2)
            result = self.tree.prune_branches(hypotheses, keep_top_n=2)
            
            return {
                "status": "DIVERGENCE_COMPLETE",
                "task": task,
                "best_paths": result['survivors'],
                "pruned_count": result['graveyard_count']
            }
        except Exception as e:
            return {"error": str(e)}

    def construct_prompt(self, task: str):
        return self.base_prompt.replace("[USER_TASK]", task)
      
