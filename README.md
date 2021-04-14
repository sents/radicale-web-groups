# What does this do?
This a radicale web interface plugin that alters the default web plugin in 2 ways:

## Specifying other owner for collection
This plugin gives the option to specify an owner to a collection other than themselves.
To do this they still have to have write access to that path.

## Specifying access control lists for collections
There is also the option of setting an access control list (acl) for each collection.<br>
The acl is given in a comma separated list like `user1:rw,user2:r`, for giving
read & write acces to user1 and only read access for user2. The available right flags
can be found in the Radicale [Documentation](https://radicale.org/3.0.html#documentation/authentication-and-rights).

The acls are written as properties into the collections.

**For acls to take effect you still need a rights plugin that uses the acls!** <br>
For example:https://github.com/sents/radicale-rights-acl

# How to use this plugin
To use this plugin, install the python package for the user running radicale and set
```conf
[web]

type = radicale_web_groups
```
in your radicale configuration file.
