# Results

This directory contains aggregate values transcribed from saved notebook outputs; no experiments were rerun.

- `metrics.csv` contains verified aggregate and best-configuration metrics.
- `user_knn_rmse.csv` contains every user-neighbourhood RMSE configuration.
- `item_hybrid_rmse.csv` contains every item/genre configuration.
- `ranking_by_user.csv` contains the saved per-user Top-20 metrics.
- `training_rmse.csv` contains the 20 printed matrix-factorisation training RMSE values.
- `figures/model-comparison.svg` compares the two Top-20 ranking methods.
- `figures/training-rmse.svg` visualises recorded training convergence.

The checked-in SVG charts are dependency-free renderings of the CSV values. PNG versions can be regenerated with `python scripts/generate_figures.py` after installing the requirements.

Neighbourhood RMSE results are in-sample diagnostics, not holdout performance.

