# Makefile for program source directory in GNU NLS utilities package.
# Copyright (C) 1995, 1996, 1997 by Ulrich Drepper <drepper@gnu.ai.mit.edu>
#
# This file file be copied and used freely without restrictions.  It can
# be used in projects which are not available under the GNU Public License
# but which still want to provide support for the GNU gettext functionality.
# Please note that the actual code is *not* freely available.
#
# - Modified by Owen Taylor <otaylor@redhat.com> to use GETTEXT_PACKAGE
#   instead of PACKAGE and to look for po2tbl in ./ not in intl/
#
# - Modified by jacob berkman <jacob@ximian.com> to install
#   Makefile.in.in and po2tbl.sed.in for use with glib-gettextize

GETTEXT_PACKAGE = vips7
PACKAGE = vips
VERSION = 7.22.1

SHELL = /bin/sh


srcdir = /export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/po
top_srcdir = /export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src
VPATH = /export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/po

prefix = /export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/inst/amd64-linux.gcc
exec_prefix = ${prefix}
datarootdir = ${prefix}/share
datadir = ${datarootdir}
libdir = ${exec_prefix}/lib
localedir = $(libdir)/locale
gnulocaledir = $(datadir)/locale
gettextsrcdir = $(datadir)/glib-2.0/gettext/po
subdir = po

INSTALL = /export/scratch/users/anton386/remove_me2/parsec-benchmark/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
MKINSTALLDIRS = $(top_srcdir)//export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src//mkinstalldirs

CC = /usr/bin/gcc
GENCAT = @GENCAT@
GMSGFMT = /usr/bin/msgfmt
MSGFMT = /usr/bin/msgfmt
MSGFMT_OPTS = -c
XGETTEXT = /usr/bin/xgettext
MSGMERGE = msgmerge

DEFS = -DHAVE_CONFIG_H
CFLAGS =   -DPARSEC_VERSION=3.0-beta-20150206
CPPFLAGS = 

INCLUDES = -I.. -I$(top_srcdir)/intl

COMPILE = $(CC) -c $(DEFS) $(INCLUDES) $(CPPFLAGS) $(CFLAGS) $(XCFLAGS)

SOURCES = 
POFILES =  en_GB.po de.po
GMOFILES =  en_GB.gmo de.gmo
DISTFILES = LINGUAS ChangeLog Makefile.in.in POTFILES.in $(GETTEXT_PACKAGE).pot \
$(POFILES) $(GMOFILES) $(SOURCES)

POTFILES = \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/acquire/im_clamp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_deviate.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_point_bilinear.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_linreg.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/arith_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_subtract.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_stats.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_maxpos.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_maxpos_avg.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_maxpos_vec.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_invert.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_sign.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/round.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_measure.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/math.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_minpos.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_abs.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_recomb.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_cross_phase.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_divide.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_bandmean.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_lintra.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_remainder.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/power.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_add.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_avg.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/arithmetic/im_multiply.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/boolean/boolean.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/boolean/bool_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/cimg/cimg_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_rad2float.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LCh2UCS.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_icc_transform.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/disp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_dE_fromLab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_Yxy2XYZ.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LabQ2disp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_Lab2LabS.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LabQ2Lab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_UCS2LCh.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LabS2Lab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_dECMC_fromLab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LabQ2LabS.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_Lab2XYZ.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_disp2XYZ.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_XYZ2disp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/colour.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_float2rad.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_Lab2LCh.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/colour_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/derived.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LabS2LabQ.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_dE00_fromLab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_lab_morph.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_XYZ2Yxy.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_Lab2LabQ.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_LCh2Lab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/colour/im_XYZ2Lab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_insert.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_mask2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_gaussnoise.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_flipver.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_falsecolour.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_vips2mask.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_clip2fmt.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_ri2c.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_system.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_text.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_zoom.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/conver_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_copy_file.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_c2real.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_grid.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_c2imag.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_scaleps.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_fliphor.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_scale.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_black.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_tbjoin.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_replicate.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_embed.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_lrjoin.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_rot180.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_extract.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_wrap.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_c2rect.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_copy.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_rot90.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_c2amph.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_msb.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_system_image.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_subsample.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_rot270.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/conversion/im_gbandjoin.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_contrast_surface.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_gradcor.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_compass.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_convsep.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_conv.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_fastcor.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/convol_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_conv_f.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_addgnoise.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_spcor.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_convsep_f.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/convolution/im_sharpen.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_tile_cache.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_ppm2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/format.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2tiff.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2csv.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2ppm.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_png2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/format_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_analyze2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_magick2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2raw.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_tiff2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_exr2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/matlab.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_jpeg2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_csv2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2png.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/radiance.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_raw2vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/im_vips2jpeg.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_freq_mask.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_phasecor_fft.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/fft_sp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/fmaskcir.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_fractsurf.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_freqflt.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/fmask4th.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_invfft.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/freq_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_rotquad.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_invfftr.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_fwfft.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/freq_filt/im_disp_ps.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_gammacorrect.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_hist.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_project.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_stdif.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_mpercent.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histnD.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histspec.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_identity.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histindexed.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/hist_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_hsp.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histgr.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_buildlut.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/tone.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histeq.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_histplot.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_lhisteq.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_invertlut.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_heq.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/histograms_lut/im_maplut.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/smudge_area.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/flood.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/im_insertplace.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/plot_point.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/line_draw.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/im_plotmask.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/im_paintrect.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/inplace_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/inplace/im_circle.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/check.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/sink.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/rect.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/semaphore.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/memory.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/region.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_setbuf.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/callback.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_wrapmany.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_guess_prefix.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_generate.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/init.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/sinkscreen.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_mapfile.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/package.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/debug.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_init_world.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_partial.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/meta.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_setupout.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/base64.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/time.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_histlin.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/object.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_image.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_cp_desc.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/buf.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/util.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_prepare.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_binfile.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/header.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/sinkmemory.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/window.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/sinkdisc.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_demand_hint.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/buffer.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_open.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/error.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/dispatch_types.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/threadpool.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_writeline.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_open_vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_unmapfile.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/im_close.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_matcat.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/rw_mask.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_matinv.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_mattrn.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_matmul.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_logmasks.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/im_gaussmasks.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/rotmask.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/matalloc.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mask/mask_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_profile.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_label_regions.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/morph_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_zerox.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_erode.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_cntlines.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_rank.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_dilate.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/morphology/im_rank_image.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/mosaicing_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_lrmerge.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_remosaic.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_tbmosaic.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_chkpair.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_tbcalcon.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/global_balance.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_tbmerge.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_maxpos_subpel.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_improve.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_avgdxdy.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_align_bands.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_lrcalcon.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_initialize.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/match.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/mosaic1.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_clinear.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/im_lrmosaic.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_simcontr.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/glds_funcs.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/cooc_funcs.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_grey.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/other_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_benchmark.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_meanstd.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_zone.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_sines.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_eye.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_spatres.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_make_xy.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/other/im_dif_std.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/relational/im_ifthenelse.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/relational/relational_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/relational/relational.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/relational/im_blend.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/im_affine.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/im_stretch3.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/transform.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/im_shrink.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/resample_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/interpolate.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/im_rightshift_size.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/video/video_dispatch.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/video/im_video_test.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/video/im_video_v4l1.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/iofuncs/vips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/iofuncs/edvips.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/iofuncs/vipsthumbnail.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/iofuncs/header.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/mosaicing/find_mosaic.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/mosaicing/mergeup.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/simcontr.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/squares.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/sines.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/glds_features.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/glds.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/spatres.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/cooc.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/tools/other/cooc_features.c \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/VDisplay.cc \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/VError.cc \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/VImage.cc \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/vipsc++.cc \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/VMask.cc \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/VDisplay.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/VImage.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/vipscpp.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/VError.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/VMask.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvipsCC/include/vips/vipsc++.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/cimg/CImg.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/format/dbh.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/type.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/struct.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/deprecated.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/image.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/mosaicing.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/freq_filt.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/buf.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/threadpool.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/header.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/inlines.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/generate.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/cimg_funcs.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/object.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/other.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/util.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/inplace.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/version.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/private.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/boolean.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/conversion.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/almostdeprecated.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/resample.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/dispatch.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/rect.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/semaphore.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/disp.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/colour.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/intl.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/region.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/morphology.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/format.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/internal.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/interpolate.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/check.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/memory.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/meta.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/transform.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/error.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/convolution.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/callback.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/mask.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/vips.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/debug.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/histograms_lut.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/thread.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/relational.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/video.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/include/vips/arithmetic.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/iofuncs/base64.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/mosaic.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/merge.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/mosaicing/global_balance.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/templates.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/video/im_video_v4l1.h \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/cimg/cimg.cpp \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/bicubic.cpp \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/nohalo.cpp \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/vsqbs.cpp \
	/export/scratch/users/anton386/remove_me2/parsec-benchmark/pkgs/apps/vips/src/libvips/resample/lbb.cpp

CATALOGS =  en_GB.gmo de.gmo
CATOBJEXT = .gmo
INSTOBJEXT = .mo

.SUFFIXES:
.SUFFIXES: .c .o .po .pox .gmo .mo .msg .cat

.c.o:
	$(COMPILE) $<

.po.pox:
	$(MAKE) $(GETTEXT_PACKAGE).pot
	$(MSGMERGE) $< $(srcdir)/$(GETTEXT_PACKAGE).pot -o $*.pox

.po.mo:
	$(MSGFMT) -o $@ $<

.po.gmo:
	file=$(srcdir)/`echo $* | sed 's,.*/,,'`.gmo \
	  && rm -f $$file && $(GMSGFMT) $(MSGFMT_OPTS) -o $$file $<

.po.cat:
	sed -f ../intl/po2msg.sed < $< > $*.msg \
	  && rm -f $@ && $(GENCAT) $@ $*.msg


all: all-yes

all-yes: $(CATALOGS)
all-no:

$(srcdir)/$(GETTEXT_PACKAGE).pot: $(POTFILES)
	$(XGETTEXT) --default-domain=$(GETTEXT_PACKAGE) --directory=$(top_srcdir) \
	  --add-comments --keyword=_ --keyword=N_ \
	  --keyword=C_:1c,2 \
	  --keyword=NC_:1c,2 \
	  --keyword=g_dngettext:2,3 \
	  --flag=N_:1:pass-c-format \
	  --flag=C_:2:pass-c-format \
	  --flag=NC_:2:pass-c-format \
	  --flag=g_dngettext:2:pass-c-format \
          --flag=g_strdup_printf:1:c-format \
          --flag=g_string_printf:2:c-format \
          --flag=g_string_append_printf:2:c-format \
          --flag=g_error_new:3:c-format \
          --flag=g_set_error:4:c-format \
          --flag=g_markup_printf_escaped:1:c-format \
          --flag=g_log:3:c-format \
          --flag=g_print:1:c-format \
          --flag=g_printerr:1:c-format \
          --flag=g_printf:1:c-format \
          --flag=g_fprintf:2:c-format \
          --flag=g_sprintf:2:c-format \
          --flag=g_snprintf:3:c-format \
          --flag=g_scanner_error:2:c-format \
          --flag=g_scanner_warn:2:c-format \
	  --files-from=$(srcdir)/POTFILES.in \
	&& test ! -f $(GETTEXT_PACKAGE).po \
	   || ( rm -f $(srcdir)/$(GETTEXT_PACKAGE).pot \
		&& mv $(GETTEXT_PACKAGE).po $(srcdir)/$(GETTEXT_PACKAGE).pot )

install: install-exec install-data
install-exec:
install-data: install-data-yes
install-data-no: all
install-data-yes: all
	if test -r "$(MKINSTALLDIRS)"; then \
	  $(MKINSTALLDIRS) $(DESTDIR)$(datadir); \
	else \
	  $(SHELL) $(top_srcdir)/mkinstalldirs $(DESTDIR)$(datadir); \
	fi
	@catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  case "$$cat" in \
	    *.gmo) destdir=$(gnulocaledir);; \
	    *)     destdir=$(localedir);; \
	  esac; \
	  lang=`echo $$cat | sed 's/\$(CATOBJEXT)$$//'`; \
	  dir=$(DESTDIR)$$destdir/$$lang/LC_MESSAGES; \
	  if test -r "$(MKINSTALLDIRS)"; then \
	    $(MKINSTALLDIRS) $$dir; \
	  else \
	    $(SHELL) $(top_srcdir)/mkinstalldirs $$dir; \
	  fi; \
	  if test -r $$cat; then \
	    $(INSTALL_DATA) $$cat $$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT); \
	    echo "installing $$cat as $$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT)"; \
	  else \
	    $(INSTALL_DATA) $(srcdir)/$$cat $$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT); \
	    echo "installing $(srcdir)/$$cat as" \
		 "$$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT)"; \
	  fi; \
	  if test -r $$cat.m; then \
	    $(INSTALL_DATA) $$cat.m $$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m; \
	    echo "installing $$cat.m as $$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m"; \
	  else \
	    if test -r $(srcdir)/$$cat.m ; then \
	      $(INSTALL_DATA) $(srcdir)/$$cat.m \
		$$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m; \
	      echo "installing $(srcdir)/$$cat as" \
		   "$$dir/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m"; \
	    else \
	      true; \
	    fi; \
	  fi; \
	done
	if test "$(PACKAGE)" = "glib"; then \
	  if test -r "$(MKINSTALLDIRS)"; then \
	    $(MKINSTALLDIRS) $(DESTDIR)$(gettextsrcdir); \
	  else \
	    $(SHELL) $(top_srcdir)/mkinstalldirs $(DESTDIR)$(gettextsrcdir); \
	  fi; \
	  $(INSTALL_DATA) $(srcdir)/Makefile.in.in \
			  $(DESTDIR)$(gettextsrcdir)/Makefile.in.in; \
	else \
	  : ; \
	fi

# Define this as empty until I found a useful application.
installcheck:

uninstall:
	catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  lang=`echo $$cat | sed 's/\$(CATOBJEXT)$$//'`; \
	  rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(GETTEXT_PACKAGE)$(INSTOBJEXT); \
	  rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m; \
	  rm -f $(DESTDIR)$(gnulocaledir)/$$lang/LC_MESSAGES/$(GETTEXT_PACKAGE)$(INSTOBJEXT); \
	  rm -f $(DESTDIR)$(gnulocaledir)/$$lang/LC_MESSAGES/$(GETTEXT_PACKAGE)$(INSTOBJEXT).m; \
	done
	if test "$(PACKAGE)" = "glib"; then \
	  rm -f $(DESTDIR)$(gettextsrcdir)/Makefile.in.in; \
	fi

check: all

dvi info tags TAGS ID:

mostlyclean:
	rm -f core core.* *.pox $(GETTEXT_PACKAGE).po *.old.po cat-id-tbl.tmp
	rm -fr *.o

clean: mostlyclean

distclean: clean
	rm -f Makefile Makefile.in POTFILES *.mo *.msg *.cat *.cat.m

maintainer-clean: distclean
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."
	rm -f $(GMOFILES)

distdir = ../$(GETTEXT_PACKAGE)-$(VERSION)/$(subdir)
dist distdir: update-po $(DISTFILES)
	dists="$(DISTFILES)"; \
	for file in $$dists; do \
	  ln $(srcdir)/$$file $(distdir) 2> /dev/null \
	    || cp -p $(srcdir)/$$file $(distdir); \
	done

update-po: Makefile
	$(MAKE) $(GETTEXT_PACKAGE).pot
	tmpdir=`pwd`; \
	cd $(srcdir); \
	catalogs='$(CATALOGS)'; \
	for cat in $$catalogs; do \
	  cat=`basename $$cat`; \
	  lang=`echo $$cat | sed 's/\$(CATOBJEXT)$$//'`; \
	  echo "$$lang:"; \
	  if $(MSGMERGE) $$lang.po $(GETTEXT_PACKAGE).pot -o $$tmpdir/$$lang.new.po; then \
	    if cmp $$lang.po $$tmpdir/$$lang.new.po >/dev/null 2>&1; then \
	      rm -f $$tmpdir/$$lang.new.po; \
            else \
	      if mv -f $$tmpdir/$$lang.new.po $$lang.po; then \
	        :; \
	      else \
	        echo "msgmerge for $$lang.po failed: cannot move $$tmpdir/$$lang.new.po to $$lang.po" 1>&2; \
	        rm -f $$tmpdir/$$lang.new.po; \
	        exit 1; \
	      fi; \
	    fi; \
	  else \
	    echo "msgmerge for $$cat failed!"; \
	    rm -f $$tmpdir/$$lang.new.po; \
	  fi; \
	done

# POTFILES is created from POTFILES.in by stripping comments, empty lines
# and Intltool tags (enclosed in square brackets), and appending a full
# relative path to them
POTFILES: POTFILES.in
	( if test 'x$(srcdir)' != 'x.'; then \
	    posrcprefix='$(top_srcdir)/'; \
	  else \
	    posrcprefix="../"; \
	  fi; \
	  rm -f $@-t $@ \
	    && (sed -e '/^#/d' 						\
		    -e "s/^\[.*\] +//" 					\
		    -e '/^[ 	]*$$/d' 				\
		    -e "s@.*@	$$posrcprefix& \\\\@" < $(srcdir)/$@.in	\
		| sed -e '$$s/\\$$//') > $@-t \
	    && chmod a-w $@-t \
	    && mv $@-t $@ )

Makefile: Makefile.in.in ../config.status POTFILES
	cd .. \
	  && $(SHELL) ./config.status $(subdir)/$@.in

# Tell versions [3.59,3.63) of GNU make not to export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
