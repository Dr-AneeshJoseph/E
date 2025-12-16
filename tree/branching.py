class TreeManager:
    """
    Implements Loop 3: Tree of Thoughts Branching & Pruning.
    """
    
    def prune_branches(self, hypotheses: list, keep_top_n=2):
        """
        Kills weak ideas. Only the top N survive.
        """
        # Sort by score (Highest first)
        sorted_branches = sorted(hypotheses, key=lambda x: x['initial_score'], reverse=True)
        
        survivors = sorted_branches[:keep_top_n]
        graveyard = sorted_branches[keep_top_n:]
        
        return {
            "survivors": survivors,
            "graveyard_count": len(graveyard),
            "graveyard_examples": [g['hypothesis'] for g in graveyard]
        }
      
