from google.appengine.ext import ndb
import types


def _produce_key(inpdetails, key_field_list):
    if isinstance(inpdetails, dict):
        return "_".join(map(lambda x: inpdetails[x], key_field_list))
    else:
        return "_".join(map(lambda x: getattr(inpdetails, x), key_field_list))


def get_instance_as_map(inst, get_output_fields, include_since=False):
    retmap = {}
    for key in get_output_fields:
        retmap[key] = getattr(inst, key)
    if include_since is True:
        datetimenow = datetime.datetime.now()
        calcseconds = (datetimenow-self.ds_dsts).seconds
        if calcseconds < 3600:
            retmap["ts_since"] = "{0}m Ago".format(int(calcseconds/60))
        else:
            retmap["ts_since"] = "{0}h:{1}m Ago".format(
                                int(calcseconds/60), int(calcseconds % 60))
    return retmap


def do_put(ModelName, inpdetails, key_field_list):
    inst_id = _produce_key(inpdetails, key_field_list)
    if isinstance(inpdetails, dict):
        retinst = ModelName(id=inst_id)
        for key, value in inpdetails.items():
            setattr(retinst, key, value)
        retinst.put()
        return retinst
    else:
        inpdetails.put()
        return inpdetails


def get_instance(ModelName, inpdetails, key_field_list):
    inst_id = _produce_key(inpdetails, key_field_list)
    return ModelName.get_by_id(inst_id)
