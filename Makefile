# Makefile for source rpm: redhat-rpm-config
# $Id$
NAME := redhat-rpm-config
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
