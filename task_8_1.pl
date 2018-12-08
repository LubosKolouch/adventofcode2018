#!/usr/bin/perl 
#===============================================================================
#
#         FILE: task_8_1.pl
#
#        USAGE: ./task_8_1.pl
#
#  DESCRIPTION: https://adventofcode.com/2018/day/8
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Lubos Kolouch
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/08/2018 12:36:27 PM
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use autodie;
use 5.026;
use Data::Dumper;

my @arr;
my $result;

sub process_node {
    my $child_nodes = shift @arr;
    my $metadata = shift @arr;

    for (1 .. $child_nodes) {
        &process_node;
    }

    for (1 .. $metadata) {
        my $m = shift @arr;
        $result += $m;
    }

    return 1;
}

sub main {
    open my $infile, '<', 'input8.txt';
    my $str = <$infile>;
    close $infile;

    @arr = split / /, $str;

    &process_node;
    say $result;

    return 1;
}

main;

