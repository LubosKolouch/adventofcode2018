## Please see file perltidy.ERR
## Please see file perltidy.ERR
#!/usr/bin/perl
#===============================================================================
#
#         FILE: task10.pl
#
#        USAGE: ./task10.pl
#
#  DESCRIPTION: www.adventofcode.com day 10 part 1
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/10/2018 01:35:49 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use autodie;
use 5.026;
use Data::Dumper;

open my $file, '<', 'input10.txt';
my %coord;
my $i = 0;

while (<$file>) {
    $i++;
    chomp;

    #position=< 42772, -21149> velocity=<-4,  2>
    my ( $x, $y, $vx, $vy ) = $_ =~ /position=<\h*(.*?),\h*(.*?)>\h*velocity=<\h*(.*?),\h*(.*?)>/msx;

    $coord{$i}{x}  = $x;
    $coord{$i}{y}  = $y;
    $coord{$i}{vx} = $vx;
    $coord{$i}{vy} = $vy;

    die if $i < 0;
    die unless $x;

}
close $file;

my $min_size = 1e6;

for ( 0 .. 20000 ) {
    my $step = $_;
    my $maxx = -200000;
    my $minx = 200000;

    my $maxy = -200000;
    my $miny = 200000;

    for ( sort keys %coord ) {

        my $x = $coord{$_}{x} + $coord{$_}{vx} * $step;
        my $y = $coord{$_}{y} + $coord{$_}{vy} * $step;

        #        say "min_size $min_size x $x y $y max $maxx maxy $maxy miny $miny minx $minx";
        $maxx = $x if $x > $maxx;
        $maxy = $y if $y > $maxy;

        $minx = $x if $x < $minx;
        $miny = $y if $y < $miny;

    }

    my $size = abs( $maxx - $minx + $maxy - $miny );
    if ( $size < $min_size ) {

        say "step $_ min_size $min_size minx $minx maxx $maxx maxy $maxy miny $miny";
        $min_size = $size;

        print_field($step, $minx, $maxx, $miny, $maxy) if ( $minx > 0 ) and ( $miny > 0 );
    }

}

sub print_field {
    my ( $step, $minx, $maxx, $miny, $maxy ) = @_;
    my @arr;

    for ( keys %coord ) {
        my $x = $coord{$_}{x} + $coord{$_}{vx} * $step;
        my $y = $coord{$_}{y} + $coord{$_}{vy} * $step;

        $arr[$x][$y] = 1;
    }

    for my $xa ( $minx .. $maxx ) {
        for my $ya ( $miny .. $maxy ) {
            if ($arr[$xa][$ya]) {
                print 'X';
            } else {
                print  ' '
            }
            
            
        }
        say ' ';
    }
    return 1;
}
