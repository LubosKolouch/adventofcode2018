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

open my $file, '<', $input;

my $gen = 0;

my %field;
my %rules;

while (<$file>) {
    chomp;
    next if /^$/msx;

    if (/initial/msx) {
        ($field{$gen}) = $_ =~ /\:\h+(.*)/msx;
            $field{$gen} = '.'x30 . $field{$gen} .'.'x30;
    } else {
        my ($rule, $result) = $_ =~ /(.*?)\h+.*\h+(.)/msx;
        $rules{$rule} = $result if $result eq '#';
    }
}

#say "0 ".$field{0};

for (1 .. 20) {
    $gen = $_;

    my $str = $field{$gen-1};
    $str = '..'.$str;

    my $count;

    for (2..length($str)-1) {
        my $test_pattern = substr( $str, $_-2, 5);
        if ($rules{$test_pattern}) {
            $field{$gen} .= '#';
            $count += $_ - 32;
        } else {
            $field{$gen} .= '.';
        }
    }

    say "$gen $count";
    #    say "$gen $field{$gen} $count";
}


