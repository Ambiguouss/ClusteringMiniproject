mkdir -p results
mkdir -p results/dane_2D/
mkdir -p results/dane_2D/acc

num_dirs=8
for i in $(seq 1 $num_dirs); do
    dir_name="results/dane_2D/acc/$i"
    mkdir -p "$dir_name"
    python3 src/main.py --model=Hierarchical --link=single --set=$i --dir="$dir_name" > results/dane_2D/acc/$i/single.txt &
    python3 src/main.py --model=Hierarchical --link=Ward --set=$i --dir="$dir_name" > results/dane_2D/acc/$i/Ward.txt &
    python3 src/main.py --model=K-means --iter=30 --set=$i --dir="$dir_name" > results/dane_2D/acc/$i/kmeans.txt &
    python3 src/main.py --model=Spectral --graph_type=full --set=$i --dir="$dir_name" > results/dane_2D/acc/$i/specfull.txt &
    python3 src/main.py --model=Spectral --graph_type=epsi --eps=5 --set=$i --dir="$dir_name" > results/dane_2D/acc/$i/speceps.txt &
done