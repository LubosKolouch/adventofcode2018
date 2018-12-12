#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task_12.pl
#
#        USAGE: ./task_12.pl  
#
#  DESCRIPTION: www.adventofcode.com task 12 part 1
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 12/12/2018 06:05:42 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use autodie;
use 5.026;
use Data::Dumper;

my $input = shift;
my $generations = shift;

open my $file, '<', $input;

my $gen = 0;
my $pad = $generations * 1.5;

my %field;
my %rules;
my %counts;
my %diffs;

while (<$file>) {
    chomp;
    next if /^$/msx;

    if (/initial/msx) {
        ($field{$gen}) = $_ =~ /\:\h+(.*)/msx;
            $field{$gen} = '.'x$pad . $field{$gen} .'.'x$pad;
    } else {
        my ($rule, $result) = $_ =~ /(.*?)\h+.*\h+(.)/msx;
        $rules{$rule} = $result if $result eq '#';
    }
}


for (1 .. $generations) {
    $gen = $_;

    my $str = $field{$gen-1};
    $str = '..'.$str;

    my $count;

    for (2..length($str)-1) {
        my $test_pattern = substr( $str, $_-2, 5);
        if ($rules{$test_pattern}) {
            $field{$gen} .= '#';
            $count += $_ - $pad -2;
        } else {
            $field{$gen} .= '.';
        }
    }

    $counts{$gen} = $count;
    $diffs{$gen} = $counts{$gen} - $counts{$gen-1};

    say "$gen $count ".$diffs{$gen};

    if ($diffs{$gen} == $diffs{$gen-1}) {
        say 'stable';
        print 'Total: ';
        my $result = $counts{$gen} + (50_000_000_000 - $gen) * $diffs{$gen};
        say $result;
        last;
    }
}


