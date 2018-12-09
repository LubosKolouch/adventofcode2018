#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task2_1.pl
#
#        USAGE: ./task2_1.pl
#
#  DESCRIPTION: https://adventofcode.com/2018/day/2 part 1
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
use List::Util;

open (my $infile, '<', 'input2_1.txt');

my %globalcounts;

while (<$infile>) {
    chomp;
    
    my %counts;
    my $input = $_;

    foreach my $char ( split //, $input ) { $counts{$char}++ };

    my %counts2;

    for my $key (keys %counts) {
        $counts2{$counts{$key}} = 1 if $counts{$key} > 1;
    }

    for my $key (keys %counts2) {
        $globalcounts{$key}++;
    }

}

my $result = 1;

for my $key (keys %globalcounts) {
    $result = $result * $globalcounts{$key}++;
    }

say $result;
