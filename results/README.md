# Results

This directory contains aggregate values transcribed from saved notebook outputs; no experiments were rerun.

- `metrics.csv` contains verified aggregate and best-configuration metrics.
- `user_knn_rmse.csv` contains every user-neighbourhood RMSE configuration.
- `item_hybrid_rmse.csv` contains every item/genre configuration.
- `ranking_by_user.csv` contains the saved per-user Top-20 metrics.
- `training_rmse.csv` contains the 20 printed matrix-factorisation training RMSE values (in-sample, rounded to four decimals as printed).
- `figures/model-comparison.svg` compares the two Top-20 ranking methods.
- `figures/training-rmse.svg` plots training RMSE per epoch.

Both SVG charts are generated from the CSV files by `python scripts/generate_figures.py`; no values are interpolated or added.

Neighbourhood RMSE results are in-sample diagnostics, not holdout performance.

