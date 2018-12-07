#!/usr/bin/perl 
#===============================================================================
#
#         FILE: t7.pl
#
#        USAGE: ./t7.pl
#
#  DESCRIPTION:
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (),
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 12/07/2018 08:43:41 AM
#     REVISION: ---
#===============================================================================
#
# worker_task - {id}->{task}
#                   ->{end}
#
#
# task_depend - {next}->{task_before}
#                     ->{task_before2}
#
# all_tasks

use strict;
use warnings;
use autodie;
use 5.026;

my %task_depend;
my %all_tasks;
my %task_in_progress;
my %worker_task;
my @finished_tasks;
my $actors        = shift // 5;
my $task_duration = shift // 60;
my $step        = -1;
open( my $file, '<', 'input7.txt' );

sub load_tasks {
    while (<$file>) {
        my ( $first, $second ) = $_ =~ /Step\h+(.).*?step\h+(.)/msx;
        $task_depend{$second}{$first} = 1;
        $all_tasks{$first}            = 1;
        $all_tasks{$second}           = 1;
    }
    close $file;
    return 1;
}

sub is_free_worker {
    my $id = shift;

    return 1 unless $worker_task{$id};
    return 0;
}

sub next_available_task {
    my $what;

    for ( sort keys %all_tasks ) {
        next if $task_in_progress{$_};
        unless ( defined $task_depend{$_} ) {
            $task_in_progress{$_} = 1;
            return $_;
        }
    }

    return 0;
}

sub cleanup_task {
    my $what = shift;

    for ( keys %all_tasks ) {
        delete $task_depend{$_}{$what} if defined $task_depend{$_}{$what};
        delete $task_depend{$_} if scalar keys %{ $task_depend{$_} } == 0;
    }
    push @finished_tasks, $what;

    return 1;

}

sub cleanup_worker_task {

    for ( keys %worker_task ) {
        if ( $worker_task{$_}->{end} == $step ) {
            cleanup_task( $worker_task{$_}{task} );
            delete $worker_task{$_};
        }
    }

    return 1;
}

sub print_worker_tasks {

    print $step. ' ';
    defined $worker_task{$_} ? print $worker_task{$_}{task} . ' ' : print '. ' for ( 1 .. $actors );
    say join '', @finished_tasks;

    return 1;
}

sub main {

    load_tasks;

    say "S " . join ' ', 1 .. $actors;

    while ( scalar %all_tasks > scalar @finished_tasks ) {
        $step++;

        cleanup_worker_task;

        for ( 1 .. $actors ) {
            next unless is_free_worker($_);

            my $what = next_available_task;
            last unless $what;

            $worker_task{$_}->{task} = $what;
            $worker_task{$_}->{end}  = $step + ord($what) - 64 + $task_duration;
        }

        print_worker_tasks;
    }

    return 1;

}

main;
