# Data Setup

The project uses the **MovieLens 1M Dataset** from GroupLens Research.

- Official page: https://grouplens.org/datasets/movielens/1m/
- Expected archive: `ml-1m.zip`
- Verified contents used by the original project: `ratings.dat` and `movies.dat`

The dataset's bundled terms state that it may not be redistributed without separate permission. It is therefore excluded from this repository.

To prepare a local copy:

1. Review the terms on the official page and in its `README.txt`.
2. Download `ml-1m.zip` from GroupLens.
3. Extract it so the local files are available under `data/ml-1m/`.

Expected local layout:

```text
data/
└── ml-1m/
    ├── movies.dat
    ├── ratings.dat
    ├── users.dat
    └── README.txt
```

The entire `data/ml-1m/` directory and dataset archives are ignored by Git.

