## Potential fix to AssertionError: No files found under certain path(s), please set `hibench.hadoop.examples.jar` manually

> NOT TESTED YET

- Download [hadoop 3.2.1](https://hadoop.apache.org/release/3.2.1.html) and extract in cluster master.

```bash
cd ~
curl https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
tar -xzf hadoop-3.2.1.tar.gz
```

- Copy non-existing folders from extracted hadoop to `/usr/lib/hadoop` ( not tried yet so no commands )
