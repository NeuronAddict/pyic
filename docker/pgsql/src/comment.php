<h2>filtered injection</h2>

<p>special chars (&#x27;&#x22;&#x3b;&#x23;&#x2d;) are filtereds, can you inject me?</p>
<p>note : to see log, set a cookie, get or post log=1</p>

<a href="/comment.php?id=1">/comment.php?id=1</a>

<?php

function log_($str) {
	if ($_REQUEST['log']=='1') {
		echo "<p>$str</p>\n";	
	}
}

function filter($id) {
	$ret = preg_replace('/[\'";#-]/', '', $id);
	log_("[*] filter id : \"$id\" ==> \"$ret\"");
	return $ret;
}

if(isset($_GET['id'])) {

	$id = filter($_GET['id']);

	$pgsql = pg_connect('host=postgres dbname=db user=pgsql password=pgsql');
	
	$query = "SELECT id, name, text FROM comments WHERE id=$id";

    log_('[*] "' . print_r($query, true) . '"');

    echo '<br /><br />';

    $stmt = pg_query($pgsql, $query);
	
	if($stmt) {

        while ($row = pg_fetch_row($stmt)) {
            print_r($row);

			echo "<p>comment " . $row[0] . "</p><h2>" . $row[1] . "</h2><p>" . $row[2] . "</p>";
		}
    }
    else {
        log_( "[-] ". pg_last_error ( $pgsql ));
    }

    pg_close($pgsql);

}

?>


