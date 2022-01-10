#!/usr/bin/env perl
print "Content-type: text/html\n\n";
print "<html><body>\n";
print "Hello Perl Script!<br>\n";

print "<hr>\n";
print "<pre>";

foreach( sort keys %ENV ) {
    if ( $_ =~ /^HTTP/ ){
        print "[\"$_\"] => $ENV{$_}\n";
    }
}

print "\n";

foreach( sort keys %ENV ) {
    if ( $_ !~ /^HTTP/ ){
        print "[\"$_\"] => $ENV{$_}\n";
    }
}

print "</pre>";
print "</body></html>\n";

exit;
