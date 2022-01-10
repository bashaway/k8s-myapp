<?php
print "<html><body>\n";
print "Hello PHP Script!<br>\n";

print "<hr>\n";
print "<pre>";
ksort($_ENV);

foreach($_ENV as $key => $value){
    if ( preg_match( '/^HTTP/', $key ) ) {
        print "[\"$key\"] => $_ENV[$key]\n";
    }
}

print "\n";

foreach($_ENV as $key => $value){
    if ( ! preg_match( '/^HTTP/', $key ) ) {
        print "[\"$key\"] => $_ENV[$key]\n";
    }
}

print "</pre>";
print "</body></html>\n";
?>
