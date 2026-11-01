def max_score_name(scores):
    best_score = -1
    best_name = None

    for name,score in scores.items():
        if score > best_score:
            best_score = score
            best_name = name

    return best_name
scores = {"小明": 88, "小红": 95, "小刚": 70}
print(max_score_name(scores))