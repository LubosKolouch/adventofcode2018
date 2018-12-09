#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task2_2.pl
#
#        USAGE: ./task2_2.pl
#
#  DESCRIPTION: www.adventofcode.com
#               https://adventofcode.com/2018/day/2 part 2
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
use 5.026;
use autodie;
use List::Util;
use Data::Dumper;
use Array::Utils qw(:all);

sub get_string_diff {
    my $string1 = shift;
    my $string2 = shift;

    my $result = 0;
    for ( 0 .. length($string1) ) {
        my $char = substr( $string2, $_, 1 );
        if ( $char ne substr( $string1, $_, 1 ) ) {
            $result++;
        }
    }

    return $result;
}

open( my $infile, '<', 'input2_1.txt' );

my $pos = 0;
my %strings;

while (<$infile>) {
    chomp;
    $pos++;

    $strings{$pos} = $_;
}

for my $key ( keys %strings ) {
    my $string1 = $strings{$key};

    for my $key2 ( keys %strings ) {
        my $string2 = $strings{$key2};
        next if $string1 eq $string2;

        my @arr1 = split //, $string1;
        my @arr2 = split //, $string2;

        my $result = get_string_diff($string1, $string2);
        say "$result  $string1 $string2" if $result < 3;
    }
}
