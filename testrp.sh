mkdir results
mkdir results/rpdata/
mkdir results/rpdata/Hierarchical
mkdir results/rpdata/K_means
mkdir results/rpdata/Spectral


python3 src/main.py --model=Hierarchical --clusters=2 --link=single > results/rpdata/Hierarchical/single &
python3 src/main.py --model=Hierarchical --clusters=2 --link=complete > results/rpdata/Hierarchical/complete &
python3 src/main.py --model=Hierarchical --clusters=2 --link=average > results/rpdata/Hierarchical/average &
python3 src/main.py --model=Hierarchical --clusters=2 --link=centroid > results/rpdata/Hierarchical/centroid &
python3 src/main.py --model=Hierarchical --clusters=2 --link=Ward > results/rpdata/Hierarchical/Ward &

python3 src/main.py --model=K-means --clusters=2 --iter=10 --eps=0.0001 > results/rpdata/K_means/I10e0001 &
python3 src/main.py --model=K-means --clusters=2 --iter=10 --eps=0.1 > results/rpdata/K_means/I10e1 &
python3 src/main.py --model=K-means --clusters=2 --iter=30 --eps=0.0001 > results/rpdata/K_means/I30e0001 &
python3 src/main.py --model=K-means --clusters=2 --iter=30 --eps=0.1 > results/rpdata/K_means/I30e1 &


python3 src/main.py --model=Spectral --clusters=2 --graph_type=full --weight=gauss  > results/rpdata/Spectral/fullgauss &
python3 src/main.py --model=Spectral --clusters=2 --graph_type=full   > results/rpdata/Spectral/full &
python3 src/main.py --model=Spectral --clusters=2 --graph_type=epsi --eps=10   > results/rpdata/Spectral/eps10 &
python3 src/main.py --model=Spectral --clusters=2 --graph_type=epsi --eps=30   > results/rpdata/Spectral/eps30 &
python3 src/main.py --model=Spectral --clusters=2 --graph_type=epsi --eps=10  --weight=gauss > results/rpdata/Spectral/eps10gauss &
python3 src/main.py --model=Spectral --clusters=2 --graph_type=epsi --eps=30  --weight=gauss > results/rpdata/Spectral/eps30gauss &