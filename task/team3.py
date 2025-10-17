# Initial teams
teams = {"Lions": ("Faisal", "Rizwan"), "TIgers": ("Atif", "Rafi")}

# 1) Remove 'Rizwan' from the Lions tuple 
lions = teams['Lions']
remove_idx = lions.index('Rizwan')                    # find position of 'Rizwan'
lions_without_rizwan = lions[:remove_idx] + lions[remove_idx+1:]
teams['Lions'] = lions_without_rizwan

print("lions without rizwan", lions_without_rizwan)