# Limitations

1. **Small ranking sample.** AP@20 and NDCG@20 are averaged over only ten sampled users.
2. **Single split.** The ranking comparison uses one seed and one holdout configuration; there is no cross-validation or repeated sampling.
3. **Holdout semantics.** The code can fill a holdout with lower ratings when a sampled user has fewer than ten ratings >= 4. This fallback did not run for the selected users, but the protocol itself is less robust than an explicit eligibility constraint.
4. **Neighbourhood leakage.** The user- and item-based RMSE experiments construct similarities using the same ratings later scored, so those values are exploratory rather than out-of-sample.
5. **Popularity baseline behaviour.** Item means can favour rarely rated movies with extreme averages; the baseline has no minimum-support or shrinkage correction.
6. **Offline-only evidence.** MovieLens ranking metrics do not measure user satisfaction, diversity, novelty, fairness, latency, or online business outcomes.
7. **No hyperparameter validation split.** Recorded configurations were compared on the same evaluated samples.
8. **Publication constraints.** The source is identifiable as coursework. The implementation is withheld until the institution's policy permits publication.
9. **Unknown-as-negative assumption.** Unrated candidate movies are treated as non-relevant even though their true relevance is unknown.
10. **Weak popularity baseline.** The item-mean baseline has no minimum-support threshold or shrinkage, so rarely rated movies with extreme means can dominate its ranking.
