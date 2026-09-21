# Methodology

## Data preparation

Ratings were parsed from MovieLens's `UserID::MovieID::Rating::Timestamp` format using pandas. Movie metadata was parsed from `MovieID::Title::Genres`. A user-by-movie matrix was created with missing ratings represented as `NaN`.

The verified data dimensions are 1,000,209 ratings, 6,040 users, 3,883 movie metadata rows, and 3,706 movies with at least one rating.

## Experiment 1: user neighbourhoods

A NumPy random generator with seed 7 selected one user from those with at least 50 ratings. The selected user was user 5717 with 384 ratings.

Similarity was calculated only on co-rated movies:

- cosine similarity on raw ratings;
- Pearson similarity by centring each overlapping rating vector on its overlap mean; and
- MSD similarity, `1 / (1 + mean_squared_difference)`.

Only positive similarities contributed to prediction. Pearson predictions used neighbour deviations from each neighbour's overall mean and added the target user's mean. Cosine and MSD used similarity-weighted ratings. Missing-neighbour cases fell back to the item mean, and predictions were clipped to the 1–5 scale.

## Experiment 2: item and genre similarity

A NumPy random generator with seed 123 selected one movie from those with at least 500 ratings. The selected target was movie 25, *Leaving Las Vegas (1995)*, with 980 ratings.

Each user's mean rating was subtracted before item similarity was calculated. Candidate items with fewer than ten shared raters were assigned zero rating similarity. Otherwise, cosine similarity between centred vectors served as adjusted rating similarity. Negative rating similarities were clipped to zero.

Genres were converted to sets and compared by Jaccard similarity. The combined score used:

`alpha * positive_rating_similarity + (1 - alpha) * genre_jaccard`

The run tested alpha values 0, 0.25, 0.5, 0.75, and 1 with neighbourhood sizes 5, 10, 20, and 40.

## Experiment 3: biased matrix factorisation

Ten users were sampled with seed 42 from users with more than 100 ratings. Ten records per user were held out, preferentially ratings of four or five. The remaining 1,000,109 records were used for training.

The model predicted:

`global mean + user bias + item bias + dot(user factors, item factors)`

It used 32 latent dimensions, 20 epochs, learning rate 0.01, L2 regularisation 0.05, factor initialisation from `0.01 × N(0, 1)`, zero-initialised biases, and shuffled per-rating SGD. The same seed-42 NumPy generator that sampled the users also initialised the factors and shuffled each epoch; the holdout sample used pandas `random_state=42`. No specialised recommender-system or machine-learning library was used.

Training RMSE fell from 0.9510 to 0.8324 and was still decreasing at epoch 20, so the model was not trained to convergence.

For each evaluation user, all movies unseen in training were scored, and the top 20 formed the ranked recommendation list. The item-mean baseline ranked the same candidate pool by each item's training-set mean (items absent from training fall back to the global mean).

