--- django/db/backends/sqlite3/schema.py.orig
+++ django/db/backends/sqlite3/schema.py
@@ -84,13 +84,29 @@
         def is_self_referential(f):
             return f.is_relation and f.remote_field.model is model
         # Work out the new fields dict / mapping
+        # The model state may contain fields whose columns no longer exist in
+        # the physical table (e.g. after a RemoveField that was not reflected
+        # in the model state). Filter to columns that actually exist in the
+        # old table so the INSERT ... SELECT does not reference stale columns.
+        with self.connection.cursor() as cursor:
+            old_columns = {
+                info.name
+                for info in self.connection.introspection.get_table_description(
+                    cursor, model._meta.db_table
+                )
+            }
         body = {
             f.name: f.clone() if is_self_referential(f) else f
             for f in model._meta.local_concrete_fields
+            if f.column in old_columns
         }
         # Since mapping might mix column names and default values,
         # its values must be already quoted.
-        mapping = {f.column: self.quote_name(f.column) for f in model._meta.local_concrete_fields}
+        mapping = {
+            f.column: self.quote_name(f.column)
+            for f in model._meta.local_concrete_fields
+            if f.column in old_columns
+        }
         # This maps field names (not columns) for things like unique_together
         rename_mapping = {}
         # If any of the new or altered fields is introducing a new PK,
