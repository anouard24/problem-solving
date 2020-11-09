<?php 
        // problem name: Lineland Mail
        // date:         21/01/2018

        fscanf(STDIN,"%d\n",$len);$len--;
	$n=explode(" ",fgets(STDIN));
	for($i=0;$i<$len+1;$i++)$x[$i]=intval($n[$i]);
	echo abs($x[0]-$x[1])." ".abs($x[$len]-$x[0])."\n";
	for($i=1;$i<$len;$i++) echo min(abs($x[$i-1]-$x[$i]),abs($x[$i+1]-$x[$i]))
		." ".max(abs($x[0]-$x[$i]),abs($x[$len]-$x[$i]))."\n";
	echo abs($x[$len]-$x[$len-1])." ".abs($x[$len]-$x[0])."\n";
?>

