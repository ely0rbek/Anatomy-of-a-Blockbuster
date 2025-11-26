import pandas as pd
import ast
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("D:\python\Anatomy_of_Blockbuster\datasets\\movies_metadata.csv", low_memory=False)

# -------------------------
# 1. Clean & convert genres
# -------------------------
def extract_genres(genre_str):
    try:
        genre_list = ast.literal_eval(genre_str)
        return [g["name"] for g in genre_list]
    except:
        return []

df["genres_list"] = df["genres"].apply(extract_genres)

# --------------------------------
# 2. Select top 10 movies by rating
# --------------------------------
df = df[pd.to_numeric(df["vote_average"], errors="coerce").notnull()]
df["vote_average"] = df["vote_average"].astype(float)

top10 = df.sort_values("vote_average", ascending=False)

print("\nTop 10 Rated Movies:")
# print(top10[["title", "vote_average", "genres_list"]])

# ------------------------
# 3. Count genre frequency
# ------------------------
# Flatten list of genres
genre_counts = {}
for genres in top10["genres_list"]:
    for g in genres:
        genre_counts[g] = genre_counts.get(g, 0) + 1

genre_series = pd.Series(genre_counts).sort_values(ascending=False)

# ------------------------
# 4. Plot using matplotlib
# ------------------------
plt.figure(figsize=(10,6))
genre_series.plot(kind="bar")

plt.title("Genre Distribution of Rated Movies")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
