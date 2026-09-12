--- libzfs.pyx.orig	2024-04-24 00:00:00.000000000 +0000
+++ libzfs.pyx	2024-04-24 00:00:00.000000000 +0000
@@ -4054,7 +4054,7 @@
             return self.get_snapshots_recursive()
 
     def get_snapshots_recursive(self, props=None):
-        for s in self.snapshots(props=props):
+        for s in self.get_snapshots(props=props):
             yield s
 
         for c in self.get_children(props=[]):
