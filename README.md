# Garuda
Automagically Exposing Djagno ORM over gRPC for microservices written in any other languages.
[link](https://github.com/dhilipsiva/garuda)

# Playground
Welcome, this is a playground for the Garuda package written by dhilipsiva.

Python 3.6.5 with Django 2.1 was used for trying out this project.

If you run in trouble running the commands try it with the pythonpath included.

```bash
PYTHONPATH=. ./sample/manage.py garuda
PYTHONPATH=. ./sample/manage.py garuda_server
```

Within this readme I have documented on how I got the sample working and some of the issues I encountered.

## Issues

1. No tests have been written
2. Generating proto files has some issues
4. Foreign key issue
5. DateTime issue
6. _to_dict functions seems very redundant
7. grpc server can only run insecure mode
8. No documentation on howto use the package but also the code lacks docs.

## HowTo
Steps describing on how to use the garuda package.

#### Setup
```bash 
pip install garuda
```
OR

Clone the repository (you can also clone mine): https://github.com/JoseJBoon/garuda-playground.git)
```bash
git clone https://github.com/dhilipsiva/garuda.git garuda
cd garuda
virtualenv --python=3.6 env
source env/bin/activate
python -m setup install
```

#### Creating the files for exposing the models to grpc
Create Models and migrate them

After that exucute the following command
```bash
./manage garuda
```

On my end this command failed to complete because the EntryLog model contained a enum of ACTION_FLAG_CHOICES. This enum did not get converted to a message in the proto file and resulted that the attribute, action_flag, at the EntryLog message to be of an undefined type.

To fix this I changed the attribute type to int32 and ran the command a second time but this time I disabled part of the code that already ran the first time.

## Generated files

The garuda command does the following:
1. Collects all the models of the installed apps.
2. Creates for each model a message object mirroring the model instance.
   For each model there will be 5 rpcs under the same service called Garuda
   Deleting, Updating, Reading, Creating and Reading w/ filter are the rpcs.
3. All messages and rpcs are being saved into the garuda.proto file.
4. For each app an app_crud.py and app_rpc are being generated.
5. Generates garuda_pb2.py and garuda_pb2_grpc.py based on the .proto.
6. Fixes the imports on the last 2 files

You should have after executing the command a proto file, garuda_pb_2.py and garuda_pb2_grpc.py representing the proto file, auto_garuda.py and each installed app 2 files: app_crud and app_rpc.

Crud files contain the Create, Read, Update and Delete functions with logic
rpc files contain the code logic for the server to execute when requested

auto_garuda is a collection of all the services in a single class and is used by the grpc server when executing add_GarudaServicer_to_server.

# Errors/Bugs
In the garuda command there is function called hacky.
`str(field.related_model).split(".")[-1].split("'")[0]`

I think the solution might be:
`field.related_model().__class__.__name__`

DateTime fields are not handled correctly by the to_dict() functions.
DateTime field gets converted to string in .proto but the string does not get converted back to datetime.

Problem with an enum not being generated into the protobuf

bug: ACTION_FLAG_CHOICES (enum) of EntryLog does not get created within the .proto
hacky can be changed to:
str(field.related_model).split(".")[-1].split("'")[0]
field.related_model().__class__.__name__

Message of a model takes string for ids

default=datetime.now
Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr)
default=datetime.datetime.now
bug: Because the lookup is larger it breaks

~~Foreign key value gets converted by the model_to_dict(obj) to str but an int is expected
TypeError: '2' has type str, but expected one of: int, long~~

~~User model: ReadUser results in the following message
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
      "grpc_status":2}"~~
