# Limitations

1. **Small ranking sample.** AP@20 and NDCG@20 are averaged over only ten sampled users.
2. **Single split.** The ranking comparison uses one seed and one holdout configuration; there is no cross-validation or repeated sampling.
3. **Few hits behind the headline ratio.** The item-mean baseline hit 1 of the 100 held-out items and MF hit 11. The 14.07× NDCG@20 ratio therefore depends on a single baseline hit and would move a lot with one more or one fewer.
4. **Holdout semantics.** The code can fill a holdout with lower ratings when a sampled user has fewer than ten ratings >= 4. This fallback did not run for the selected users, but the protocol itself is less robust than an explicit eligibility constraint.
5. **Neighbourhood leakage.** The user- and item-based RMSE experiments construct similarities using the same ratings later scored, so those values are exploratory rather than out-of-sample.
6. **Weak popularity baseline.** The item-mean baseline has no minimum-support threshold or shrinkage, so rarely rated movies with extreme means dominate its ranking.
7. **Offline-only evidence.** MovieLens ranking metrics do not measure user satisfaction, diversity, novelty, fairness, latency, or online business outcomes.
8. **No hyperparameter validation split.** Neighbourhood settings (similarity, k, alpha) were compared on the same samples they were scored on. For MF, an earlier configuration with 64 factors and 8 epochs was scored on the same ten-user holdout (NDCG@20 ≈ 0.0335) before the reported 32-factor, 20-epoch run, so the final configuration was not selected independently of the test users.
9. **Unknown-as-negative assumption.** Unrated candidate movies are treated as non-relevant even though their true relevance is unknown.
10. **Publication constraints.** The source is identifiable as coursework. The implementation is withheld until the institution's policy permits publication.
