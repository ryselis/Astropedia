<?php
error_reporting(0);
	$list = "http://en.wikipedia.org/wiki/List_of_stars_by_constellation";
	$all = file_get_contents($list);

	preg_match_all('|<li><a href="([^<>"]+)" title="List of stars in\s+([^<>"]+)"|Uis', $all, $m, PREG_SET_ORDER);
	foreach ($m as $v) {
		$stars_url[$v[2]] = $v[1];
	} 
	foreach ($stars_url as $key => $v) {
		// echo "$v\t\n";
		$stars_list_html = file_get_contents('http://en.wikipedia.org'.$v);
		preg_match('|<table class="wikitable sortable">(.*)</table|Uis', $stars_list_html, $M);
		preg_match_all('|<th>(<a[^<>]*title=")?([^<>"]+)["<]+|Uis', $M[1], $H);
		preg_match_all('|<tr>(.*)</tr>|Uis', $M[1], $N);
		foreach ($N[1] as $star) {
			$t_star['Constellation'] = $key;
			$t = explode('<td>', $star);
			unset($t[0]);
			if(count($t)> 1){
				foreach ($t as $k => $sv) {
					
					if($k == 1){
						preg_match('|title="([^<>]*)"|Uis', $sv, $m);
						$sv = $m[1];
					}
					$t_star[urldecode(strip_tags($H[2][$k-1]))] = preg_replace('|\s+|s',' ',trim(str_replace('&#160;','',preg_replace('|\[[^\]\[]+\]|Uis', '', strip_tags($sv)))));
				}
			} else{
				continue;
			}
			$stars_list[] = $t_star;
			unset($t_star);


		}
		// echo count($stars_list)."\n\n";
	}
	// print_r($stars_list);
	echo count($stars_list)."\n\n"
?>