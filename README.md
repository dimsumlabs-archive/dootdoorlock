dootdoorlock
============

The new doorlock at DSL - William Liang's DOOT from BOOT

On the pi, copy "doord" to /etc/init.d/

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
./door add
```


dependencies: pyserial, zdaemon
