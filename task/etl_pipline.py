# --- Raw dataset ---
raw_reviews = [
    {'source': 'web', 'payload': {'product_id': 'P1001',
    'user_id': 'U100', 'rating': 5, 'verified_purchase': True}},

    {'source': 'mobile', 'payload': {'product_id': 'P1001',
    'user_id': 'U101', 'rating': 4, 'verified_purchase': False}},

    {'source': 'third_party', 'payload': {'product_id': 'P1002',
    'user_id': 'U102', 'rating': 2, 'verified_purchase': True}},
]

# --- Extract step ---
r1 = raw_reviews[0]['payload']
r2 = raw_reviews[1]['payload']
r3 = raw_reviews[2]['payload']

# --- Transform step: filter only verified purchases ---
verified1 = r1 if r1['verified_purchase'] else None
verified2 = r2 if r2['verified_purchase'] else None
verified3 = r3 if r3['verified_purchase'] else None

# Keep only non-None verified reviews
final_reviews = [verified1, verified3]  # verified2 is None

# --- Transform step: calculate average ratings ---
# For P1001
p1_rating = verified1['rating']
p1_avg = p1_rating / 1   # only one verified rating

# For P1002
p2_rating = verified3['rating']
p2_avg = p2_rating / 1   # only one verified rating

# --- Transform step: classify based on rules ---
def classify(avg):
    if avg >= 4.5:
        return "Excellent"
    elif avg >= 3.5:
        return "Good"
    else:
        return "Poor"

p1_class = classify(p1_avg)
p2_class = classify(p2_avg)

# --- Load step: store results in dictionary ---
results = {
    'P1001': {'average_rating': p1_avg, 'classification': p1_class},
    'P1002': {'average_rating': p2_avg, 'classification': p2_class}
}

print(results)
