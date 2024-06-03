mkdir -p results
mkdir -p results/dane_2D/
mkdir -p results/dane_2D/no_clusters

num_dirs=8
for i in $(seq 1 $num_dirs); do
    dir_name="results/dane_2D/no_clusters/$i"
    mkdir -p "$dir_name"
    python3 src/no_clusters.py --set=$i --dir="$dir_name" &
done