dootdoorlock
============

The new doorlock at DSL 2.0

On the pi, copy "init/doord" to /etc/init.d/

To enable at boot:
```
sudo update-rc.d doord defaults
```

daemon control:
```
sudo /etc/init.d/doord {start, stop, restart}
```

to add users:
```
Not yet implemented, use web interface for now
```
