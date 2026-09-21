"""Regenerate portfolio charts from verified saved result files."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"


def model_comparison() -> None:
    metrics = pd.read_csv(RESULTS / "metrics.csv")
    ranking = metrics[metrics["experiment"] == "ranking"].copy()
    table = ranking.pivot(index="method", columns="metric", values="value")
    table = table.loc[["item_mean_baseline", "biased_matrix_factorisation"]]
    labels = ["Item-mean baseline", "Biased MF"]

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    colors = ["#94a3b8", "#2563eb"]
    for axis, metric in zip(axes, ["AP@20", "NDCG@20"]):
        values = table[metric].to_numpy()
        bars = axis.bar(labels, values, color=colors)
        axis.set_title(metric)
        axis.set_ylabel(metric)
        axis.grid(axis="y", alpha=0.25)
        axis.bar_label(bars, labels=[f"{value:.4f}" for value in values], padding=3)
    fig.suptitle("Top-20 ranking on the fixed 10-user holdout")
    fig.tight_layout()
    fig.savefig(FIGURES / "model-comparison.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def training_curve() -> None:
    training = pd.read_csv(RESULTS / "training_rmse.csv")
    fig, axis = plt.subplots(figsize=(7, 4))
    axis.plot(training["epoch"], training["training_rmse"], color="#2563eb", marker="o", markersize=3)
    axis.set_title("Biased matrix factorisation training convergence")
    axis.set_xlabel("Epoch")
    axis.set_ylabel("Training RMSE")
    axis.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "training-rmse.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    FIGURES.mkdir(parents=True, exist_ok=True)
    model_comparison()
    training_curve()

