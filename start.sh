mkdir -p proc && sudo mount --bind /proc proc
m2sh load --config distribute_traffic.conf --db config.sqlite
m2sh start -config config.sqlite -name distribute_traffic -sudo

python distribute_traffic.py &
