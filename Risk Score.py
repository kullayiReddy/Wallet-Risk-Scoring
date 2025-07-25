from sklearn.preprocessing import MinMaxScaler
from FeatureCalculation import scores_df
# Step A: Normalize each feature to 0–1
scaler = MinMaxScaler()

scores_df[["borrow_ratio_scaled", "supplied_scaled", "tokens_scaled"]] = scaler.fit_transform(
    scores_df[["borrow_ratio", "total_supplied", "token_count"]]
)

# Step B: Recalculate weighted score
scores_df["weighted_score"] = (
    0.5 * scores_df["borrow_ratio_scaled"] +
    0.3 * scores_df["supplied_scaled"] +
    0.2 * scores_df["tokens_scaled"]
)

# Step C: Scale final score to 0–1000
scores_df["score"] = MinMaxScaler(feature_range=(0, 1000)).fit_transform(scores_df[["weighted_score"]])

print("\nFinal scores:")
scores_df[["wallet_id", "score"]].to_csv("wallet_risk_scores.csv", index=False)
