# Evaluation

## Ranking evaluation

The reported AP@20 and NDCG@20 values come from one deterministic split:

- eligibility: users with more than 100 ratings;
- sampled users: 10, without replacement, using NumPy seed 42;
- sampled IDs: 569, 590, 624, 1246, 2745, 2776, 4004, 4269, 4711, and 5225;
- holdout: 10 records per user, preferentially ratings >= 4;
- training size: 1,000,109 ratings;
- candidates: every movie not seen by that user in the training set;
- relevant set: the user's ten held-out movie IDs;
- aggregation: arithmetic mean across the ten users.

If a user had fewer than ten ratings >= 4, the original code would fill the holdout with the user's highest remaining ratings, breaking ties by earlier timestamp. A read-only check of the source data found that the ten selected users had 30–334 ratings >= 4, so the fallback did not run and all 100 held-out records were positive under the project's threshold.

AP@20 divides accumulated precision at hit positions by `min(number_of_relevant_items, 20)`. NDCG@20 uses binary relevance and logarithmic rank discount, normalised by the ideal DCG for the available relevant items.

### Verified aggregate results

| Method | AP@20 | NDCG@20 |
| --- | ---: | ---: |
| Item-mean baseline | 0.0006666667 | 0.0055022942 |
| Biased matrix factorisation | 0.0216033019 | 0.0774080886 |

The NDCG ratio is `0.0774080886 / 0.0055022942 = 14.0683`. This comparison is valid only for this fixed split and candidate construction.

### Hits behind the averages

The per-user values in `results/ranking_by_user.csv` can be decoded into hit positions (with ten relevant items, each hit at rank k adds `1 / log2(k + 1)` to DCG):

| User | Baseline hit ranks | MF hit ranks |
| ---: | --- | --- |
| 624 | – | 4, 14 |
| 1246 | 15 | 12 |
| 2776 | – | 3, 9 |
| 4269 | – | 15 |
| 4711 | – | 5, 7, 12, 17 |
| 5225 | – | 11 |
| 569, 590, 2745, 4004 | – | – |

A separate re-run of the ranking experiment from the raw MovieLens files (same seeds and call order, run outside this repository) reproduced the ten sampled users, the 1,000,109-row training set, all 20 printed training RMSE values, and both AP@20/NDCG@20 pairs to at least 13 decimal places.

In total the baseline recovered 1 of the 100 held-out items and MF recovered 11. Four users had no hits under either method. The ratio above is therefore driven by very small counts.

## Rating-prediction diagnostics

The original notebook also reports RMSE for two neighbourhood experiments. These ratings were not held out before similarities were constructed, so the results are in-sample diagnostics and not unbiased generalisation estimates.

Where the leakage enters:

- **User-based kNN.** Every movie the test user rated is scored, but the user-user similarities were computed over all of that user's ratings, including the one being predicted. The Pearson prediction also adds back the user's mean, which includes the target rating.
- **Item-based and hybrid.** Rating similarity between the target movie and every other movie was computed from centred vectors that contain all 980 target ratings, i.e. the values later predicted. User means used for centring and in the prediction also include the target rating.
- **Selection.** The best similarity, k and alpha were picked by comparing RMSE on these same ratings.

The size and direction of the bias were not measured, and it may differ between similarity measures. These RMSEs are not estimates of prediction error on unseen ratings, and the comparisons between configurations are indicative only.

### User-based kNN

One sampled user (5717) and all 384 movies rated by that user were evaluated. Best recorded RMSE: Pearson similarity with k=10, 0.638941.

### Item and genre similarity

One target movie (movie 25) and its 980 raters were evaluated. Best rating-only result: k=10, RMSE 0.924768. Best setting with genre contribution (`alpha < 1`) was alpha=0.75 and k=10, RMSE 0.971694.

Because the target ratings contributed to the similarity matrix, neither number should be presented as test-set performance.
