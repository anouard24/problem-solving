<?php 
        // problem name: Twins
        // date:         21/01/2018

        fscanf(STDIN,"%d\n",$len);
	$input = fgets(STDIN);
	if ($len < 2) {
		echo "1";
	} else {
		$n=explode(" ",$input);
		for($i=0;$i<$len;$i++) $x[$i]=intval($n[$i]);
		$moy=array_sum($x)/2;
		rsort($x);$sum=0;
		for($i=0;$i<$len;$i++){
			$sum+=$x[$i];
			if($sum>$moy) break;
		}
		echo $i+1;
	}
?>

