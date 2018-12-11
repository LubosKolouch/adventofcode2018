#!/usr/bin/perl
#===============================================================================
#
#         FILE: task_11.pl
#
#        USAGE: ./task_11.pl
#
#  DESCRIPTION: www.adventofcode.com Task 11
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (),
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/11/2018 07:43:08 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use 5.026;
use Data::Dumper;

my $max_square = shift;
my $grid       = shift;
my $grid_size = shift;

my %arr;
my %square_cache;

my $max       = 0;
my $maxx      = 0;
my $maxy      = 0;

for my $x ( 1 .. $grid_size ) {
    for my $y ( 1 .. $grid_size ) {
        $arr{$x}{$y} = ( ( ( ( ( ( $x + 10 ) * $y ) + $grid ) * ( $x + 10 ) ) / 100 ) % 10 ) - 5;
        $square_cache{$x}{$y}{1} = $arr{$x}{$y};
        if ( $arr{$x}{$y} > $max ) {
            $max  = $arr{$x}{$y};
            $maxx = $x;
            $maxy = $y;

            say "max $max $maxx $maxy";
        }
    }
}

for my $size ( 2 .. $max_square ) {
    say "to do size $size";

    #    2..3

    for my $x ( 1 .. $grid_size - $size + 1 ) {

        # 1 .. $grid_size -3 +1=298
        #    say "x $x";
        for my $y ( 1 .. $grid_size - $size + 1 ) {
            #   say "y $y";
            # say "arr " . $arr{$x}{$y};

            # 1 .. $grid_size-3+1 = 298

            my $value = $square_cache{$x}{$y}{ $size - 1 };

            #add extra column
            for my $dx ( $x .. $x + $size - 1 ) {
                $value += $arr{$dx}{ $y + $size - 1 };
            }

            #add extra row
            for my $dy ( $y .. $y + $size - 2 ) {
                $value += $arr{ $x + $size - 1 }{$dy};
            }

            $square_cache{$x}{$y}{$size} = $value;
            #  say "size $size value $value square_cache" . $square_cache{$x}{$y}{$size};

            if ( $value > $max ) {
                $max  = $value;
                $maxx = $x;
                $maxy = $y;

                   say "max $max $maxx $maxy size $size";
            }

        }

    }

}

say "max $max $maxx $maxy";

return 1;
