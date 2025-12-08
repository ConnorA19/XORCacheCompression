prefix=/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/x264/inst/amd64-linux.gcc
exec_prefix=${prefix}
bindir=${exec_prefix}/bin
libdir=${exec_prefix}/lib
includedir=${prefix}/include
ARCH=X86_64
SYS=LINUX
CC=/usr/bin/gcc
CFLAGS=-O4 -ffast-math   -DPARSEC_VERSION=3.0-beta-20150206 -Wall -I.  -DPARSEC_VERSION=3.0-beta-20150206 -fno-pie -no-pie -DHAVE_MALLOC_H -DHAVE_MMX -DARCH_X86_64 -DSYS_LINUX -DHAVE_PTHREAD -s -fomit-frame-pointer
ALTIVECFLAGS=
LDFLAGS=  -fno-pie -no-pie  -lm -lpthread -s
AS=yasm
ASFLAGS=-f elf -m amd64
EXE=
VIS=no
HAVE_GETOPT_LONG=1
DEVNULL=/dev/null
ECHON=echo -n
CONFIGURE_ARGS= '--enable-pthread' '--extra-asflags=' '--extra-cflags= -DPARSEC_VERSION=3.0-beta-20150206 -fno-pie -no-pie' '--extra-ldflags= -fno-pie -no-pie ' '--build=' '--host=' '--prefix=/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/x264/inst/amd64-linux.gcc'
