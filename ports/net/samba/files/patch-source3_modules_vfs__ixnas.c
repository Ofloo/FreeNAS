--- source3/modules/vfs_ixnas.c.orig	2026-09-13 15:44:04.825133000 +0200
+++ source3/modules/vfs_ixnas.c	2026-09-13 15:44:04.814331000 +0200
@@ -1470,7 +1470,7 @@
 
 static int fsp_set_times(files_struct *fsp, struct timespec *times, bool set_btime)
 {
-	int flag = set_btime ? AT_UTIMENSAT_BTIME : 0;
+	int flag = 0; /* FreeBSD utimensat has no btime flag */
 	if (fsp->fsp_flags.have_proc_fds) {
 		int fd = fsp_get_pathref_fd(fsp);
 		const char *p = NULL;
