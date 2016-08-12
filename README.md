
# ndbutils

Helper functions for working with gae ndb.


## Installation

```
$ git clone
$ python setup.py install
```

## Code Examples

define a class
```
class GaeUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    country = ndb.StringProperty()
```

write an instance where the first_name and last_name create the primary key    

```
inst = do_put(GaeUser, {'first_name':'pj', 'last_name': 'fitzpatrick',
  'country':'ireland' }, ['first_name','last_name'])
```

retrieve the instance
```
inst = get_instance(GaeUser, {'first_name':'pj', 'last_name': 'fitzpatrick'},['first_name','last_name'] )
```

update an instance
```
inst = do_put(GaeUser, {'first_name':'pj', 'last_name': 'fitzpatrick',
  'country':'republic or ireland' }, ['first_name','last_name'])
```


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
