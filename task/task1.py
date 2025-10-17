# Initial teams
teams = {"Lions": ("Faisal", "Rizwan"), "TIgers": ("Atif", "Salman")}

# 1) (No 'Sara' here, so we just keep Lions as is — nothing to remove)

# 2) Add new name 'Fasii' to the TIgers tuple
teams["TIgers"] = teams["TIgers"] + ("Fasii",)

# 3) Swap team names (keys) without retyping player lists
teams = {"Lions": teams["TIgers"], "TIgers": teams["Lions"]}

# 4) Concatenate the two team tuples into one tuple (may include duplicates)
all_players = teams["Lions"] + teams["TIgers"]

# 5) Create unique_players as a tuple with duplicates removed (order-preserving)
unique_players = tuple(dict.fromkeys(all_players))

# 6) Use sorted() to create tuple sorted_players (alphabetical)
sorted_players = tuple(sorted(unique_players))

# 7) Function to return team roster size
def roster_size(team_name):
    return len(teams[team_name])

team_by_size_desc = tuple(sorted(teams, key=roster_size, reverse=True))

# Print results
print("teams after swap:", teams)
print("all_players (concatenated):", all_players)
print("unique_players:", unique_players)
print("sorted_players:", sorted_players)
print("team_by_size_desc:", team_by_size_desc)
