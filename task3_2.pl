#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task3_2.pl
#
#        USAGE: ./task3_2.pl
#
#  DESCRIPTION: https://adventofcode.com/2018/day/3 part 2
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
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
    my ($order) = $_ =~ /\#(\d+)/msx;
    my ($shift, $dimensions) = split /:/msx;
    my ($shiftx, $shifty) = $shift =~ /(\d+),(\d+)/msx;
    my ($dimensionx, $dimensiony) = $dimensions =~ /(\d+)x(\d+)/msx;

    for my $x (1 .. $dimensionx) {
        for my $y (1 .. $dimensiony) {
            $fields{$shiftx + $x}{$shifty + $y}++;
        }
    }
}

close $infile;

open ($infile, '<', 'input3.txt');
while (<$infile>) {
    chomp;
    my ($order) = $_ =~ /\#(\d+)/msx;
    my ($shift, $dimensions) = split /:/msx;
    my ($shiftx, $shifty) = $shift =~ /(\d+),(\d+)/msx;
    my ($dimensionx, $dimensiony) = $dimensions =~ /(\d+)x(\d+)/msx;

    my $ok = 1;

    for my $x (1 .. $dimensionx) {
        for my $y (1 .. $dimensiony) {
            $ok = 0 if $fields{$shiftx + $x}{$shifty + $y}>1;
        }
    }

    say $order  if $ok;
}


