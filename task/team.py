# Initial teams
teams = {"Lions": ("Faisal", "Rizwan"),
         "TIgers": ("Atif", "Rafi")
         }

lions = teams['Lions']
remove_idx = lions.index('Rizwan')                    
lions_without_rizwan = lions[:remove_idx] + lions[remove_idx+1:]
teams['Lions'] = lions_without_rizwan
print("lions without rizwan", lions_without_rizwan)
teams['TIgers'] = teams['TIgers'] + ('Auun',)
teams = {'Lions': teams['TIgers'], 'TIgers': teams['Lions']}
print("teams after swap:", teams)


all_players = teams['Lions'] + teams['TIgers']
print("all_players (concatenated):", all_players)

unique_players = tuple(dict.fromkeys(all_players))
print("unique_players:", unique_players)

sorted_players = tuple(sorted(unique_players))
print("sorted_players:", sorted_players)


def roster_size(team_name):
    return len(teams[team_name])
team_by_size_desc = tuple(sorted(teams, key=roster_size, reverse=True))
print("team_by_size_desc:", team_by_size_desc)

