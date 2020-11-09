<?php 
        // problem name: Oath of the Night's Watch
        // date:         21/01/2018

        fscanf(STDIN,"%d\n",$len);
	$input = fgets(STDIN);
	if ($len < 3) {
		echo "0";
	} else {
		$n=explode(" ",$input);
		for($i=0;$i<$len;$i++)$x[$i]=intval($n[$i]);
		$p = min($x);$g=max($x);$ns=0;
		for($i=0;$i<$len;$i++)
			if($x[$i]<$g AND $x[$i]>$p) $ns++;
		echo $ns;
	}
?>

