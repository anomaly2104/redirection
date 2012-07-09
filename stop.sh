ping_procs=`ps aux | grep "distribute_traffic.py" | awk '{print $2}'`
mong_procs=`ps aux | grep "ed89ec0d-3886-40d2-af1c-e96832f30784" | awk '{print $2}'`

for i in $ping_procs
do
	`sudo kill $i`	
done

for i in $mong_procs
do
	`sudo kill $i`	
done

