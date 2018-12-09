#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task_9.pl
#
#        USAGE: ./task_9.pl
#
#  DESCRIPTION: https://adventofcode.com/2018/day/9
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/09/2018 10:36:39 AM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use 5.026;
use Data::Dumper;

my $players     = shift;
my $last_marble = shift;

$last_marble = $last_marble;
my %scores;
my $current_player = 0;
my $position       = 0;

my $marbles->{$position} = {next=>0, prev=>1};


for my $current_marble ( 1 .. $last_marble ) {
    $current_player++;
    $current_player = $current_player % $players;

    if ( $current_marble % 23 == 0 ) {
        $scores{$current_player} += $current_marble;

        for (1..7) {
            $position = $marbles->{$position}->{prev};
        }
        $scores{$current_player} += $position;

        my $prev = $marbles->{$position}->{prev};
        my $next = $marbles->{$position}->{next};

        $marbles->{$prev}->{next} = $next;
        $marbles->{$next}->{prev} = $prev;

        $position = $next;

    }
     else {

         # current position, move to next one
         # 0 - (1)
         $position = $marbles->{$position}->{next};
         my $old_next = $marbles->{$position}->{next};
         my $old_prev = $position;
         
         $marbles->{$position}->{next} = $current_marble;

         $position = $marbles->{$position}->{next};

         $marbles->{$position}->{next} = $old_next;
         $marbles->{$position}->{prev} = $old_prev;

         $position = $marbles->{$position}->{next};
         $marbles->{$position}->{prev} = $current_marble;

         $position = $current_marble;
    }

}

my $max = 0;

for ( keys %scores ) {
    $max = $scores{$_} if $scores{$_} > $max;
}
say $max;
