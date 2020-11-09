<?php 
        // problem name: Snacktower
        // date:         22/01/2018

        fscanf(STDIN,"%d\n",$len);
	$x=array_map('intval',explode(' ',fgets(STDIN)));
	$q=array_fill_keys((range(1,$len)),false);
	for($j=$s=$len,$i=0;$i<$len;$i++){
		if($x[$i]==$s){echo $s;
			for($j=$s-1;$j>0&&$q[$j];)echo " ".$j--;
			$s=$j;}
		else $q[$x[$i]]=true;
		if($j!=0) echo "\n";}
?>

