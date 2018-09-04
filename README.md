# garuda
Automagically Exposing Djagno ORM over gRPC for microservices written in any other languages

# Playground
PYTHONPATH=. ./sample/manage.py garuda
PYTHONPATH=. ./sample/manage.py garuda_server

 Django 2.1, Python 3.6.5
 No tests has been written... there might be more bugs in it
 Generated crud files has alot of redundant model_to_dict functions

 bug: ACTION_FLAG_CHOICES (enum) of EntryLog does not get created within the .proto
 hacky can be changed to:
 str(field.related_model).split(".")[-1].split("'")[0]
 field.related_model().__class__.__name__

 Foreign key value gets converted by the model_to_dict(obj) to str but an int is expected
 TypeError: '2' has type str, but expected one of: int, long

 default=datetime.now
 Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr)
 default=datetime.datetime.now
 bug: Because the lookup is larger it breaks

 DateTime fields are within the protobuf represented as strings, but the generated code does not convert this.

 User model: ReadUser results in the following message
 _Rendezvous: <_Rendezvous of RPC that terminated with:
         status = StatusCode.UNKNOWN
         details = "Exception calling application: datetime.datetime(2018, 8, 30, 15, 46, 21, 461481, tzinfo=<UTC>)
                    has type datetime.datetime, but expected one of: bytes, unicode"
         debug_error_string =
               "{"created":"@1535719967.248868469",
         "description":"Error received from peer",
         "file":"src/core/lib/surface/call.cc",
         "file_line":1083,
         "grpc_message":"Exception calling application: datetime.datetime(2018, 8, 30, 15, 46, 21, 461481,
                         tzinfo=<UTC>) has type datetime.datetime, but expected one of: bytes, unicode",
         "grpc_status":2}"
