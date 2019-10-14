<html>

<body>


    <?php include 'header.php' ?>

    <div>
    
        <form method="post">
            <input type="text" name="login" />
            <input type="password" name="pass" />
            <input type="submit" value="Login" />
        </form>
    
    </div>

    <pre>
        <?php

        $login = ($_REQUEST['login']);
        $pass = ($_REQUEST['pass']);
        
        if($login && $pass) {

            if($_COOKIE['as']) {
                $login = addslashes($login);
                $pass = addslashes($pass);
            }

            $pgsql = pg_connect('host=postgres dbname=db user=pgsql password=pgsql');

            $query = "SELECT username, pass FROM users WHERE username = '$login' AND pass = '$pass';";

            // print_r($query);

            echo '<br /><br />';

            $stmt = pg_query($pgsql, $query);
            if ($stmt) {

                /* fetch values */
                if ($row = pg_fetch_row($stmt)) {
                    $login = $row['username'];
                    $pass = $row['pass'];
                    echo "Logged";
                    //printf ("Logged as %s (%s)\n", $login, $pass);
                }
            }
            else {
                echo pg_last_error ( $pgsql );
            }

            pg_close($pgsql);
        }
        ?>
    </pre>

</body>

</html>

