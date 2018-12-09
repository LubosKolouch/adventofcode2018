#!/usr/bin/perl 
#===============================================================================
#
#         FILE: t1.pl
#
#        USAGE: ./t1.pl  
#
#  DESCRIPTION: https://adventofcode.com/2018/day/3
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 12/02/2018 02:10:32 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use autodie;
use 5.026;
use Data::Dumper;

open (my $infile, '<', 'input3.txt');

my %fields;

while (<$infile>) {
    chomp;
    my ($shift, $dimensions) = split /:/msx;
    my ($shiftx, $shifty) = $shift =~ /(\d+),(\d+)/msx;
    my ($dimensionx, $dimensiony) = $dimensions =~ /(\d+)x(\d+)/msx;

    for my $x (1 .. $dimensionx) {
        for my $y (1 .. $dimensiony) {
            $fields{$shiftx + $x}{$shifty + $y}++;
        }
    }

}

my $result;

for my $key (keys %fields) {
    for my $key2 (keys %{$fields{$key}}) {
        $result++ if  $fields{$key}{$key2}>1;
    }
}

say $result;
